import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
states_list = states_data.state.to_list()
n_states = 0

t = turtle.Turtle()
t.hideturtle()
t.penup()

while n_states < 50:
    answer_state = screen.textinput(title=f"{n_states}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        n_states += 1
        states_list.remove(answer_state.title())
        x_coordinate = int(states_data[states_data.state == answer_state].x)
        y_coordinate = int(states_data[states_data.state == answer_state].y)
        t.goto(x_coordinate, y_coordinate)
        t.write(answer_state)

states_to_learn = {'states': states_list}
states_to_learn_dt = pd.DataFrame(states_to_learn)
states_to_learn_dt.to_csv('States_to_learn.csv')
