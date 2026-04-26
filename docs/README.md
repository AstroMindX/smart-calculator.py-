# Smart Calculator

Smart Calculator includes:
- a Python CLI calculator for multi-number workflows,
- a browser UI for quick two-number operations,
- persisted calculation history in both experiences,
- a GitHub Pages deployment workflow for the UI.

## Project structure

- `src/smart_calculator.py` — CLI app with history, duplicate detection, and version banner.
- `ui/index.html` — calculator UI layout.
- `ui/style.css` — UI styling.
- `ui/script.js` — browser logic and local history.
- `.github/workflows/deploy-ui.yml` — CI smoke test + GitHub Pages deploy workflow.
- `docs/CHANGELOG.md` — release notes.
- `VERSION` — canonical app version for this repository.

## Features

### CLI features
- Add, subtract, multiply, divide, and percentage for multiple numbers.
- Reuse previous number list (`yes/no` prompt flow).
- Duplicate-operation detection.
- Persistent history saved to `history.txt`.
- Up to 10 recent history records in memory.

### UI features
- Add, subtract, multiply, divide, and percentage (% of) operations.
- Validation for missing numbers.
- Division-by-zero guard.
- Swap input button.
- Press Enter in either input to calculate.
- History list stored in browser localStorage.
- Clear history button.

## Run instructions

### 1) CLI

From the repository root:

```bash
python src/smart_calculator.py
```

### 2) Browser UI

Open `ui/index.html` directly in your browser, or serve the repo folder with a simple static server.

## Deploy on GitHub Pages

1. Push this repository to GitHub.
2. Ensure your default branch is named `main` (or adjust the workflow trigger).
3. In GitHub, open **Settings → Pages** and set **Source** to **GitHub Actions**.
4. Push to `main` (or `work` in this repo) or run the workflow manually via **Actions** to deploy.
4. Push to `main` (or run the workflow manually via **Actions**) to deploy.

The workflow publishes the contents of `ui/` as the Pages site.

## Versioning

This project uses Semantic Versioning (`MAJOR.MINOR.PATCH`).

- `VERSION` contains the current project version.
- `docs/CHANGELOG.md` tracks user-facing changes.

Current version: **v4.1.0**.
