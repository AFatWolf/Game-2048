import random

def draw_border():
    string = ""
    for i in range(0,4):
        string += "+-----"
    string += '+'
    print string

def draw_empty_line():
    empty = ""
    for i in range(0,4):
        empty += "|     "
    empty += '|'
    print empty

def draw_number(numberList):
    strToPrint = ""
    if(len(numberList) != 4):
        print "Error: Do not have enough elements!"
    else:
        for i in range(0,len(numberList)):
            number = str(numberList[i])
            # to create, eg, "| 1024" or "|  2  "
            length = len(number)
            secondSpace = (5 - len(number)) / 2
            firstSpace = 5 - len(number) - secondSpace
            strToPrint +=  '|' + ' ' * firstSpace + str(numberList[i]) + ' ' * secondSpace
        strToPrint += '|'
        print strToPrint

# listOfNumberList : a list of the number lists a.k.a. the table
def draw_the_table(listOfNumberList): 
    for i in range(0,len(listOfNumberList)):
        draw_border()
        draw_empty_line()
        draw_number(listOfNumberList[i])
        draw_empty_line()
    draw_border()

# return false if the table is not full, 
def check_full_table(listOfNumberList):
    for i in range(0,4):
        for j in range(0,4):
            if listOfNumberList[i][j] == 0:
                return False
    return True

# generate a new value in the cell
def generate_random_cell(listOfNumberList):
    cellValues = [2,2,2,4]                
    # generate random position in table
    iOfRandomCell = random.randint(0,3)
    jOfRandomCell = random.randint(0,3)
    while(listOfNumberList[iOfRandomCell][jOfRandomCell] != 0):
        iOfRandomCell = random.randint(0,3)
        jOfRandomCell = random.randint(0,3)
    # geenerate the cell's value
    randomCellValue = cellValues[random.randint(0,3)]
    listOfNumberList[iOfRandomCell][jOfRandomCell] = randomCellValue

# initialize the table to 0
def init_table():
    t = []
    for i in range(0,4):
        t.append([0,0,0,0])
    return t

#print out the rules
def rules():
    print "The rules are simple:"
    print "You have a 4x4 table."
    print "Each turn the table creates either 2 or 4 out of the blue then puts it in a random cell"
    print "You can move the whole table up, down, right, left ny using keys 'u', 'd', 'r', 'l' respectively."
    print "Your mission is to create the number 2048."
    print "Good luck!"

# promt user to enter movement key
def game_play():
    global table
    # enter next move
    movement = raw_input("Enter nex move:")
    while movement != 'u' and movement != 'd' and movement != 'l' and movement != 'r':
        movement = raw_input("Invalid move. Enter next move:")
    # update the table
    table = update_table(table, movement)

# how will we apply movement?
# Eg we have a row like [0,4,4,2] and a 'l' command
# we create a list, then push each element from the row which is diff from 0
# First ele: []
# Second ele: [4]
# Third ele: [4,4] -> [8]
# Fourth ele: [8,2]
# Then replace the real one with this
def update_table(table, movement):
    t = init_table()
    wayToMove = []
    direction = 0
    if movement == 'u' or movement == 'l':
        wayToMove = range(0,4,1)
        direction = 1
    elif movement == 'd' or movement == 'r':
        wayToMove = range(3,-1,-1)
        direction = -1
    for other in range(0,4):
        rc = []
        for i in wayToMove:
            if (movement == 'u' or movement == 'd') and table[i][other] != 0:
                # jump to where i != 0
                rc.append(table[i][other])
                # if there is already another element
                if len(rc) > 1:
                    # if latest element is equal, replace it with the sum
                    if rc[-1] == rc[-2]:
                        s = rc.pop()
                        s += rc.pop()
                        rc.append(s)
            elif (movement == 'l' or movement == 'r') and table[other][i] != 0:
                rc.append(table[other][i])
                # if there is already another element
                if len(rc) > 1:
                    # if latest element is equal, replace it with the sum
                    if rc[-1] == rc[-2]:
                        s = rc.pop()
                        s += rc.pop()
                        rc.append(s)
        # fill full row/column
        while len(rc) < 4:
            rc.append(0)
        if movement == 'u':
            for i in range(0,4):
                # replace the value in the table
                t[i][other] = rc[i]
        elif movement == 'd':
            for i in range(3,-1,-1):
                t[i][other] = rc[3-i]
        elif movement == 'r':
            for i in range(3,-1,-1):
                t[other][i] = rc[3-i]
        else:
            t[other] = rc
    return t

def win_condition(table):
    for i in range(0,4):
        for j in range(0,4):
            if table[i][j] == 2048:
                return True
    return False
############                        
# MAIN GAME#
############
rules()
table = init_table()
while check_full_table(table) == False and win_condition(table) == False:
    print "Current state:"
    generate_random_cell(table)
    draw_the_table(table)
    game_play()
if win_condition(table) == True:
    print "cONGRATULATIONS! YOU WIN!"
else:
    print "GAME OVER!"
