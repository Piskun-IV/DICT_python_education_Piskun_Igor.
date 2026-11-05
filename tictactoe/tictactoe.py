def print_grid(c):
    print("---------")
    print(f"| {c[0]} {c[1]} {c[2]} |")
    print(f"| {c[3]} {c[4]} {c[5]} |")
    print(f"| {c[6]} {c[7]} {c[8]} |")
    print("---------")


def check_win(c, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for w in wins:
        if c[w[0]] == c[w[1]] == c[w[2]] == player:
            return True
    return False


cells = "         "
print_grid(cells)
current_player = 'X'

while True:
    raw_coords = input("Enter the coordinates: ").split()
    joined_coords = "".join(raw_coords)

    if not joined_coords.isdigit() or len(joined_coords) != 2:
        print("You should enter numbers!")
        continue

    r = int(joined_coords[0])
    c = int(joined_coords[1])

    if r < 1 or r > 3 or c < 1 or c > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    index = (r - 1) * 3 + (c - 1)

    if cells[index] != ' ':
        print("This cell is occupied! Choose another one!")
        continue

    cells_list = list(cells)
    cells_list[index] = current_player
    cells = "".join(cells_list)

    print_grid(cells)

    if check_win(cells, current_player):
        print(f"{current_player} wins")
        break
    elif ' ' not in cells:
        print("Draw")
        break

    current_player = 'O' if current_player == 'X' else 'X'