# Sample Python App

A minimal Python package layout you can push to a remote Git repository (GitHub, GitLab, Azure DevOps, etc.). It uses a **src layout**, **`pyproject.toml`**, a small CLI, tests, and optional GitHub Actions CI.

## Layout

| Path | Purpose |
|------|---------|
| `src/sample_python_app/` | Application code |
| `tests/` | Pytest tests |
| `pyproject.toml` | Project metadata, dependencies, console script |
| `requirements.txt` | Hints for `pip`; prefer `pip install -e ".[dev]"` |
| `.gitignore` | Python / venv / tooling ignores |
| `LICENSE` | MIT (change if your org requires another license) |
| `.github/workflows/ci.yml` | CI on push/PR (remove if you do not use GitHub) |

## Requirements

- Python 3.10+

## Quick start (local)

```bash
cd samples/sample-python-app
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
# source .venv/bin/activate

pip install -e ".[dev]"
pytest -v
python -m sample_python_app
python -m sample_python_app --name Alice
sample-app --name Bob
```

## Publish to a remote repository

1. Create an empty repository on your host (no README if you already have one locally).
2. From this folder:

   ```bash
   git init
   git add .
   git commit -m "Initial commit: sample Python application"
   git branch -M main
   git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
   git push -u origin main
   ```

3. Replace `YOUR_USER/YOUR_REPO` with your URL. Update `pyproject.toml` `[project.urls]` to match.

## Customize

- Rename `sample_python_app` (folder and imports) and `sample-app` in `[project.scripts]` in `pyproject.toml`.
- Set `authors` and URLs in `pyproject.toml`.
- Add runtime dependencies under `[project] dependencies = [...]`.
