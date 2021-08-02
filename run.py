from random import randrange
import random


def check_ok(boat, occupied):

    """
    
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

    ok = True
    while ok:
        ship = []
        # ask user to enter numbers
        print("Enter your ship of length", long)
        for i in range(long):
            boat_num = input("Please enter a number")
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
    # occupied = []
    ships = []
    boats = [5, 4, 3, 3, 3, 2]

    for boat in boats:
        ship, occupied = get_ship(boat, occupied)
        ships.append(ship)
    # ships = create_ships(occupied, boats)

    return ships, occupied


def check_boat(b, start, dirn, occupied):
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
    # occupied = []
    ships = []
    # boats = [5, 4, 3, 3, 3, 2]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 4)
            print(b, boat_start, boat_direction)
            boat = check_boat(b, boat_start, boat_direction, occupied)
        ships.append(boat)
        occupied = occupied + boat
        print(ships)

    return ships, occupied


def show_board_c(occupied):
    """
    Creates the game board for the computer.

    Inside for loop creates the row and the outside for loop
    prints each row.
    
    Keyword Arguments:
    occupied -- A number on the board that has been taken by a battleship
    """
    print("            Battleships       ")
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
    sink -- A number on the board that has completed a battleship and has sunk it
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

    missed = 0
    for i in range(len(ships)):
        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                sink.append(shot)
                missed = 2
    if missed == 0:
        miss.append(shot)

    return ships, hit, miss, sink, missed


def calc_strategy(shot, strategy, guesses, hit):

    temp = []
    if len(strategy) < 1:
        temp = [shot+1]
        for num in [2, 3, 4, 5, 6, 7, 8]:
            if shot-num not in hit:
                temp.append(shot+num)
                break
    elif shot+1 in hit:
        temp = [shot-1]
        for num in [2, 3, 4, 5, 6, 7, 8]:
            if shot+num not in hit:
                temp.append(shot+num) 
                break
    elif shot-10 in hit:
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

    cand = []
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            cand.append(temp[i])

    random.shuffle(cand)

    return cand


def get_shot(guesses):

    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("incorrect number, please try again")
            elif shot in guesses:
                print("incorrect number, used before")
            else:
                ok = "y"
                break
        except:
            print("Incorrect entry - please enter again")

    return shot


def check_if_empty_2(list_of_lists):
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

battleships = [5, 4, 3, 3, 2, 2]
# game amount of ships
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
        print("end of game - winner in", i)
        break
# computer shoots

    shot2, guesses2 = get_shot_comp(guesses2, strategy2)
    ships2, hit2, miss2, sink2, missed2 = check_shot(shot2, ships2, hit2, miss2, sink2)
    show_board(hit2, miss2, sink2)

    if missed2 == 1:
        tactics2 = calc_strategy(shot2, strategy2, guesses2, hit2)
    elif missed2 == 2:
        strategy2 = []
    elif len(strategy2) > 0:
        strategy2.pop(0)

    if check_if_empty_2(ships2):
        print("end of game - computer wins", i)
