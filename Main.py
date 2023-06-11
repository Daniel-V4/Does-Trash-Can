import random

class Game():

    def __init__(self):
        self.cols = 0
        self.rows = 0
        self.board = []
        self.answers = []

    def create_board(self):
        print("Insert the number of trashcan collums [3 to 16]")
        self.cols = self.validate_input(3, 16)
        print("Insert the number of trashcan rows [3 to 16]")
        self.rows = self.validate_input(3, 16)
        self.board = ["🗑️ " for _ in range(self.cols*self.rows)]


    def update_board(self, guess):
        try: 
            guess = int(guess)
            self.board[guess-1] = "❌"
        except:
            pass
    
    def update_board_correct(self, guess):
        self.board[guess-1] = "✅"

    def print_board(self):
        for i in range(self.rows):
            row = self.board[i*self.cols:(i+1)*self.cols]
            print(' '.join(f'{element: <}' for element in row))

    def choose_answer(self):
        self.answers = []
        self.answers.append(random.randint(0, self.cols*self.rows))
        while len(self.answers) < 2:
            num = random.choice((self.answers[0] + 1, self.answers[0] - 1, self.answers[0] + self.cols, self.answers[0] - self.cols))
            if num in range(0, self.rows * self.cols) and not (self.answers[0] - num in (1, -1) and self.answers[0] // self.cols == num // self.cols):
                self.answers.append(num)
    
    def validate_input(self, min, max):
        value = 0
        while value == 0:
            try: 
                val = int(input())
            except: 
                print("invalid input")
                continue
            if (val >= min and val <= max):
                value = val
            else:
                print("invalid input")
        return value
    
    def greet(self):
        print("""   Welcome to this completely original and high (🗑️) quality puzzle minigame!!!
    The rules are simple:
    There are 2 hidden switches inside the trashcans.
    You can try to find the first one as many times as you like, but have only one shot for the second.
    The second switch is immediately up, left, right or down the first one.
    You select the trashcan inputting it's conrresponding number. Ex.:
        1  2  3
        4  5  6
        7  8  9
    If there's a switch in 3, it has to be in either 2 or 6.
            
    That said, do you really wanna play? [yes or no]""")
        aws = input()
        if aws in ("Yes", "yes", "YES", "y", "Y"):
            return True
        else:
            return False
    
    def execute(self):
        playing = self.greet()
        while playing == True:
            self.create_board()
            self.choose_answer()
            playing = self.gameplay_loop()
        else:
            print("Thank you for playing!!!")

    def gameplay_loop(self):
        phase = 0
        while phase == 0:
            self.print_board()
            print("Take your guess:")
            guess = input()
            try: guess = int(guess)
            except: continue
            if guess-1 in self.answers:
                self.update_board_correct(guess)
                self.answers.remove(guess-1)
                phase = 1
            else:
                self.update_board(guess)
                print("skill issue")
        else:
            self.print_board()
            print("Congratulations!!! Now it's your time to shine, take your final「guess」")
            guess = input()
            try: 
                guess = int(guess)
                if guess-1 in self.answers:
                    self.update_board_correct(guess)
                    self.print_board()
                    print("Congratulations squared!!! You're the epitome of intelect.")
                else:
                    self.update_board(guess)
                    self.print_board()
                    print("Git gud, no way you're gonna face that electric rat this way!")
            except:
                print("That's not even a real answer LMAO")
        print("/n Do you wanna play some more? [yes or no]")
        ending = input()
        if ending in ("yes", "YES", "y", "Y", "Yes"):
            return True
        else:
            return False
            
        




game = Game()
game.execute()
