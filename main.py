# PROFESSIONAL PROJECT: Tic Tac Toe Game

# Import necessary library(ies):
from itertools import permutations
from os import system
from random import choice

############### House Rules #####################
# User is the player identified by marker 'X'.  Computer is the player identified by marker 'O'
# User can elect if s/he wishes to place a mark first or defer to the computer to do so.
# When player or computer scores three of his/her marker in a row, the game ends and that
#   player is declared the winner.
# If game progresses to the point whether neither the user nor the computer can score three marks
#   in a row, the game ends with no winner (draw).
# Additional games can be played until the user elects to exit the application.


# Define lists to store what marks user and computer have made in the present game:
marks = []
boxes_marked = []
boxes_unmarked = []

# Define individual lists (for user and computer) to store what marks each one, respectively, has made:
boxes_marked_computer = []
boxes_marked_user = []

# Define list which stores all possible winning combinations (by box number):
winning_box_combos = ['(1, 2, 3)','(1, 4, 7)','(1, 5, 9)','(2, 5, 8)','(3, 6, 9)','(3, 5, 7)','(4, 5, 6)','(7, 8, 9)']


# DEFINE FUNCTIONS TO BE USED FOR THIS APPLICATION (LISTED IN ALPHABETICAL ORDER BY FUNCTION NAME):
def check_winner_status():
    """Function which checks if either a winner can be declared or a draw has been reached"""
    # Define variable for flagging the winner status:
    winner = ""

    # Check if user has won:
    list_combos = []
    if len(boxes_marked_user) >= 3:  # There must be a minimum of 3 marks made by this player before a win is possible.
        # Identify and store current combinations (using box numbers) player currently has scored:
        for comb in permutations(boxes_marked_user, 3):
            list_combos.append(''.join(str(comb)))
        winning_combo = ""

        # Check if any of the current combinations matches one of the possible winning combinations:
        for item in list_combos:
            if item in winning_box_combos:
                winning_combo += item
            if winning_combo != "":  # User has won the game.
                winner = "User"
                break

    # Check if computer has won:
    list_combos = []
    if len(boxes_marked_computer) >= 3:  # There must be a minimum of 3 marks made by this player before a win is possible.
        # Identify and store current combinations (using box numbers) player currently has scored:
        for comb in permutations(boxes_marked_computer, 3):
            list_combos.append(''.join(str(comb)))
        winning_combo = ""

        # Check if any of the current combinations matches one of the possible winning combinations:
        for item in list_combos:
            if item in winning_box_combos:
                winning_combo += item
            if winning_combo != "":  # Computer has won the game.
                winner = "Computer"
                break

    # Check if all boxes on the board have been marked without a winner:
    if winner == "":  # Neither player has won the game.
        if len(boxes_marked) == 9:  # No boxes remain available for marking.  Therefore, game has reached a draw.
            winner = "draw"

    # Return the winning status to the calling function:
    return winner


