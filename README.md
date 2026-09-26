# tagless snake

A classic Snake game rendered entirely on an HTML canvas, built with Python (Brython)

## Play

Arrow keys or WASD to move. Eat read circles to grow. Press R to restart.

## How it works

The entire UI is drawn on a canvas via `document.createElement`, no `<div></div>` tags, just shapes and pixels. 

## Run locally

```bash
python -m http.server
```

Then open `localhost:8080`
