import random
import time


def check_ok(boat, occupied_coordinate):
    """
    Iterates through the coordinates of the boat and checks
    to see if placement is valid and if boat coordinates run
    off edges of board, returns 'boat'.

    Args:
    boat -- A boat in the game made by the user's input
    occupied_coordinate -- A number on the board that has been taken by
    a battleship
    """
    boat.sort()
    for i in range(len(boat)):
        num = boat[i]
        # if the boat is trying to place  in occupied area break
        if num in occupied_coordinate:
            boat = [-1]
            break
        # if boat coordinate is below min or above max break
        elif num < 0 or num > 99:
            boat = [-1]
            break
        # if the boat is running off the edge of grid break
        elif num % 10 == 9 and i < len(boat) - 1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break
        # if boat is running off the edge of grid break
        if i != 0:
            if boat[i] != boat[i-1]+1 and boat[i] != boat[i-1]+10:
                boat = [-1]
                break

    return boat


def get_ship(length_of_boat, occupied_coordinate):
    """
    Takes input from the user to place ship, checks if placement is valid, if
    it is store it in ship list.
    If it is invalid or already used then display error message.

    Args:
    length_of_boat -- The length of the boats predetermined before game
    occupied_coordinate -- A number on the board that has been taken
    by a battleship
    """
    ok = True
    while ok:
        ship = []
        # ask user to enter coordinate for placement of ship
        print("Now please enter your coordinates one at a time for ship \
            length", length_of_boat)
        for i in range(length_of_boat):
            print("")
            boat_num = input("Enter coordinate. ")
            print("")
            ship.append(int(boat_num))
        # check that ship is valid
        ship = check_ok(ship, occupied_coordinate)
        if ship[0] != -1:
            occupied_coordinate = occupied_coordinate + ship
            break
        else:
            print("Error - please try again")

    return ship, occupied_coordinate


def create_ships(occupied_coordinate, boats):
    """
    Creates a list of ships from the boats list

    Args:
    occupied_coordinate -- A number on the board that has been
    taken by a battleship
    boats -- A predetermined list of the different sized boats in the game
    """
    ships = []
    # predetermined before game start
    boats = [5, 4, 3, 3, 2]

    for boat in boats:
        ship, occupied_coordinate = get_ship(boat, occupied_coordinate)
        ships.append(ship)

    return ships, occupied_coordinate


def check_boat(start_length_of_boat, start, dirn, occupied_coordinate):
    """
    Checks to make sure the boat is being placed correctly
    on the board. and returns the value for boat.

    Args:
    start_length_of_boat -- The predetermined length of the boat
    start -- startng coordinate for boat
    dirn -- The direction the boat is facing i.e. vertical, horizontol
    occupied_coordinate -- A number on the board that has been taken
    by a battleship
    """
    boat = []
    # checks the 4 directions of boat and appends it to boat list of valid
    if dirn == 1:
        for i in range(start_length_of_boat):
            boat.append(start - i*10)
    elif dirn == 2:
        for i in range(start_length_of_boat):
            boat.append(start + i)
    elif dirn == 3:
        for i in range(start_length_of_boat):
            boat.append(start + i*10)
    elif dirn == 4:
        for i in range(start_length_of_boat):
            boat.append(start - i)
    boat = check_ok(boat, occupied_coordinate)

    return boat


def create_boats(occupied_coordinate, boats):
    """
    Takes the input from the user validates it and adds it to the
    ships list
    When we have not gotten a valid boat the loop continues
    and when we do it gets appended to the ships list

    Args:
    occupied_coordinate -- A number on the board that has been taken
    by a battleship
    boats -- A list of the different sized boats in the game
    """
    ships = []
    for start_length_of_boat in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = random.randrange(99)
            boat_direction = random.randrange(1, 4)
            boat = \
                check_boat(start_length_of_boat, boat_start,
                           boat_direction, occupied_coordinate)
        ships.append(boat)
        occupied_coordinate = occupied_coordinate + boat

    return ships, occupied_coordinate


