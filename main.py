from random import randint


board =[",","-","-","-","-","-","-","-","-","-"]
available=[]
Combinations=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
def getU_choice():
    ni=input("You Want O or X :")
    lower=ni.lower()
    if(lower=="x"):
        return "x"
    return "o"
COMPUTER=""
USER =getU_choice()
if(USER =="x"):
    COMPUTER="o"
if USER == "o":
    COMPUTER="x"
print(USER,COMPUTER)
def print_board(board):
    for i in range(1,10):
        if(i%3 == 0):
            print(board[i],end="\n")
        else:
            print(board[i],end=" ")

def check_available(num,board):
    if(num == 0):
        print("Thank you")
        exit()
    if(num<10 and num>0):
        if(board[num]==COMPUTER):
            print("COMPUTER OCCUPIED THAT PLACE")
            GetInputs();
        elif(board[num]==USER):
            
            print("YOU ALREADY OCCUPIED THAT PLACE")
            GetInputs()
        else:
            board[num]=USER
    else:
        print("Number must be less than 9 and greater than 0")
        
def check_chance(num,board):
    if "-" in board:
        if((board[num]==COMPUTER)or (board[num]==USER)):
            MakeComputerMove()
            return False
        else:
            board[num]=COMPUTER
            return True
    else:
        print("Match Drawn")
    
def MakeComputerMove(currentPlayer):
    print(currentPlayer ,"computer moved")
    #print_board(board)
    n=randint(1,9)
    check_chance(n,board)
    

def GetInputs(currentPlayer):
    print_board(board)
    print(currentPlayer," is move ")
    choice=int(input("Enter your choice"))
    check_available(choice,board)
def getUserCombinations(board,player):
    for i in range(1,10):
        if(i in available):
            pass
        else:
            if(board[i]==player):
                available.append(i)


def compareWin(avail,base,player):
    for i in base:
        nums=set(i)
        bse=set(avail)
        if nums.issubset(bse) and len(nums)==3:
            print(player," won the game")
            print_board(board)
            exit()
        
    
def check_Combinations(BOARD,current):
    getUserCombinations(board,current)
    if(len(available)>=3):
        current_player=current
        compareWin(available,Combinations,current_player)
    
if __name__ == '__main__':
    currentPlayer=None
    while True:
        print()
        currentPlayer=USER
        GetInputs(currentPlayer)
        check_Combinations(board,currentPlayer)
        currentPlayer=COMPUTER
        MakeComputerMove(currentPlayer)
        check_Combinations(board,currentPlayer)
        
        
        

    