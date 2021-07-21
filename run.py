from random import randrange
import random


def check_ok(boat, occupied):

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
    boats = [5, 4, 3, 3, 3, 2]
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
    print("            Battleships       ")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
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
    print("            Battleships       ")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
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


def check_if_empty_2(list_of_lists):
    return all([not elem for elem in list_of_lists])



occupied = []
hit = []
miss = []
sink = []
guesses = []
boats = []

ships, occupied = create_boats(occupied, boats)
show_board_c(occupied)
strategy = []

for i in range(80):
    shot, guesses = get_shot_comp(guesses, strategy)
    ships, hit, miss, comp, missed = check_shot(shot, ships, hit, miss, sink)
    show_board(hit, miss, sink)
    if missed == 1:
        strategy = calc_strategy(shot, strategy, guesses, hit)
    elif missed == 2:
        strategy = []
    elif len(strategy) > 0:
        strategy.pop(0)

    if check_if_empty_2(ships):
        print("end of game", i)
        break

show_board_c(occupied)
show_board(hit, miss, sink)
