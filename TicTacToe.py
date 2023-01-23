import sys

board = [' ' for x in range(10)]
space = set()
full = set()

for i in range(1,10):
        full.add(i)

def insertLetter(pos, le):
    board[pos] = le

def printboard(board):
    print(board[1] + "  | " + board[2] + " | " + board[3])
    print("===========")
    print(board[4] + "  | " + board[5] + " | " + board[6])
    print("===========")
    print(board[7] + "  | " + board[8] + " | " + board[9])

def isWinner(bo,le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le)
    or (bo[4] == le and bo[5] == le and bo[6] == le)
    or (bo[7] == le and bo[8] == le and bo[9] == le)
    or (bo[1] == le and bo[4] == le and bo[7] == le)
    or (bo[2] == le and bo[5] == le and bo[8] == le)
    or (bo[3] == le and bo[6] == le and bo[9] == le)
    or (bo[1] == le and bo[5] == le and bo[9] == le)
    or (bo[3] == le and bo[5] == le and bo[7] == le)
    )

def playerMove():
    flag  = True
    while flag:
        if not isWinner(board, 'O'):
            print("\nYour Turn")
            user_input = int(input("Enter the number between 1-9: "))
            print("\nPlayer X's turn. Human Player")
            while not user_input in range(1,10):
                user_input = int(input("Please enter a valid no. between 1-9: "))
            
            if not isSpaceboard(user_input):
                space.add(user_input)
                insertLetter(user_input, 'X')
                printboard(board)
                flag = False
        else:
            print("Computer Wins")
            sys.exit()        
               

def compMove():
    import random
    flag  = True
    while flag:
        if not isWinner(board, 'X'):
            comp_input = random.randint(1,9)
            while isSpaceboard(comp_input):
                comp_input = random.randint(1,9)

            # if not isSpaceboard(comp_input):
            space.add(comp_input)
            insertLetter(comp_input, 'O')
            print("Player O's turn. Computer Player")
            printboard(board)
            flag = False

        else:
            print("You Win")
            sys.exit()
                       


def isFullboard():
    rem = full.difference(space)
    if len(rem) == 0:
        print("The board is full. It's a TIE.")
        sys.exit()
        
        return True
    else:
        return False
    

def isSpaceboard(move):
    if not isFullboard():
         if move in space:
            # print("The space is occupied. Choose another space")
            return True
         else:
            return False
    else:
        return False             
    

def main():
    flag = True
    while flag:
        while not isFullboard():
            playerMove()
            print("\n\n")
            compMove()
        flag = False  

main()