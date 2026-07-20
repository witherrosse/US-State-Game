import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()   



guessed_list = []



while len(guessed_list) < 51:

    

    answer_state = screen.textinput(f"[{len(guessed_list)}/50 is correct]", "Enter a state").title()

    ### Exit the game and save missing states to learn later ###

    if answer_state == "Exit":

        missing_state = [state for state in all_state if state not in guessed_list]
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_need_to_learn.csv")   
        break

   

    if answer_state in all_state:

        guessed_list.append(answer_state)

       

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())  
        t.write(answer_state, font=("Arial", 10, "bold"))   