def play_game():
    """Main function which controls game-playing and feedback"""
    global marks

    # Define variable to determine whether game should continue to be played (used in 'while' loop below):
    continue_with_game = True

    # Proceed with game play until user elects to exit the application:
    while continue_with_game:
        # Initialize the 'player_choice' variable:
        player_choice = ""

        # Clear the screen:
        # NOTE: PyCharm displays the output of your running module using the output console.
        #       In order for your terminal commands under os.system() to work,
        #       you need to emulate your terminal inside the output console as follows:
        #
        #       1. Select 'Edit Configurations' from the 'Run' menu.
        #       2. Under the 'Execution' section, select 'Emulate terminal in output console'
        system('cls')

        # Greet the user:
        print("WELCOME TO MY TIC TAC TOE GAME!")

        # Define variable to determine whether user has made a valid choice re: who marks first (or exit the game):
        player_choice_valid = False

        # Proceed with prompting user to choose which player marks first (or if user wished to exit the game).
        # Loop until a valid choice has been made:
        while not player_choice_valid:
            # Ask user to choose which player (user or computer) should place a mark first (or if user wishes to exit the game):
            player_choice = input(
                f"Do you wish to place your mark first, or do you wish to defer to the\nother player (computer) to do so?\nEnter 'U' for you or 'C' for computer.\nAlternatively, enter -BYE to exit the game.: ")

            if player_choice.lower() == '-bye':  # User has elected to exit the game.
                print("Thank you for using this application. Goodbye!")
                player_choice_valid = True
                exit()

            else:  # User has not elected to exit the game.
                if not (player_choice.lower() == 'u' or player_choice.lower() == 'c'):  # User has made an invalid choice.
                    # Clear the screen:
                    system('cls')
                    # Inform user of invalid choice.  Application will loop back and re-prompt user to make a valid choice:
                    print("Invalid choice.")
                else:  # User has made a valid choice:
                    player_choice_valid = True

        # At this point, user has elected to proceed with the game and has chosen who marks first.

        # Reset mark lists to beginning-of-game state:
        reset_mark_lists()

        # Define variable to track how many marks have been placed by user and computer combined"
        counter = 0

        # Set the 'counter' variable according to whether user has elected to play first or defer to the computer to play first:
        if player_choice.lower() == 'u':  # User has elected to play first.
            counter = 0
        else:  # User has elected to defer to computer to play first.
            counter = 1

        # Set initial value of the 'invalid_choice' variable:
        invalid_choice = "TIME FOR YOU TO PLAY!"

        # Continue to play the game until a winner is declared.
        while counter >= 0:
            # Clear the screen:
            system('cls')

            # Set initial value of the 'invalid_choice'
            invalid_choice = "TIME FOR YOU TO PLAY!"

            # Depending on the value of the 'counter' variable, user or computer marks next
            # (If 'counter' is an even number, user marks next.  If 'counter' is an odd number,
            # computer marks next.):
            if counter % 2 == 0: # User plays.
                # Prompt user for a box to mark until user selects an unmarked box:
                while invalid_choice != "BOX MARKED SUCCESSFULLY!":
                    # Update the game board to reflect marks made so far.
                    update_board(None, "")

                    # Prompt user to pick a box to mark.  Inform user of unmarked boxes (identified by number) available to pick from:
                    box = int(input(
                        f"\n{invalid_choice}\nEnter a number corresponding to the box in which you wish to make your mark. Available boxes = {boxes_unmarked}: "))

                    # Proceed depending on whether user has made a valid box selection:
                    if box == "" or not (box - 1 >= 0 and box - 1 <= 8):  # User has made an invalid choice.
                        invalid_choice = "INVALID CHOICE."
                    else:  # User has selected one of the 9 boxes on the total board.
                        # Check if selected box is already marked:
                        if marks[box - 1] == " X " or marks[box - 1] == " O ":  # Selected box is already marked.
                            invalid_choice = f"BOX '{box}' IS ALREADY MARKED."
                        else:  # Selected box is not marked.  Therefore, user successfully claims this box.
                            # Update 'marks' list to indicate an "X" for the selected box:
                            marks[box - 1] = " X "

                            # Update the 'invalid_choice' variable to indicate successful box selection.
                            # This will end the immediate 'while' loop:
                            invalid_choice = "BOX MARKED SUCCESSFULLY!"

                            # Update the lists tracking which boxes are marked vs. which boxes are unmarked:
                            update_box_lists(box, 0)

            else:  # Computer plays.
                # Make a random choice from the list of unmarked boxes:
                box = choice(boxes_unmarked)

                # Update 'marks' list to indicate an "O" for the selected box:
                marks[box - 1] = " O "

                # Update the lists tracking which boxes are marked vs. which boxes are unmarked:
                update_box_lists(box, 1)

            # Check if either a winner can be declared or a draw has been reached:
            winner_status = check_winner_status()
            if winner_status == "":  # Game has not ended.
                # Increment the 'counter' variable by 1 to pass control to the next player:
                counter += 1
            else:
                # Clear the screen:
                system('cls')

                # Show the final board.  If either user or computer has won, show only the winning combo on the board:
                update_board(None, winner_status)
                if winner_status == "User":  # User has won the game.
                    print("YOU HAVE WON! CONGRATULATIONS!")
                elif winner_status == "Computer":  # Computer has won the game.
                    print("YOU HAVE LOST TO THE COMPUTER.")
                elif winner_status == "draw":  # Game has reached a draw.
                    print("GAME IS A DRAW. NO WINNER.")

                # Set counter to -1, thus ending the immediate 'while' loop:
                counter = -1

        # Ask user if s/he wishes to play another game.  Any response outside of 'n' = play another game:
        if input("Do you wish to play another game? Enter Y or N: ").lower() == 'n':
            print("Thank you for playing this game. Goodbye!")

            # Update variable to indicate that user does not wish to play another game (thus, ending the immediate 'while' loop):
            continue_with_game = False


