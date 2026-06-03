## U.S. States Game - How it works

This is an **interactive U.S. states geography game** built with Turtle graphics. You guess state names, and the program places them correctly on a blank US map.

### Project files

- `main.py` – the main game script
- `blank_states_img.gif` – blank US map image
- `50_states.csv` – contains state names and their x/y coordinates
- `states_need_to_learn.csv` – created when you exit (lists states you missed)

### What is used

- `turtle` module: for graphics and writing on the map
- `pandas` module: to read and write CSV files
- `screen.textinput()`: to get user input via popup dialog

### How it works

1. **Game starts** – Shows blank US map
2. **Popup asks** – "Enter a state name"
3. **Correct guess** – State name appears on the map at correct location
4. **Counter updates** – Shows progress like `[5/50 is correct]`
5. **Type "Exit"** – Game saves all unguessed states to `states_need_to_learn.csv`
6. **Goal** – Guess all 50 states

### Features

- Interactive popup input box
- Real-time score display
- State names appear exactly at their geographic location
- Saves missed states for later practice

### Controls

| Action | Result |
|--------|--------|
| Type state name | Places state on map (if correct) |
| Type "Exit" | Saves missing states and closes game |

### Data files

**50_states.csv** format:
| state | x | y |
|-------|---|---|
| Alabama | 150 | 200 |
| Alaska | -300 | -100 |
| ... | ... | ... |

**states_need_to_learn.csv** – created on exit:
- Contains only the states you didn't guess

### Example gameplay

```
Popup: [0/50 is correct] Enter a state
User: Texas → Texas appears on map
Popup: [1/50 is correct] Enter a state  
User: California → California appears on map
Popup: [2/50 is correct] Enter a state
User: Exit → Saves remaining 48 states to file
```

### Learning benefit

- Memorize all 50 US states
- Learn their geographic locations
- Practice until you get 50/50

---