def show_board_c(occupied_coordinate):
    """
    Creates the game board for the computer.
    Inside for loop creates the row and the outside for loop
    prints each row.

    Args:
    occupied_coordinate -- A number on the board that has been taken
    by a battleship
    """
    print("This is where you placed your ships, Remember your board will \
        be on top and the AI board is on the bottom\n")
    print("            Your Battleships      ")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " . "
            if place in occupied_coordinate:
                ch = " o "
            row = row + ch
            place = place + 1
        print(x, " ", row)


def get_shot_comp(guesses, strategy):
    """
    Gets shot from computer, checks to see if there is an intelligent guess
    available using 'strategy'.
    No intelligent guess, then it attempts to make a random shot.
    The shot is then compared with previous guesses,
    If valid then it records the shot.

    Args:
    guesses -- previous guesses inputted from the user
    """
    ok = "n"
    while ok == "n":
        try:
            if len(strategy) > 0:
                shot = strategy[0]
            else:
                shot = random.randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
        except Exception:
            print("Incorrect entry - please enter again")

    return shot, guesses


def instructions(occupied_coordinate):
    """
    Prints out the Game instructions to the user before game starts

    Args:
    occupied_coordinate -- A number on the board that has been taken
    by a battleship
    """
    print("\rThe Game is simple, Try to find and sink all of the \
        opponents ships\n before they sink yours\n")
    time.sleep(3)
    print("\rEach player will take turns shooting to try and find\
         the opponents ships\n")
    time.sleep(3)
    print("\rEach player has 5 Battleships and 80 bullets\n")
    time.sleep(3)
    print("\rThe first player to sink all of the opponents Battleships \
        will be the winner.\n")
    time.sleep(3)
    print("This is your game grid, ships can be placed vertical or \
        horizontal. NOT diagonally\n")
    time.sleep(3)
    # print an example game board to the user for clarification
    print("            Your Battleships      ")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " . "
            if place in occupied_coordinate:
                ch = " o "
            row = row + ch
            place = place + 1
        print(x, " ", row)

    time.sleep(3)
    print("\rAs you can see the board is a 10x10 Grid numbered 0-99\n")
    time.sleep(3)
    print("\rThe battleships are differant lengths and can be placed \
        in different ways.\n")
    time.sleep(3)
    print("\rAn Example of a ship with the length of 5 is: 10,11,12,13,14\n")
    time.sleep(3)
    print("\rThe player would enter one coordinate at a time. 10 then 11\
         then 12 and so on.\n")
    time.sleep(3)
    print("\rThen they would enter in the next ship of length 4\n")
    time.sleep(3)
    print(
        "\rAn Example of this would be 80,70,60,50 this ship would be\
             vertical\n")
    time.sleep(3)
    print("On the board an 'x' marks a miss\n An 'o' means you hit \
        the ship\n And a '0' means that you sunk a Battleship\n")
    time.sleep(3)
    print("\rNow you are ready to go to battle!\n")


def show_board(hit, miss, sink):
    """
    Creates the game board for the player.
    Inside for loop creates the row and the outside for loop
    prints each row.

    Args:
    hit -- A number on the board that has hit one of the battleships
    miss -- A number on the board that has missed one of the battleships
    sink -- A number on the board that has completed a battleship
    """
    print("            Battleships       ")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " . "
            if place in miss:
                ch = " x "
            elif place in hit:
                ch = " o "
            elif place in sink:
                ch = " O "

            row = row + ch
            place = place + 1
        print(x, " ", row)


def check_shot(shot, ships, hit, miss, sink):
    """
    Checks shot,
    If shot is in the ships list it will either be a hit or a sink,
    if the shot is not in the boat it will be a miss.
    Correctly appends or removes the shot accordingly

    Args:
    shot -- The player's recent shot/guess to try and sink the opponents ship
    ships -- A list containing the ships in the game after the input from user
    hit -- A number on the board that has hit one of the battleships
    miss -- A number on the board that has missed one of the battleships
    sink -- A number on the board that has completed a battleship
    """
    missed = 0
    for i in range(len(ships)):
        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
                # this is used when computer shoots
            else:
                sink.append(shot)
                missed = 2
                # this is used when computer shoots
    if missed == 0:
        miss.append(shot)

    return ships, hit, miss, sink, missed


