# Tic-Tac-Toe AI — Minimax Agent

**CSC 361 — Artificial Intelligence**

student name:سلطان الدريويش

student number:445101292

## Description

An unbeatable Tic-Tac-Toe game where the human plays **O** and the computer plays **X** using the **Minimax** adversarial search algorithm. The agent searches the full game tree to terminal states, so it plays optimally — you can draw against it, but you can never win.

## How It Works

- **Board:** a flat list of 9 integers (`+1` = X, `-1` = O, `0` = empty).
- **Win check:** sums the values on each of the 8 winning lines. `+3` → X wins, `-3` → O wins.
- **Minimax:** two mutually recursive functions, `max` and `min`, explore every possible move. X tries to maximize utility, O tries to minimize it.
- **Utility:** `+100 − depth` for an X win (rewards faster wins), `-100` for a loss, `0` for a draw.

## Files

- `tic-tac-toy.py` — full implementation (UI + game logic + Minimax).

## Requirements

- `customtkinter` → `pip install customtkinter`

## Run

```bash
python tic-tac-toy.py
```

Click any cell to place an O. The AI responds with X after a short delay. Use the reset button to start a new game.
