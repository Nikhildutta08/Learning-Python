#################################################################################
#######################GLOBAL VARAIBLES TO BE DEFINED HERE#######################
#################################################################################
#Program for tic tac toe game
replay=True

#Defining the list for test board
game_board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
rules_game_board=['#','1','2','3','4','5','6','7','8','9']

##################################################################################
#######################FUNCTION DEFINITION START FROM HERE########################
##################################################################################
#function to display the board
def display_board(board):
    print('   |   |')
    print(' '+ board[1] +' | '+ board[2] +' | '+board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[4] +' | '+ board[5] +' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[7] +' | '+ board[8] +' | '+board[9])
    print('   |   |')
#End of display the board function
    
#Define Player input
def player_marker():
    marker=''

    while marker not in ('X','O'):
        marker=input("\nPlayer 1: You want to be X or O?").upper()
        if marker not in ('X','O'):
            print("oops!! wrong input, enter again")

    if marker=='X':
        return 'X'
    elif marker=='O':
        return 'O'
#End of taking player input

#place marker:Defining on which place player want their mark
def place_marker(playerid):
    place=''

    while place not in range(1,10):
        value = input(f"\n[{playerid}]Enter the index position between 1-9:")
        if value.isdigit():
            place = int(value)

        if place not in range(1,10):
            print("oops!! enter index position in numeric 1-9 only")

    if game_board[place]==' ':
        game_board[place]=playerid
        return game_board
    else:
        print("This place is already taken, Try again")
        place_marker(playerid)
    
#End of place marker function

#Start of check winner function
def check_winner():
    if (game_board[1]+game_board[2]+game_board[3]=='XXX') or (game_board[1]+game_board[2]+game_board[3]=='OOO'):
        return 1
    elif (game_board[4]+game_board[5]+game_board[6]=='XXX') or (game_board[4]+game_board[5]+game_board[6]=='OOO'):
        return 1
    elif (game_board[7]+game_board[8]+game_board[9]=='XXX') or (game_board[7]+game_board[8]+game_board[9]=='OOO'):
        return 1
    elif (game_board[1]+game_board[4]+game_board[7]=='XXX') or (game_board[1]+game_board[4]+game_board[7]=='OOO'):
        return 1
    elif (game_board[2]+game_board[5]+game_board[8]=='XXX') or (game_board[2]+game_board[5]+game_board[8]=='OOO'):
        return 1
    elif (game_board[3]+game_board[6]+game_board[9]=='XXX') or (game_board[3]+game_board[6]+game_board[9]=='OOO'):
        return 1
    elif (game_board[1]+game_board[5]+game_board[9]=='XXX') or (game_board[1]+game_board[5]+game_board[9]=='OOO'):
        return 1
    elif (game_board[3]+game_board[5]+game_board[7]=='XXX') or (game_board[3]+game_board[5]+game_board[7]=='OOO'):
        return 1
    else:
        return 0
#End of check winner function

#This is the main function from where all the function is getting called
def playgame():
    ###Execution start from here###
    print("\n!!!Welcome to TIC_TAC_TOE!!!\n")
    #Displaying the rules board
    display_board(rules_game_board)
    #Explaining the rules
    print("\nGame Rules:")
    print("\n1. Player need to choose if they want to be player X or player O.")
    print("\n2. Player need to select the position where they want their mark.")
    print("\n3. Player 1 shall always get the first chance to enter their mark.")
    print("\n4. First player to complete 3 mark in straight line wins!!!")

    #Assignment of players
    player1=player_marker()
    if player1=='X':
        player2='O'
        print(f"\nPlayer 1 is assigned the letter {player1}")
        print(f"Player 2 is assigned the letter {player2}\n")
    elif player1=='O':
        player2='X'
        print(f"\nPlayer 1 is assigned the letter {player1}")
        print(f"Player 2 is assigned the letter {player2}\n")

    #Running place marker
    count=1
    for count in range(1,11):
        if count in (1,3,5,7,9):
            place_marker(player1)
            display_board(game_board)
            winner=check_winner()
            if winner==1:
                print("\nCongatulations!! Player 1 won the game!!")
                break
        elif count in (2,4,6,8):
            place_marker(player2)
            display_board(game_board)
            winner=check_winner()
            if winner==1:
                print("\nCongratulations!! Player 2 won the game!!")
                break
        elif count==10:
            print("\noops!!! no players won the game!!!")
#End of main function

##################################################################################
#######################FUNCTION DEFINITION ENDS HERE##############################
##################################################################################

##################################################################################
#######################PROGRAMME MAIN BODY START HERE#############################
##################################################################################
if __name__=='__main__': #statement for code organisation. whenever .py script is run directly the built in variable __name__ is assigned '__main__'
    while replay==True:
        playgame()
        ans=''
        while ans.upper() not in ('Y','N'):
            ans=input("\nEnter (Y/N) to play again:")
        if ans.upper()=='Y':
            for position in range(1,10):
                game_board[position]=' '
            continue
        else:
            print("\n!!!Thank you for playing the game!!!")
            break

##################################################################################
#######################PROGRAMME MAIN BODY ENDS HERE##############################
##################################################################################