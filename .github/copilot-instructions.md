# Copilot Instructions

Purpose
- Help AI coding agents become productive quickly by describing discovery steps, repo-specific probes, and merge guidance.

If this file already exists: merge rather than overwrite. Preserve human-written sections and append missing probes below.

Quick discovery checklist (run immediately)
- List top-level files: `ls -la` or open workspace root.
- Search for language manifests: `package.json`, `pyproject.toml`, `requirements.txt`, `Pipfile`, `pom.xml`, `go.mod`, `Cargo.toml`.
- Search for CI/workflow and infra: `.github/workflows/*`, `Dockerfile`, `docker-compose.yml`.
- Identify entrypoints: common folders `src/`, `app/`, `cmd/`, `main.go`, `manage.py`, `server.ts`.

How to infer architecture
- If `Dockerfile` or `docker-compose.yml` exists, inspect service names and ports to map services.
- If monorepo (multiple `package.json` or `pyproject.toml` under folders), treat each package as a separate service boundary.
- Look for API routes in `src/*/routes`, `routes/`, `controllers/`, or `handlers/` to find surface area.

Build / test / run commands (discovery-first)
- Node: check `package.json` scripts (`npm run build`, `npm test`, `npm run dev`).
- Python: check for `pyproject.toml`, `requirements.txt`; try `python -m pytest` and `python -m <module>` if entrypoint found.
- .NET/Java/Go: inspect respective manifests and use `dotnet build`, `mvn test`, `go test ./...` as applicable.
- If unsure, ask: "Which command runs tests or starts the app locally?"

Project-specific conventions to probe
- Linting/formatting: look for `.eslintrc`, `pyproject.toml` `[tool.black]`, `ruff`, `.prettierrc` and run them if present.
- Testing patterns: find `tests/`, `spec/`, or `__tests__` folders and sample test naming conventions.
- Configuration: prefer environment variables via `.env` or `config/*.yaml` — do not hardcode secrets.

Integration points
- Look for external service clients (`aws-sdk`, `boto3`, `psycopg2`, `pg`, `sqlalchemy`, `mongodb` drivers) to surface dependencies.
- Note any external APIs, auth providers, or database connection strings in `config` or `secrets` scaffolding.

Editing and PR guidance
- Make minimal, well-scoped changes. Run local tests and linters before proposing changes.
- If adding behavior, update or add tests under existing test patterns.

If anything is missing or unclear
- Open relevant files and summarize findings (top-level manifest, main entrypoint, test command). If you cannot determine runtime commands, ask the human.

Examples of targeted probes (copy into agent runbook)
- `git status --porcelain --untracked-files=no` — check repo cleanliness.
- `rg --hidden "pytest|unittest|describe\(|it\(" -S || true` — locate test frameworks.
- `rg --hidden "FROM |EXPOSE |CMD |ENTRYPOINT" .github Dockerfile -S || true` — inspect Docker usage.

Author: generated for repo by AI helper. Ask for feedback to iterate.
