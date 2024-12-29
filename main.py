import turtle
import pandas

image = "blank_states_img.gif"


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

# working wth data
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()


'''to find the coordinate of particular point on the screen we use following concept'''
# def get_click_coordinate(x, y):
#     print(x, y)
# turtle.onscreenclick(get_click_coordinate)
# turtle.mainloop()

guess_state = []

while len(guess_state) < 50:

    answer_state = screen.textinput(title=f"{len(guess_state)}/50 State Correct",
                                    prompt="what's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_state:
                missing_states.append(state)
        new_data = pandas.DataFrame()
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(x=int(state_data["x"]), y=int(state_data.y))
        t.write(answer_state)


screen.exitonclick()
