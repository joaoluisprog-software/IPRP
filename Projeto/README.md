# Liga dos Últimos — Foosball Game

A two-player foosball simulator built with Python's `turtle` module, developed for the IPRP course (2023/2024).

## How to play

```bash
python foosball_alunos.py
```

| Player | Move Up | Move Down | Move Left | Move Right |
|--------|---------|-----------|-----------|------------|
| Red (A) | `W` | `S` | `A` | `D` |
| Blue (B) | `↑` | `↓` | `←` | `→` |

Press **ESC** to end the game.

## Rules

- Move your player to hit the ball into the opponent's goal.
- The ball bounces off the top and bottom walls and off the sides outside the goal area.
- A goal is scored when the ball enters the opponent's goal zone.
- The ball resets to the center after every goal.

## Files

| File | Description |
|------|-------------|
| `foosball_alunos.py` | Main game logic |
| `var_alunos.py` | VAR replay viewer |
| `histórico_resultados.csv` | Running history of all game results |
| `replay_golo_jv_*_ja_*.txt` | Per-goal replay files (auto-generated) |

## VAR Replay

Every goal generates a replay file named `replay_golo_jv_[red]_ja_[blue].txt` containing the full trajectory of the ball and both players up to the moment of the goal.

To watch a replay:

```bash
python var_alunos.py
```

Update the filename in `var_alunos.py → main()` to the replay you want to view.

## Game history

Each time the game ends (ESC), the result is appended to `histórico_resultados.csv`:

```
NJogo,JogadorVermelho,JogadorAzul
1,3,2
2,0,1
```

## Requirements

- Python 3
- `turtle` module (included in the standard library)
