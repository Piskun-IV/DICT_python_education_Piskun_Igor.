class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "action"
        self.running = True
        self.prompt()

    def prompt(self):
        if self.state == "action":
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.state == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif self.state == "fill_water":
            print("Write how many ml of water do you want to add:")
        elif self.state == "fill_milk":
            print("Write how many ml of milk do you want to add:")
        elif self.state == "fill_beans":
            print("Write how many grams of coffee beans do you want to add:")
        elif self.state == "fill_cups":
            print("Write how many disposable cups of coffee do you want to add:")

    def process_input(self, user_input):
        if self.state == "action":
            self.handle_action(user_input)
        elif self.state == "buy":
            self.handle_buy(user_input)
        elif self.state == "fill_water":
            self.water += int(user_input)
            self.state = "fill_milk"
            self.prompt()
        elif self.state == "fill_milk":
            self.milk += int(user_input)
            self.state = "fill_beans"
            self.prompt()
        elif self.state == "fill_beans":
            self.beans += int(user_input)
            self.state = "fill_cups"
            self.prompt()
        elif self.state == "fill_cups":
            self.cups += int(user_input)
            self.state = "action"
            self.prompt()

    def handle_action(self, action):
        if action == "buy":
            self.state = "buy"
            self.prompt()
        elif action == "fill":
            self.state = "fill_water"
            self.prompt()
        elif action == "take":
            print(f"I gave you {self.money}")
            self.money = 0
            self.prompt()
        elif action == "remaining":
            self.print_state()
            self.prompt()
        elif action == "exit":
            self.running = False

    def handle_buy(self, choice):
        if choice == 'back':
            self.state = "action"
            self.prompt()
            return

        need_water, need_milk, need_beans, cost = 0, 0, 0, 0
        if choice == '1':
            need_water, need_milk, need_beans, cost = 250, 0, 16, 4
        elif choice == '2':
            need_water, need_milk, need_beans, cost = 350, 75, 20, 7
        elif choice == '3':
            need_water, need_milk, need_beans, cost = 200, 100, 12, 6

        if self.water < need_water:
            print("Sorry, not enough water!")
        elif self.milk < need_milk:
            print("Sorry, not enough milk!")
        elif self.beans < need_beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= need_water
            self.milk -= need_milk
            self.beans -= need_beans
            self.cups -= 1
            self.money += cost

        self.state = "action"
        self.prompt()

    def print_state(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")


machine = CoffeeMachine()

while machine.running:
    user_in = input()
    machine.process_input(user_in)