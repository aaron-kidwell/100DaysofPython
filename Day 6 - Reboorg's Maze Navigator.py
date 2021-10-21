#Here I use while loops, functions, and if statements to navigate a robot through a maze, until it finds the goal.

#The following code can be ran here: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#There was no function for the robot to turn right so I made one.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#while loop to search for flag until it's found, carefully navigating through the maze

while not at_goal():
    
    if right_is_clear():
        turn_right()
        move()  
        
    elif front_is_clear():
        move()
    else:
        turn_left()
        