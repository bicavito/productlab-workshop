#!/usr/bin/env python3
"""
Bet Ranker — Signal Scoring (Arcate Light)
Reads:   _context/signals_segmented.json
Outputs: _context/bets.json

Scoring model mirrors Arcate's Fermi Leverage Model (simplified):
  signal_contribution = sqrt(TYPE_WEIGHT[type])
  per bet:
    weighted_sum     = Σ signal_contribution
    customer_weight  = log10(Σ ARR_PROXY[customer_size] + 1)   ← Fermi: OOM estimate, log-compressed
    volume_factor    = weighted_sum / sqrt(n + 5)
    score            = customer_weight × volume_factor

Design rationale:
  - ARR_PROXY uses 10× steps (Fermi order-of-magnitude reasoning)
  - log10 compression prevents any single XL customer from dominating
  - Severity is display-only: strategic type (deal-loss/problem/friction/mention)
    already encodes urgency — stacking severity on top would double-count
  - This mirrors how Arcate impact.ts works: log10(totalARR) × maxIcpWeight

No external dependencies. Pure Python 3 stdlib.
Run from the starter-repo root:
    python bet_ranker/score.py
"""

import json
import math
import os
from collections import defaultdict

# ─── Paths ────────────────────────────────────────────────────────────────────

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
INPUT_JSON  = os.path.join(SCRIPT_DIR, '..', '_context', 'signals_segmented.json')
OUTPUT_JSON = os.path.join(SCRIPT_DIR, '..', '_context', 'bets.json')

# ─── Weights (mirrors Arcate impact.ts) ───────────────────────────────────────

# Customer size → order-of-magnitude ARR proxy (10× steps = Fermi scale)
# Arcate uses actual ARR; here we use a best-guess OOM estimate per tier.
# These are summed across all signals in a bet, then log10-compressed —
# so breadth of customer evidence matters, not just the single largest name.
ARR_PROXY = {'XL': 10_000_000, 'L': 1_000_000, 'M': 100_000, 'S': 10_000, 'XS': 1_000}

# Signal type → strategic weight (Arcate: deal-loss=30, problem=10, friction=3, mention=1)
TYPE_WEIGHTS = {'deal-loss': 30, 'problem': 10, 'friction': 3, 'mention': 1}

# Severity weights kept for display only — not used in Fermi scoring path.
# (Arcate uses severity only in its no-ARR fallback mode, not the main formula.)
SEVERITY_WEIGHTS = {'High': 3, 'Medium': 2, 'Low': 1}

# Volume dampening constant (Arcate: K=5)
K = 5


def arr_proxy(size: str) -> int:
    """Order-of-magnitude ARR estimate for a customer size tier."""
    return ARR_PROXY.get(size.strip().upper(), 1_000)

def type_weight(signal_type: str) -> float:
    return TYPE_WEIGHTS.get(signal_type.strip().lower(), 1)

def severity_weight(severity: str) -> int:
    """For display/breakdown only — not used in the Fermi scoring path."""
    return SEVERITY_WEIGHTS.get(severity.strip().capitalize(), 1)

def score_label(score: float) -> str:
    # Thresholds calibrated for log-compressed model (scores typically 5–35)
    if score >= 20:
        return 'High Leverage'
    elif score >= 10:
        return 'Medium Leverage'
    else:
        return 'Low Confidence'


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    # Validate input
    if not os.path.exists(INPUT_JSON):
        print(f"✗ File not found: {INPUT_JSON}")
        print("  Run the segmentation step first (see bet_ranker/segment.md).")
        return

    # Read and group by bet
    bets_map = defaultdict(list)
    with open(INPUT_JSON, encoding='utf-8') as f:
        signals = json.load(f)
    for signal in signals:
        bet = signal.get('bet', '').strip() or 'Uncategorized'
        bets_map[bet].append(signal)

    # Score each bet
    bets = []
    for bet_title, signals in bets_map.items():
        n = len(signals)

        # Customer weight: Fermi OOM estimate
        # Sum proxy ARR across all signals, then log10-compress.
        # This mirrors Arcate's log10(totalARR + 1) × maxIcpWeight, adapted
        # for a workshop where actual ARR is unknown.
        # Effect: XL breadth accumulates, but no single tier dominates.
        total_proxy_arr = sum(arr_proxy(s.get('customer_size', 'XS')) for s in signals)
        customer_weight = math.log10(total_proxy_arr + 1)
        top_size        = max(signals, key=lambda s: arr_proxy(s.get('customer_size', 'XS'))) \
                              .get('customer_size', 'XS').strip().upper()

        # Weighted signal sum: each signal contributes sqrt(type_weight) only.
        # Severity is intentionally excluded — type already encodes urgency.
        # (Arcate: weightedSignalSum += sqrt(SIGNAL_TYPE_WEIGHTS[type]))
        weighted_sum = sum(
            math.sqrt(type_weight(s.get('type', 'mention')))
            for s in signals
        )

        # Volume-dampened leverage
        volume_factor = weighted_sum / math.sqrt(n + K)
        score = round(customer_weight * volume_factor, 2)

        bets.append({
            'title':             bet_title,
            'score':             score,
            'label':             score_label(score),
            'signal_count':      n,
            'top_customer_size': top_size,
            'signals': [
                {
                    'text':     s.get('raw_signal', '').strip(),
                    'type':     s.get('type', '').strip(),
                    'severity': s.get('severity', '').strip(),
                }
                for s in signals
            ],
        })

    # Sort by score, assign rank
    bets.sort(key=lambda b: b['score'], reverse=True)
    for i, bet in enumerate(bets):
        bet['rank'] = i + 1

    # Write output
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(bets, f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"✓ Scored {len(bets)} bets → viewer/bets.json\n")
    for bet in bets:
        bar = '█' * min(int(bet['score'] / 10), 20)
        print(f"  #{bet['rank']:>2}  {bet['title']:<30} {bet['label']:<18} "
              f"score: {bet['score']:>7}  signals: {bet['signal_count']}  top: {bet['top_customer_size']}")
        print(f"       {bar}")
        print()

    print("Open bet_ranker/viewer/index.html in your browser to see the full ranking.")


if __name__ == '__main__':
    main()
