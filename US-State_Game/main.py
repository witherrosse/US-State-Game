import turtle
import pandas as pd

### Setup the game screen with US map image ###

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

### Load state data from CSV file ###

data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()   # List of all 50 state names

### Track states that user has guessed correctly ###

guessed_list = []

### Main game loop - continue until all 50 states are guessed ###

while len(guessed_list) < 51:

    ### Ask user to enter a state name ###

    answer_state = screen.textinput(f"[{len(guessed_list)}/50 is correct]", "Enter a state").title()

    ### Exit the game and save missing states to learn later ###

    if answer_state == "Exit":

        missing_state = [state for state in all_state if state not in guessed_list]
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_need_to_learn.csv")   # Save unguessed states
        break

    ### Check if the answer is a correct state ###

    if answer_state in all_state:

        guessed_list.append(answer_state)

        ### Create turtle to write state name on map ###

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())   # Move to state's coordinates
        t.write(answer_state, font=("Arial", 10, "bold"))   # Write state name on map