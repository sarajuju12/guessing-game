import turtle
import pandas

points = 0
win = turtle.Turtle()
win_font = ("Arial", 24, "bold")
state_font = ("Arial", 8, "normal")
alignment = "center"

screen = turtle.Screen()
screen.title("Name the U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

game_end = False
while not game_end:

    answer_state = screen.textinput(title=f"{points}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        points += 1
        state_data = data[data.state == answer_state]
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(float(state_data.x), float(state_data.y))
        state_turtle.write(arg=answer_state, align=alignment, font=state_font)
        guessed_states.append(answer_state)

    if points == 50:
        win.penup()
        win.hideturtle()
        win.write(arg="YOU WIN!", align=alignment, font=win_font)
        game_end = True


