def reset_mark_lists():
    """Function which resets the mark lists to beginning-of-game state"""
    global marks, boxes_marked, boxes_unmarked, boxes_marked_computer, boxes_marked_user

    # Reset mark lists to beginning-of-game state:
    marks = [' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ']
    boxes_marked = []
    boxes_unmarked = [1,2,3,4,5,6,7,8,9]
    boxes_marked_computer = []
    boxes_marked_user = []


def update_board(box, winner):
    """Function which draws the game board and reflects marks made so far for each player. If a winner has been declared, the board shows just the winning combination of marks."""

    # If either user or computer has won the game, show the final board with the winning combo:
    if winner == "User" or winner == "Computer":
        if winner == "User":
            boxes_marked_by_player = boxes_marked_user
            marker = "X"
        elif winner == "Computer":
            boxes_marked_by_player = boxes_marked_computer
            marker = "O"

        list_combos = []
        # Identify and store current combinations winner has scored:
        for comb in permutations(boxes_marked_by_player, 3):
            list_combos.append(''.join(str(comb)))
        winning_combo = ""

        # Check if any of the current combinations matches one of the possible winning combinations:
        for item in list_combos:
            if item in winning_box_combos:
                winning_combo += item
                print(f"Winning combination: {winning_combo}")

        # Update and display the final board, showing the winning player's winning combo:
        # Print title and top border of board:
        print("\nFINAL BOARD:")
        print(" ___ ___ ___")

        # Prepare the main body of the final board:
        contents_row_1 = "|   |   |   |"
        contents_row_2 = "|   |   |   |"
        contents_row_3 = "|   |   |   |"
        for i in winning_combo:
            # Calculate the box (by row and position) in which to display the winning player's marker:
            position_list = [2,6,10]
            if i != "(" and i != ")" and i != " " and i != ",":
                if int(i) >= 1 and int(i) <= 3:  # Row 1
                    position = (position_list[int(i)-1])
                    contents_row_1 = contents_row_1[:position] + marker + contents_row_1[position + 1:]
                elif int(i) >= 4 and int(i) <= 6:  # Row 2
                    position = (position_list[int(i)-1-3])
                    contents_row_2 = contents_row_2[:position] + marker + contents_row_2[position + 1:]
                elif int(i) >= 7 and int(i) <= 9:  # Row 3
                    position = (position_list[int(i)-1-6])
                    contents_row_3 = contents_row_3[:position] + marker + contents_row_3[position + 1:]

        # Print the main body of the final board:
        print(contents_row_1)
        print(" --- --- ---")
        print(contents_row_2)
        print(" --- --- ---")
        print(contents_row_3)

        # Print bottom border of board:
        print(" --- --- ---")

    else:  # Neither user nor computer has won the game.
        # Update and display the current game's board:
        # Print title and top border of board:
        if winner == "":
            print("\nCURRENT BOARD:")
        elif winner == "draw":
            print("\nFINAL BOARD:")
        print(" ___ ___ ___")

        # Print marks currently made:
        for i in range(0, 9, 3):
            print(f"|{marks[i]}|{marks[i+1]}|{marks[i+2]}|")
            print(" --- --- ---")


def update_box_lists(box, player):
    """Function which updates the lists tracking which boxes are marked vs. which boxes are unmarked"""
    # Update the 'boxes_unmarked' list to remove the box just marked by the current player:
    boxes_unmarked.remove(box)

    # Update the 'boxes_marked' list to add the box just marked by the current player:
    boxes_marked.append(box)

    # Re-sort the 'boxes_marked' list to show the marked boxes in numerical order:
    boxes_marked.sort()

    # Update the player-specific 'boxed_marked' list to add the box just marked by the current player:
    if player == 0:  # User is the current player.
        # Update the 'boxes_marked_user' list to add the box just marked by user:
        boxes_marked_user.append(box)

        # Re-sort the 'boxes_marked_user' list to store the user's marked boxes in numerical order:
        boxes_marked_user.sort()

    elif player == 1:  # Computer is the current player.
        # Update the 'boxes_marked_computer' list to add the box just marked by computer:
        boxes_marked_computer.append(box)

        # Re-sort the 'boxes_marked_computer' list to store the computer's marked boxes in numerical order:
        boxes_marked_computer.sort()


# Run the main application for the game:
play_game()