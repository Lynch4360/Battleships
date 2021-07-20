from random import randrange


def check_boat(b, start, dirn):
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
            print(start - i*10)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
            print(start + i)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
            print(start + i*10)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
            print(start - i)


boats = [5, 4, 3, 3, 2, 2]
for b in boats:
    boat_start = randrange(99)
    boat_direction = randrange(1, 4)
    print(b, boat_start, boat_direction)
    check_boat(b, boat_start, boat_direction)


# def get_shot(guesses):

#     ok = "n"
#     while ok == "n":
#         try:
#             shot = input("please enter your guess")
#             shot = int(shot)
#             if shot < 0 or shot > 99:
#                 print("incorrect number, please try again")
#             elif shot in guesses:
#                 print("incorrect number, please try again")

#             else:
#                 ok = "y"
#                 break
#         except:
#             print("please enter again")

#     return shot


# def show_board(hit, miss, sink):
#     print("            Battleships       ")
#     print("     0  1  2  3  4  5  6  7  8  9")

#     place = 0
#     for x in range(10):
#         row = ""
#         for y in range(10):
#             ch = " _ "
#             if place in miss:
#                 ch = " x "
#             elif place in hit:
#                 ch = " o "
#             elif place in sink:
#                 ch = " O "

#             row = row + ch
#             place = place + 1
#         print(x, " ", row)


# def check_shot(shot, boat1, boat2, hit, miss, sink):

#     if shot in boat1:
#         boat1.remove(shot)
#         if len(boat1) > 0:
#             hit.append(shot)
#         else:
#             sink.append(shot)
#     elif shot in boat2:
#         boat2.remove(shot)
#         if len(boat2) > 0:
#             hit.append(shot)
#         else:
#             sink.append(shot)
#     else:
#         miss.append(shot)

#     return boat1, boat2, hit, miss, sink


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
