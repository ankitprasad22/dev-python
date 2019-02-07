from IPython.display import clear_output# this clears the board and presents a new one withought presenting the old one
 
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3]) 
 
 
 
def player_input():
  inpux=''
  while inpux.lower() != 'x' and inpux.lower() !='o':
    inpux=input('player1 select X or O: ')
  
  player1=inpux
  if player1 == 'x':
       player2 ='o'
  else :
    player2 ='x'
    player1 = 'o'
  return (player1,player2)
 
 
def place_marker(board, marker, position):
        board[position]= marker
        return marker
            
def win_check(board, mark):
    return ((board[7]== mark and board[8]== mark and board[9]== mark)or #horizontal win combinations
           (board[4]== mark and board[5]== mark and board[6]== mark)or#horizontal win combinations
           (board[1]== mark and board[2]== mark and board[3]== mark)or#horizontal win combinations
           (board[7]== mark and board[4]== mark and board[1]== mark)or# vertival win combinations
           (board[8]== mark and board[5]== mark and board[2]== mark)or# vertival win combinations
           (board[9]== mark and board[6]== mark and board[3]== mark)or# vertival win combinations
           (board[1]== mark and board[5]== mark and board[9]== mark)or#diagonal win combinations
           (board[3]== mark and board[5]== mark and board[7]== mark))#diagonal win combinations
import random
 
def choose_first():
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'
def space_check(board, position):
    return board[position] ==' '
 
 
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
             return False # return false if the board is NOT fill
    return True # True if its full
 
def player_choice(board):
    pos=0
    while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board,pos):
        pos= int(input('choose your next position: '))
    return pos
 
def replay():
    
    return input('do you want to play again: ').lower().startswith('y')
 
print('Welcome to Tic Tac Toe!')
while True:
    theBoard=[' '] * 10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+'will be the first ')
    play_game=input('are you ready?? yes or no: ')
    if play_game.lower()[0]=='y':
        game_on=True
    else:
        game_on=False
 
    
    # Set the game up here
    
    #pass
    while game_on:
       if turn == 'player1':
            #Player 1 Turn
          display_board(theBoard)
          position=player_choice(theBoard)
          place_marker(theBoard,player1_marker,position)
          if win_check(theBoard,player1_marker):
               display_board(theBoard)
               print('player 1 win the game')
               game_on=False
              
          else:
             if full_board_check(theBoard):
                 display_board(theBoard)
                 print('DRAW')
                 break
             else:
                turn='player2'
               # Player2's turn.
       else:
          display_board(theBoard)
          position=player_choice(theBoard)
          place_marker(theBoard,player2_marker,position)
        
          if win_check(theBoard,player2_marker):
               display_board(theBoard)
               print('player2 wins')
               game_on=False
          else:
             if full_board_check(theBoard):
                display_board(theBoard)
                print('DRAW')
                break
             else:
                turn='player1'
            
        #pass
 
    if not replay():
   
        break