def calc_strategy(shot, strategy, guesses, hit):
    """
    Strategy for the computer guesses,
    takes a shot and if it is a hit makes the computer guess
    a number above, below, left or right of the first guess.
    it then places these guesses into a temp list.

    Args:
    shot -- The input of a coordinate to try and sink a ship
    strategy -- The amount of hits made by computer to sink a ship
    guesses -- previous valid coordinates inputted by the user
    """
    temp = []
    if len(strategy) < 1:
        temp = [shot-1, shot+1, shot-10, shot+10]
    else:
        if shot-1 in hit:
            temp = [shot+1]
            for num in [2, 3, 4, 5, 6, 7, 8]:
                if shot-num not in hit:
                    temp.append(shot-num)
                    break
        elif shot+1 in hit:
            temp = [shot-1]
            for num in [2, 3, 4, 5, 6, 7, 8]:
                if shot+num not in hit:
                    temp.append(shot+num)
                    break
        if shot-10 in hit:
            temp = [shot+10]
            for num in [20, 30, 40, 50, 60, 70, 80]:
                if shot-num not in hit:
                    temp.append(shot-num)
                    break
        elif shot+10 in hit:
            temp = [shot-10]
            for num in [20, 30, 40, 50, 60, 70, 80]:
                if shot+num not in hit:
                    temp.append(shot+num)
                    break
    # if the values in temporary list are on the board and not in guesses
    # then the values can be placed in this candidate list
    cand = []
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            cand.append(temp[i])
    # this list is then shuffled
    random.shuffle(cand)
    # the shuffled list is then returned
    return cand


def get_shot(guesses):
    """
    Take in input for user's shot.
    Check to see if the user's shot is valid, if it is return the shot
    if it is incorrect, give correct error message.

    Args:
    guesses -- previous valid coordinates inputted by the user
    """
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter a guess between 0 and 99: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("incorrect number. Make sure your guess is \
                    between 0 and 99.")
            elif shot in guesses:
                print("incorrect number, you have already tried that one!")
            else:
                ok = "y"
                break
        except Exception:
            print("Invalid entry - please try again!")

    return shot


def check_if_empty_2(list_of_lists):
    """
    Checks if a list of lists is empty
    This was taken from StackOverFlow and was not written by the developer
    """
    return all([not elem for elem in list_of_lists])


# before game starts
hit1 = []
miss1 = []
sink1 = []
guesses1 = []
missed1 = 0
strategy1 = []
occupied_coordinate1 = []
occupied_coordinate2 = []
hit2 = []
miss2 = []
sink2 = []
guesses2 = []
missed2 = 0
strategy2 = []

# Amount of ships in game
battleships = [5, 4, 3, 3, 2]

# Game Instructions
instructions(occupied_coordinate2)

# computer creates a board for player 1
ships1, occupied_coordinate1 = create_boats(occupied_coordinate1, battleships)

# user creates the board for player 2 - show board
ships2, occupied_coordinate2 = create_ships(occupied_coordinate2, battleships)
show_board_c(occupied_coordinate2)

# loop for player shots with a total of 80 bullets
for i in range(80):
    # player shoots
    guesses1 = hit1 + miss1 + sink1
    shot1 = get_shot(guesses1)
    ships1, hit1, miss1, sink1,\
        missed1 = check_shot(shot1, ships1, hit1, miss1, sink1)
    show_board(hit1, miss1, sink1)
    # repeat until ships empty
    if check_if_empty_2(ships1):
        print("End of game - You are the winner in", i)
        break

    # computer shoots
    shot2, guesses2 = get_shot_comp(guesses2, strategy2)
    ships2, hit2, miss2, sink2, \
        missed2 = check_shot(shot2, ships2, hit2, miss2, sink2)
    show_board(hit2, miss2, sink2)

    if missed2 == 1:
        tactics2 = calc_strategy(shot2, strategy2, guesses2, hit2)
    elif missed2 == 2:
        strategy2 = []

    # if the list is not empty get rid of number in first index place
    # and then move on to the second one

    elif len(strategy2) > 0:
        strategy2.pop(0)

    # checks to see if see if players ships list is empty and computer has won
    if check_if_empty_2(ships2):
        print("end of game - computer wins in", i)
        break
