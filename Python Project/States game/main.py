import turtle
import pandas

screen  = turtle.Screen()
screen.title("U.S. state Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# --------- get coordinates on map ---------
# def get_mouse_click_coor(x,y):
# 	print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
#---------------------------------------------
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
	answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct ",prompt="what's another state name").title()
	if answer_state == "Exit":
		missing_states= [state for state in all_states if state not in guessed_states]
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("states to learn.csv")
		break
	if answer_state in all_states:
		guessed_states.append(answer_state)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = data[data.state == answer_state]
		t.goto(int(state_data.x),int(state_data.y))
		t.write(state_data.state.item()) #item()  grabs the first element
		#  or   t.write(answer_state)

