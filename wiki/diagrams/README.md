# Diagrams

Mermaid source (`.mmd`) + rendered `.png`. Diagrams are colored by status:
green = done, blue = active, yellow = to do.

## Regenerate a diagram

`mmdc` (Mermaid CLI) is installed globally via npm. From this folder:

```powershell
mmdc -b white -i current-state.mmd -o current-state.png
```

Render all three:

```powershell
foreach ($f in @("current-state","target-architecture","roadmap")) {
  mmdc -b white -i "$f.mmd" -o "$f.png"
}
```

## Files
- `current-state.mmd` — what is actually running right now
- `target-architecture.mmd` — full end-state pipeline (every tool + phase)
- `roadmap.mmd` — the phase order / dependency chain
- `puppeteer-config.json` — `--no-sandbox` flags (used by the Docker fallback)

As each phase completes, update the relevant `.mmd` (flip nodes to the `done`
class) and re-render so the visuals always match reality.
