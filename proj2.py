"""
File: proj2.py
Author: Rooklyn Kline
Date: 11/8/19
Section: 15
E-mail: rkline2@umbc.edu
Description:
   This program starts out by asking each player what they would like their character symbol to be. 
It will then print out a hexagon with six vertices and continuously ask the players where they
would like to "draw" a line. Once the player has entered two valid points, it will connect two vertices 
by "drawing" a line between the two points with their character symbol. The player who creates a 
triangle from their own lines will result in them losing.   
"""
from proj2_ui import print_board

# Used for input validation
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
NOTHING = ''

# Represents the index value
PLAYER_1_SYMBOL = 0
PLAYER_2_SYMBOL = 1

# For-loop expressions
END = 1
REVERSE = -1
BEGINNING = -1

# Max and min values a player can enter
LOWEST_VERTICES = 1
HIGHEST_VERTICES = 6

# List values
ONE_VALUE = 1
TWO_VALUES = 2
THREE_VALUES = 3
EMPTY_LIST = 0
FIRST_VALUE = 0
SECOND_VALUE = 1
TWO_LISTS = 2

# Return values to determine who lost
P1_LOSES = 1
P2_LOSES = 2


def ask_character():
    """
    Asks the user what symbol they would like to use while they play the game.
    It makes sure that the character isn't nothing, only one character long and
    player 2's character is not the same as player 1.

    :return: A list of the two imputed symbols.
    """
    char_list = []
    # The code below is for player 1
    player_1_char = NOTHING
    while player_1_char == NOTHING or len(player_1_char) > ONE_VALUE:
        player_1_char = nowhitespace(input("Hello, what character would player 1 like to use? "))
        # Makes sure player_1_char is valid
        if player_1_char == NOTHING:
            print("Invalid input")
        elif len(player_1_char) > ONE_VALUE:
            print("You can only enter a single value")
        else:
            char_list.append(player_1_char)

    # The code below is for player 2
    player_2_char = NOTHING
    while player_2_char == NOTHING or len(player_2_char) > ONE_VALUE:
        player_2_char = nowhitespace(input("Hello, what character would player 2 like to use? "))
        # Makes sure player_2_char is valid
        if player_2_char == NOTHING:
            print("Invalid input")
        elif len(player_2_char) > ONE_VALUE:
            print("You can only enter a single value")
        elif player_2_char == player_1_char:
            print("This symbol has already been used")
            player_2_char = NOTHING
        else:
            char_list.append(player_2_char)
    return char_list
        

def nowhitespace(input_response):
    """
    This function removes all of the white spaces of any statement.

    :param input_response: This parameter represents the
     word you would like to remove all of the white spaces from.
    :return: The parameter as a single word.
    """
    input_response = input_response.strip()
    input_response = input_response.split()
    input_response = NOTHING.join(input_response)
    return input_response


def convert_to_list(input_response):
    """
    This function converts the two imputed numbers (ex: 5 4) 
    into a list (ex.[5,4]).

    :param input_response: Represents the users imputed value.
    :return: The value as a single list.
    """
    input_response = input_response.strip()
    input_response = input_response.split()
    return input_response


def are_coordinates_valid(coordinates):
    """
    Checks to see if the coordinates are valid by making sure that
    the two values are not the same (ex: [1,1]). It checks if the values 
    are positive integers and if the values are in the range 1-6.
 
    :param coordinates: The user's imputed coordinates as a single list.
    :return: True if the input is valid and False if it is not.
    """
    int_list = []
    # Makes sure the values are positive integers
    for value in coordinates:
        if value not in NUMBERS:
            print("Invalid input")
            return False
    for input_value in coordinates:
        int_list.append(int(input_value))
    # Checks if they only entered two values
    if len(int_list) != TWO_LISTS:
        print("Invalid input")
        return False
    else:
        # Checks if the values are in range 1-6
        for integer_value in int_list:
            if (integer_value < LOWEST_VERTICES) or (integer_value > HIGHEST_VERTICES):
                print("You have entered a value out of the range 1-6")
                return False
            # Checks if the values are the same (ex. [3, 3])
            elif (integer_value == int_list[FIRST_VALUE]) and (integer_value == int_list[SECOND_VALUE]):
                print("Invalid input")
                return False
        return int_list


