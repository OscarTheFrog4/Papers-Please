from utils import wait
# Day
class Day:
    def __init__(self, nexa, is_running, food, heat):

        self.nexa = nexa
        self.is_running = is_running
        self.food = food
        self.heat = heat

        wait(2, 30)

    @staticmethod
    def needs(need, price, var, nexa, cause, is_running):

        # Satisfy needs
        if nexa >= price:
            response = input(f"Purchase {need} for {price} nexas? (y/n): ").lower()
            while not response == "n" and not response == "y":
                response = input(f"Purchase {need} for {price} nexas? Only respond with 'y' or 'n': ").lower()

            wait(0, 1)
            if response == "y":
                nexa -= price
                if var < 3:
                    var += 1
            elif response == "n":
                var -= 1

        else:
            print(f"You do not have enough money to buy {need}.")
            var -= 1
            wait(2, 0)

        if var == 0:
            print(f"You died of {cause}!")
            input("(Enter anything to continue): ")
            is_running = False

        return nexa, var, is_running

    def evaluate_day(self):

        print(f"You have {self.nexa} nexas to spend.")
        wait(3, 1)

        # Print Temperature and Hunger
        match self.food:
            case 3:
                print("You are full.")
            case 2:
                print("You are hungry.")
            case 1:
                print("You are starving.")

        wait(1, 0)

        match self.heat:
            case 3:
                print("You are warm.")
            case 2:
                print("You are cold.")
            case 1:
                print("You are freezing.")

        wait(1, 0)

        self.nexa, self.food, self.is_running = self.needs("food", 6, self.food, self.nexa, "starvation", self.is_running)
        self.nexa, self.heat, self.is_running = self.needs("heat", 4, self.heat, self.nexa, "the cold", self.is_running)



        if self.heat == 0:
            print("You died of the cold!")
            self.is_running = "dead"

        input("(Enter anything to continue): ")
        wait(0, 30)

        return self.nexa, self.food, self.heat, self.is_running


