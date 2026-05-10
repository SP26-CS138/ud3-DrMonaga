'''
DEVELOPER(S): Simon Monagas
COLLABORATORS: 
DATE: 4/24
'''

"""
Golf scorecard tracker which takes input for scoes and then formats it nicely so you can see scores at end. I limited it to 3 holes just for demonstration

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
def write_scorecard(scores):
    '''Writes the list of golf scores stored in the list thats passed through into a text file.'''
    file = open(INPUT_FILE, "w")
    for score in scores:
        file.write(str(score) + " ")
    file.close()

def show_scorecard():
    '''Reads file and puts all the stored scores into a list. Then prints out the hole number and its assosiated score'''
    print("===== SCORECARD =====")
    hole = 1
    file = open(INPUT_FILE, "r")
    scores = file.read()
    split_scores = scores.split()
    for hole_number in split_scores:
        print(f"Hole {hole}: {hole_number} strokes")
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