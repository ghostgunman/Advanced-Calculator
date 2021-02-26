import re

print("Calculator")
print("Type quit to exit")

previous=0
run=True

def Maths():
    global run
    global previous
    equation=""
    if previous==0:
        equation = input("Enter Equation:\n")
    else:
        equation=input(str(previous))

    if equation=='quit':
        print("Thanks")
        run=False
    else:
        equation =re.sub('[A-Za-z,.;:()" "]','',equation)

        if previous==0:
            previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)

while run:
    Maths()