def reverse_the_list(entered_list):
    """
    Reverses the user's imputed coordinates.

    :param entered_list: The coordinates the user imputed as a single list.
    :return: The user's coordinates in reverse.
    """
    reverse_list = []
    for list_element in range(END, BEGINNING, REVERSE):
        reverse_list.append(entered_list[list_element])
    return reverse_list


def ask_p1_coordinates():
    """
    Asks player 1 for coordinates and calls are_coordinates_valid() to make sure
    it's valid. It will continue to ask the user for coordinates until it meets
    the are_coordinates_valid()'s criteria. It will also reverse the list if the first 
    value is greater than the second value.
 
    :return: The user's imputed coordinates and the coordinate's values in reverse. This will
    all be in a 2-D list.
    """
    ask_p1_num = NOTHING
    p1_moves = []
    while len(ask_p1_num) == EMPTY_LIST:
        # Converts the two values in a list and makes sure they're valid
        ask_p1_num = are_coordinates_valid(convert_to_list(input("Enter player 1 coordinates: ")))
        if ask_p1_num is False:
            ask_p1_num = NOTHING
        else:
            # The first value will now always be less than the second value
            if ask_p1_num[FIRST_VALUE] > ask_p1_num[SECOND_VALUE]:
                p1_moves.append(reverse_the_list(ask_p1_num))
            else:
                p1_moves.append(ask_p1_num)
    return p1_moves


def ask_p2_coordinates():
    """
    Asks player 2 for coordinates and calls are_coordinates_valid() to make sure
    it's valid. It will continue to ask the user for coordinates until it meets
    the are_coordinates_valid()'s criteria. It will also reverse the list if the first
    value is greater than the second value.

    :return: The user's imputed coordinates and the coordinate's values in reverse. This will
    all be in a 2-D list.
    """
    ask_p2_num = NOTHING
    p2_moves = []
    while len(ask_p2_num) == EMPTY_LIST:
        # Converts the two values in a list and makes sure they're valid
        ask_p2_num = are_coordinates_valid(convert_to_list(input("Enter player 2 coordinates: ")))
        if ask_p2_num is False:
            ask_p2_num = NOTHING
        else:
            # The first value will now always be less than the second value
            if ask_p2_num[FIRST_VALUE] > ask_p2_num[SECOND_VALUE]:
                p2_moves.append(reverse_the_list(ask_p2_num))
            else:
                p2_moves.append(ask_p2_num)
    return p2_moves


def find_entered_val(main_list, test_list):
    """
    Makes sure that the imputed coordinates have not been previously used.

    :param main_list: A list of all of coordinates that has been used in the game.
    :param test_list: The list that needs to be tested.
    :return: Returns false if the tested coordinated have been used before.
    """
    for sub_list in range(len(main_list)):
        for coordinates in range(len(test_list)):
            if main_list[sub_list] == test_list[coordinates]:
                print("This value has already been entered")
                return False


def print_game_board(p1_character, p2_character):
    """
    This function asks the each player the coordinates they would like to use. If the
    coordinates are valid, then it will print out the board and continue to ask for
    coordinates until a player has drawn a triangle. It will call other
    functions inside of this function such as ask_p1_coordinates() and ask_p2_coordinates(). 

    :param p1_character: The character's symbol for player 1.
    :param p2_character: The character's symbol for player 2.
    :return: none
    """
    main_list = []
    p1_lines = []
    p2_lines = []
    winner = is_winner(p1_lines, p2_lines, main_list)
    while winner is False:
        # The code below is for player 1
        print_board(p1_lines, p1_character, p2_lines, p2_character)
        p1_coordinates = ask_p1_coordinates()
        # Makes sure the entered coordinate is valid before proceeding
        while find_entered_val(main_list, p1_coordinates) is False:
            p1_coordinates = ask_p1_coordinates()
        else:
            # Valid inputs are appended in their appropriate lists
            for p1_list_value in p1_coordinates:
                main_list.append(p1_list_value)
                p1_lines.append(p1_list_value)
            print_board(p1_lines, p1_character, p2_lines, p2_character)
            winner = is_winner(p1_lines, p2_lines, main_list)
        # The code below is for player 2
        if winner is False:
            p2_coordinates = ask_p2_coordinates()
            # Makes sure the entered coordinate is valid before proceeding
            while find_entered_val(main_list, p2_coordinates) is False:
                p2_coordinates = ask_p2_coordinates()
            else:
                # Valid inputs are appended in their appropriate lists
                for p2_list_value in p2_coordinates:
                    main_list.append(p2_list_value)
                    p2_lines.append(p2_list_value)
                    winner = is_winner(p1_lines, p2_lines, main_list)
    # Determines which player formed a triangle
    if winner is not False:
        if winner == P1_LOSES:
            print("Game over. Player 1 loses")
        elif winner == P2_LOSES:
            print_board(p1_lines, p1_character, p2_lines, p2_character)
            print("Game over. Player 2 loses")


