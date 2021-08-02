from random import randrange
import random


def check_ok(boat, occupied):
    """
    Iterates through the coordinates of the boat and checks
    to see if placement is valid and if boat coordinates run
    off edges of board, returns 'boat'.

    Keyword arguments:
    boat -- A boat in the game made by the user's input
    occupied -- A number on the board that has been taken by a battleship
    """
    boat.sort()
    for i in range(len(boat)):
        num = boat[i]
        if num in occupied:
            boat = [-1]
            break
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(boat) - 1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break
        if i != 0:
            if boat[i] != boat[i-1]+1 and boat[i] != boat[i-1]+10:
                boat = [-1]
                break

    return boat


def get_ship(long, occupied):
    """
    Takes input from the user to place ship, checks if placement is valid, if it is store it in ship list.
    If it is invalid or already used then display error message.

    Keyword arguments:
    long -- The length of the ship
    occupied -- A number on the board that has been taken by a battleship
    """
    print("Now you must enter the coordinates for your ship.\nYou will do this one coordinate at a time.\nType in your number. Press enter and then type in the next coordinate.\nRemember Battleships can only be placed vertical and horizontal.\nSome Examples are\n [11,12,13,14,] [66,65,64] [20,30,40,50] [77,67,57]")
    ok = True
    while ok:
        ship = []
        # ask user to enter numbers
        print("Now please enter your coordinates one at a time for ship length", long)
        for i in range(long):
            boat_num = input("Enter coordinate. ")
            ship.append(int(boat_num))
        # check that ship
        ship = check_ok(ship, occupied)
        if ship[0] != -1:
            occupied = occupied + ship
            break
        else:
            print("Error - please try again")

    return ship, occupied


def create_ships(occupied, boats):
    """
    Creates a list of ships from the boats list

    Keyword arguments:
    occupied -- A number on the board that has been taken by a battleship
    boats -- A list of the different sized boats in the game
    """
    ships = []
    boats = [5, 4, 3, 3, 3, 2]

    for boat in boats:
        ship, occupied = get_ship(boat, occupied)
        ships.append(ship)

    return ships, occupied


def check_boat(b, start, dirn, occupied):
    """
    Checks to make sure the boat is being placed correctly
    on the board. and returns the value for boat.

    Keyword arguments:
    b -- The length of the boat
    start -- Where the boat starts
    dirn -- The direction the boat is facing
    occupied -- A number on the board that has been taken by a battleship
    """
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
    boat = check_ok(boat, occupied)

    return boat


def create_boats(occupied, boats):
    """
    When we have not gotten a valid boat the loop continues
    and when we do it gets appended to the ships list
    Keyword arguments:
    occupied -- A number on the board that has been taken by a battleship
    boats -- A list of the different sized boats in the game
    """
    ships = []
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 4)
            boat = check_boat(b, boat_start, boat_direction, occupied)
        ships.append(boat)
        occupied = occupied + boat

    return ships, occupied


def show_board_c(occupied):
    """
    Creates the game board for the computer.
    Inside for loop creates the row and the outside for loop
    prints each row.
    Keyword Arguments:
    occupied -- A number on the board that has been taken by a battleship
    """
    print("This is where you placed your ships,/nHit = o, Miss = X, Sink Boat = O/nRemember your guesses will be on top and the AI guesses on the bottom")
    print("            Your Battleships      ")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " . "
            if place in occupied:
                ch = " o "
            row = row + ch
            place = place + 1
        print(x, " ", row)


def get_shot_comp(guesses, strategy):
    """
    Gets shot from computer, checks to see if there is an intelligent guess available using 'strategy'.
    No intelligent guess, then it attempts to make a random shot.
    Shot is then compared with previous guesses if valid then it makes the shot.
    Keyword arguments:
    guesses -- previous guessdes made by user
    """
    ok = "n"
    while ok == "n":
        try:
            if len(strategy) > 0:
                shot = strategy[0]
            else:
                shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
        except:
            print("Incorrect entry - please enter again")

    return shot, guesses


def show_board(hit, miss, sink):
    """
    Creates the game board for the player.
    Inside for loop creates the row and the outside for loop
    prints each row.
    Keyword Arguments:
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

    Keyword arguments:
    shot -- The player's guesses that are valid
    ships -- A list containing the ships in the game
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
    it then places these guesses into a temp list
    Keyword arguments:
    shot -- The player's guesses that are valid
    strategy -- Stores the computer guess for calc_strategy()
    guesses -- previous guessdes made by user
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
    cand =[]
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

    Keyword arguments:
    guesses -- previous guesses made by user
    """
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter a guess between 0 and 99: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("incorrect number. Make sure your guess is between 0 and 99.")
            elif shot in guesses:
                print("incorrect number, you have already tried that one!")
            else:
                ok = "y"
                break
        except:
            print("Invalid entry - please try again!")

    return shot


def check_if_empty_2(list_of_lists):
    """
    Checks if a list of lists is empty
    This was taken from StackOverFlow
    """
    return all([not elem for elem in list_of_lists])


# before game
hit1 = []
miss1 = []
sink1 = []
guesses1 = []
missed1 = 0
strategy1 = []
occupied1 = []
occupied2 = []
hit2 = []
miss2 = []
sink2 = []
guesses2 = []
missed2 = 0
strategy2 = []

# game amount of ships
battleships = [5, 4, 3, 3, 2, 2]

# computer creates a board for player 1
ships1, occupied1 = create_boats(occupied1, battleships)

# user creates the board for player 2 - show board
ships2, occupied2 = create_ships(occupied2, battleships)
show_board_c(occupied2)

# loop
for i in range(80):
    # player shoots
    guesses1 = hit1 + miss1 + sink1
    shot1 = get_shot(guesses1)
    ships1, hit1, miss1, sink1, missed1 = check_shot(shot1, ships1, hit1, miss1, sink1)
    show_board(hit1, miss1, sink1)
    # repeat until ships empty
    if check_if_empty_2(ships1):
        print("End of game - You are the winner in", i)
        break

    # computer shoots
    shot2, guesses2 = get_shot_comp(guesses2, strategy2)
    ships2, hit2, miss2, sink2, missed2 = check_shot(shot2, ships2, hit2, miss2, sink2)
    show_board(hit2, miss2, sink2)

    if missed2 == 1:
        tactics2 = calc_strategy(shot2, strategy2, guesses2, hit2)
    elif missed2 == 2:
        strategy2 = []
    # if the list is not empty get rid of number in first index place
    # and then move on to the second one
    elif len(strategy2) > 0:
        strategy2.pop(0)

    if check_if_empty_2(ships2):
        print("end of game - computer wins in", i)
        break
