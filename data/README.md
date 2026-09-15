# Your Data Goes Here

This folder contains the datasets the app reads.

## To swap the dataset

Open `src/app.js` and change line 3:

```js
const DATA_FILE = '../data/dataset_a.json'; // change this
```

Replace `dataset_a.json` with `dataset_b.json` — or with your own file.

## To use your own data

1. Create a new `.json` file in this folder.
2. Copy the structure from `dataset_a.json`.
3. Replace `label`, `fields`, and `items` with your data.
4. Point `DATA_FILE` in `app.js` to your new file.

## The data format

```json
{
  "label": "Name shown in the header",
  "fields": [
    { "key": "column_name", "label": "Column Header", "filterable": false, "badge": false }
  ],
  "items": [
    { "column_name": "value" }
  ]
}
```

**field options:**
- `filterable: true` — adds filter buttons above the table for this column
- `badge: true` — renders the value as a colored badge (uses the value as CSS class)

## Included datasets

| File | Contents |
|---|---|
| `dataset_a.json` | Customer signals (20 items) |
| `dataset_b.json` | Feature requests derived from the same signals (20 items) |
