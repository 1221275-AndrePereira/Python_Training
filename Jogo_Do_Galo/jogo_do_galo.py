from random import randrange

def display_board(board):
 print("+-------+-------+-------+")
 for row in board:
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(row[0], row[1], row[2]))
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
 while True:
        try:
            move = int(input("Escolha a casa onde pretende colocar a sua letra: "))
            if move < 1 or move > 9:
                raise ValueError
            for row in range(3):
                for column in range(3):
                    if board[row][column] == move:
                        board[row][column] = "O"
                        return
            print("Essa casa já está ocupada")
            
        except:
            print("Entrada inválida. O número deve ser entre 1 e 9")


def make_list_of_free_fields(board):
 free = []
 for row in range(3):
    for column in range(3):
        if board[row][column] not in ("X", "O"):
            free.append((row, column))
 return free
 


def victory_for(board, sign):
 for row in range(3):
    if all(board[row][column] == sign for column in range(3)):
        return True
        
 for column in range(3):
    if all(board[row][column] == sign for row in range(3)):
        return True
        
 if all(board[i][i] == sign for i in range(3)):
     return True
 if all(board[i][2 - i] == sign for i in range(3)):
     return True
 
 
 return False


def draw_move(board):
 free = make_list_of_free_fields(board)
 if free:
     row, column = free[randrange(len(free))]
     board[row][column] = "X"
 
 
board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9]
]

display_board(board)

while True:
    enter_move(board)
    display_board(board)
    
    if victory_for(board, "O"):
        print("Ganhaste")
        break
    
    if not make_list_of_free_fields(board):
        print("Empate")
        break
    
    draw_move(board)
    display_board(board)
    
    if victory_for(board, "X"):
        print("Perdeste")
        break
    
    if not make_list_of_free_fields(board):
        print("Empate")
        break