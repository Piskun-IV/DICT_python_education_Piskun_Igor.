import random

print("How many pencils would you like to use:")
while True:
    pencils_str = input()
    if not pencils_str.isdigit():
        print("The number of pencils should be numeric")
        continue
    pencils = int(pencils_str)
    if pencils == 0:
        print("The number of pencils should be positive")
        continue
    break

print("Who will be the first (John, Jack):")
while True:
    current_player = input()
    if current_player not in ["John", "Jack"]:
        print("Choose between 'John' and 'Jack'")
        continue
    break

while pencils > 0:
    print("|" * pencils)

    if current_player == "Jack":
        print("Jack's turn:")
        if pencils % 4 == 0:
            taken = 3
        elif pencils % 4 == 3:
            taken = 2
        elif pencils % 4 == 2:
            taken = 1
        else:
            taken = random.randint(1, min(3, pencils))
        print(taken)
    else:
        print("John's turn!")
        while True:
            taken_str = input()
            if taken_str not in ['1', '2', '3']:
                print("Possible values: '1', '2' or '3'")
                continue
            taken = int(taken_str)
            if taken > pencils:
                print("Too many pencils were taken")
                continue
            break

    pencils -= taken

    if pencils == 0:
        winner = "John" if current_player == "Jack" else "Jack"
        print(f"{winner} won!")
        break

    current_player = "Jack" if current_player == "John" else "John"