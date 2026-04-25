'''
DEVELOPER(S): Simon Monagas
COLLABORATORS: 
DATE: 4/24
'''

"""
Golf scorecard tracker which takes input for scoes and then formats it nicely so you can see scores at end. I limited it to 3 holes just for demonstration

Confused of where to explain why I used list over dictionary but I used a list over a dictionary because with a scorecard the values and the amount of values is constantly changing so a list would be ideal so I can change the values much easier than using a dicitonary. 

Leave one blank line.  The rest of this docstring should contain an
overall description of the program.
"""

##########################################
# IMPORTS:
# <list of modules needed for the program and their purpose>
##########################################
# <replace this line with import statement(s)>
INPUT_FILE = "input_file.txt"


##########################################
# FUNCTIONS:
##########################################
# <replace this line with function definitions, each needs a description>
def write_scorecard(x):
    file = open(INPUT_FILE, "w")
    for y in x:
        file.write(str(y) + " ")
    file.close()

def show_scorecard():
    print("===== SCORECARD =====")
    hole = 1
    file = open(INPUT_FILE, "r")
    s = file.read()
    z = s.split()
    for i in z:
        y = int(i)
        print(f"Hole {hole}: {y} strokes")
        hole = hole + 1
    file.close()


##########################################
# MAIN PROGRAM:
##########################################


scores = []
print("I will keep your scores for you")
hole1 = input("How many strokes did you do on hole 1: ")
scores.append(int(hole1))
hole2 = input("How many strokes did you do on hole 2: ")
scores.append(int(hole2))
hole3 = input("How many strokes did you do on hole 3: ")
scores.append(int(hole3))
write_scorecard(scores)
show_scorecard()