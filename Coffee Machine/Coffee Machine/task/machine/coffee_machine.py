class CoffeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffe = 120
        self.disposable_cups = 9
        self.money = 550
        self.espresso = (250, 0, 16, 4)
        self.latte = (350, 75, 20, 7)
        self.cappuccino = (200, 100, 12, 6)

    def display(self):
        print(
            f'The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffe} of coffee beans\n{self.disposable_cups} of disposable cups\n{self.money} of money')

    def fill(self, ingredient, ingredient_name):
        print(f'Write how many ml of {ingredient_name} do you want to add:')
        return ingredient + int(input())

    def change_amount(self, action, *args, cups=1):
        print(args)
        if action == 'fill':
            self.water = self.fill(self.water, 'water')
            self.milk = self.fill(self.milk, 'milk')
            self.coffe = self.fill(self.coffe, 'coffe')
            self.disposable_cups = self.fill(self.disposable_cups, 'disposable cups')
        elif action == 'buy':
            self.water = self.water - args[0]
            self.milk = self.milk - args[1]
            self.coffe = self.coffe - args[2]
            self.disposable_cups = self.disposable_cups - cups
            self.money = self.money + args[3]
        elif action == 'take':
            self.money = 0

    def check_avaliable(self, args):
        if self.water - args[0] < 0:
            return 'water'
        elif self.milk - args[1] < 0:
            return 'milk'
        elif self.coffe - args[2] < 0:
            return 'coffee beans'
        elif self.disposable_cups / 1 < 1:
            return 'disposable cups'
        else:
            return False

    @staticmethod
    def _choice_action():
        print('Write action (buy, fill, take, remaining, exit):')
        return input()

    def buy(self, coffe_type):
        if coffe_type == '1':
            return self.check_avaliable(self.espresso)
        elif coffe_type == '2':
            return self.check_avaliable(self.latte)
        elif coffe_type == '3':
            return self.check_avaliable(self.cappuccino)

    def work(self):
        action = self._choice_action()
        if action == 'exit':
            exit()
        elif action == 'remaining':
            self.display()
        elif action == 'take':
            print(f'I gave you ${self.money}')
            self.change_amount(action)
        elif action == 'fill':
            self.change_amount(action)
        elif action == 'buy':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            coffe_type = input()
            if coffe_type == 'back':
                pass
            else:
                able = self.buy(coffe_type)
                if not able:
                    print('I have enough resources, making you a coffee!')
                    if coffe_type == '1':
                        self.change_amount(action, *self.espresso)
                    elif coffe_type == '2':
                        self.change_amount(action, *self.latte)
                    elif coffe_type == '3':
                        self.change_amount(action, *self.cappuccino)
                else:
                    print(f'Sorry, not enough {able}!')
        else:
            pass


if __name__ == '__main__':
    coffe_machine = CoffeMachine()
    while True:
        coffe_machine.work()
