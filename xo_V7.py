import sys
import time

#Initial board set up


list0 = [" "," "," "]
list1 = [" "," "," "]
list2 = [" "," "," "]



def draw_grid():

    print()

    for i in range(0,3):
        print(list0[i],end="")
        
        if (i!=2):
            print("|",end="")
            
    print()
    print("-----")

    for i in range(0,3):
        print(list1[i],end="")
        
        if (i!=2):
            print("|",end="")
            
    print()
    print("-----")

    for i in range(0,3):
        print(list2[i],end="")
        
        if (i!=2):
            print("|",end="")
            
    print()
    print()



def input_p1():

    print("Player 1 input X position")

    while True:
        
        while True:
            try:
                row1 = int(input("Row position (0-2):"))
                if row1 not in [0, 1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid integer. Please try again.")

        while True:
            try:
                col1 = int(input("Column position (0-2):"))
                if col1 not in [0, 1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid integer. Please try again.")

        if row1 == 0:
            if list0[col1] == " ":
                break
            else:
                print("Invalid - select an empty position")

        if row1 == 1:
            if list1[col1] == " ":
                break
            else:
                print("Invalid - select an empty position")

        if row1 == 2:
            if list2[col1] == " ":
                break
            else:
                print("Invalid - select an empty position")   
            
    return row1,col1



def input_p2():
    
    print("Player 2 input O position")

    while True:
        
        while True:
            try:
                row2 = int(input("Row position (0-2):"))
                if row2 not in [0, 1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid integer. Please try again.")

        while True:
            try:
                col2 = int(input("Column position (0-2):"))
                if col2 not in [0, 1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid integer. Please try again.")

        if row2 == 0:
                if list0[col2] == " ":
                    break
                else:
                    print("Invalid - select an empty position")

        if row2 == 1:
                if list1[col2] == " ":
                    break
                else:
                    print("Invalid - select an empty position")

        if row2 == 2:
                if list2[col2] == " ":
                    break
                else:
                    print("Invalid - select an empty position")

    return row2,col2



def update_grid1():
    if row1 == 0:
        list0[col1] = "X"
    elif row1 == 1:
        list1[col1] = "X"
    elif row1 == 2:
        list2[col1] = "X"



def update_grid2():
    if row2 == 0:
        list0[col2] = "O"
    elif row2 == 1:
        list1[col2] = "O"
    elif row2 == 2:
        list2[col2] = "O"



def check_draw():
    if " " not in list0 and " " not in list1 and " " not in list2:
        print()
        print("It is a DRAW")
        print()
        time.sleep(60)
        sys.exit()



def check_win1():

    if list0 == ["X","X","X"] or list1 == ["X","X","X"] or list2 == ["X","X","X"] :
        print()
        print("PLAYER 1 WINS")
        print()
        time.sleep(60)
        sys.exit()

    if list0[0] == "X" and list1[0] == "X" and list2[0] == "X" :
        print()
        print("PLAYER 1 WINS")
        print()
        time.sleep(60)
        sys.exit()

    if list0[1] == "X" and list1[1] == "X" and list2[1] == "X" :
        print()
        print("PLAYER 1 WINS")
        print()
        time.sleep(60)
        sys.exit()

    if list0[2] == "X" and list1[2] == "X" and list2[2] == "X" :
        print()
        print("PLAYER 1 WINS")
        print()
        time.sleep(60)
        sys.exit()

    if list0[0] == "X" and list1[1] == "X" and list2[2] == "X" :
        print()
        print("PLAYER 1 WINS")
        print()
        time.sleep(60)
        sys.exit()

    if list0[2] == "X" and list1[1] == "X" and list2[0] == "X" :
        print()
        print("PLAYER 1 WINS")
        print()
        time.sleep(60)
        sys.exit()



def check_win2():

    if list0 == ["O","O","O"] or list1 == ["O","O","O"] or list2 == ["O","O","O"] :
        print()
        print("PLAYER 2 WINS")
        print()
        time.sleep(60)
        sys.exit()

    if list0[0] == "O" and list1[0] == "O" and list2[0] == "O" :
        print()
        print("PLAYER 2 WINS")
        print()
        time.sleep(60)
        sys.exit()

    if list0[1] == "O" and list1[1] == "O" and list2[1] == "O" :
        print()
        print("PLAYER 2 WINS")
        print()
        time.sleep(60)
        sys.exit()

    if list0[2] == "O" and list1[2] == "O" and list2[2] == "O" :
        print()
        print("PLAYER 2 WINS")
        print()
        time.sleep(60)
        sys.exit()

    if list0[0] == "O" and list1[1] == "O" and list2[2] == "O" :
        print()
        print("PLAYER 2 WINS")
        print()
        time.sleep(60)
        sys.exit()

    if list0[2] == "O" and list1[1] == "O" and list2[0] == "O" :
        print()
        print("PLAYER 2 WINS")
        print()
        time.sleep(60)
        sys.exit()

for i in range(0,5):

    draw_grid()
    
    row1,col1 = input_p1()
    update_grid1()
    draw_grid()

    check_win1()
    check_draw()

    print()

    row2,col2 = input_p2()
    update_grid2()
    check_win2()

    print()
