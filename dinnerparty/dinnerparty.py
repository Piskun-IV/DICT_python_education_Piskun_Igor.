import random

n = int(input("Enter the number of friends joining (including you):\n"))

if n <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {input(): 0 for _ in range(n)}

    total = float(input("Enter the total amount:\n"))

    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if answer == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")
        split_amount = round(total / (n - 1), 2)
        friends = {name: (0 if name == lucky_one else split_amount) for name in friends}
    else:
        print("No one is going to be lucky")
        split_amount = round(total / n, 2)
        friends = {name: split_amount for name in friends}

    print(friends)