def is_winner(p1_moves, p2_moves, total_moves):
    """
    This function determines who loses the game by analyzing the current 
    moves that have been made by each player.
     
    :param p1_moves: The moves player 1 has made in the game.
    :param p2_moves: The moves player 2 has made in the game.
    :param total_moves: The total amount of moves in the game.
    :return: Returns false if neither player 1 nor 2 created a triangle or returns 
    the value P1_LOSES or P2_LOSES depending on who created the triangle.
    """
    total_moves = total_moves
    # The code below is for player 1
    for p1_row in range(len(p1_moves)):
        # Tests the sub-lists in player_1 if they have the same first index value
        test_list = []
        for p1_row_test in range(p1_row, len(p1_moves)):
            if p1_moves[p1_row][FIRST_VALUE] == p1_moves[p1_row_test][FIRST_VALUE]:
                test_list.append(p1_moves[p1_row_test])
        if len(test_list) >= TWO_LISTS:
            # Tests to see if the second sub-list index value in test_list
            # is equal to the first sub-list index value in p1_moves
            for test in range(len(test_list)):
                second_index_list = []
                for moves in range(len(p1_moves)):
                    if test_list[test][SECOND_VALUE] == p1_moves[moves][FIRST_VALUE] and \
                       test_list[test] != p1_moves[moves]:
                        second_index_list.append(p1_moves[moves])

                if len(second_index_list) > EMPTY_LIST:
                    # Tests to see if the second sub-list index value in test_list
                    # is equal to the second sub-list index value in second_index_list
                    for test_index in range(len(test_list)):
                        for second_test_index in range(len(second_index_list)):
                            if test_list[test_index][SECOND_VALUE] == \
                               second_index_list[second_test_index][SECOND_VALUE] \
                               and test_list[test] != second_index_list[second_test_index]:
                                return P1_LOSES

    # The code below is for player 2
    for p2_row in range(len(p2_moves)):
        # Tests the sub-lists in player_2 if they have the same first index value
        test_list = []
        for y in range(p2_row, len(p2_moves)):
            if p2_moves[p2_row][FIRST_VALUE] == p2_moves[y][FIRST_VALUE]:
                test_list.append(p2_moves[y])
        if len(test_list) >= TWO_LISTS:
            # Tests to see if the second sub-list index value in test_list
            # is equal to the first sub-list index value in p2_moves
            for test in range(len(test_list)):
                second_index_list = []
                for moves in range(len(p2_moves)):
                    if test_list[test][SECOND_VALUE] == p2_moves[moves][FIRST_VALUE] and \
                       test_list[test] != p2_moves[moves]:
                        second_index_list.append(p2_moves[moves])

                if len(second_index_list) > EMPTY_LIST:
                    # Tests to see if the second sub-list index value in test_list
                    # is equal to the second sub-list index value in second_index_list
                    for test_index in range(len(test_list)):
                        for second_test_index in range(len(second_index_list)):
                            if test_list[test_index][SECOND_VALUE] == \
                               second_index_list[second_test_index][SECOND_VALUE] and \
                               test_list[test] != second_index_list[second_test_index]:
                                return P2_LOSES
    return False


if __name__ == '__main__':
    character = ask_character()
    print_game_board(character[PLAYER_1_SYMBOL], character[PLAYER_2_SYMBOL])
