from random import randrange


def check_ok(boat, occupied):
    
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

    return boat


def check_boat(b, start, dirn, occupied):
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
            boat = check_ok(boat, occupied)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
            boat = check_ok(boat, occupied)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
            boat = check_ok(boat, occupied)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
            boat = check_ok(boat, occupied)

    return boat


def create_boats():
    occupied = []
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


def show_board(hit, miss, comp):
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


def get_shot_comp(guesses):

    ok = "n"
    while ok == "n":
        try:
            shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
        except:
            print("Incorrect entry - please enter again")

    return shot, guesses


def check_shot(shot, ships, hit, miss, sink):

    missed = 1
    for i in range(len(ships)):
        if shot in ships[i]:
            ships[i].remove(shot)
            missed = 0
            if len(ships[i]) > 0:
                hit.append(shot)
            else:
                sink.append(shot)
    if missed == 1:
        miss.append(shot)

    return ships, hit, miss, sink


hit = []
miss = []
sink = []
guesses = []

ships, occupied = create_boats()
show_board_c(occupied)


shot, guesses = get_shot_comp(guesses)
ships, hit, miss, comp = check_shot(shot, ships, hit, miss, sink)
show_board(hit, miss, sink)



# boat2 = [6, 16, 26]
# boat1 = [45, 46, 47]
# hit = []
# miss = []
# sink = []

# for i in range(10):
#     guesses = hit + miss + sink
#     shot = get_shot(guesses)
#     boat1, boat2, hit, miss, sink = check_shot(shot,boat1,boat2,hit,miss,sink)
#     show_board(hit, miss, sink)

#     if len(boat1) < 1 and len(boat2) < 1:
#         print("You have Won!")
#         break
# print("Finished")
