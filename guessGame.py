import random
import tkinter
from tkinter import *

class Guess(Frame):

    def __init__(self,master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.guesses=0
        self.number = random.randint(1, 101)
        print(self.number)

    def create_widgets(self):
        Label(self, text="Choose a number from 1 to 100.").grid(row=0, column=0, sticky=W)
        Label(self, text="Try and guess it .... U have only 5 chances..").grid(row=1, column=0, sticky=W)

        Label(self, text="Take a guess:").grid(row=2, column=0, sticky=W)
        self.guess_num = Entry(self)
        self.guess_num.grid(row=2, column=1, sticky=W)

        Label(self, text="Press submit if you are sure!!!").grid(row=3, column=0, sticky=W)
        Button(self, text="Submit", command=self.run_game).grid(row=3, column=1, sticky=W)

        self.text = Text(self, width=75, height=10, wrap=WORD)
        self.text.grid(row=4, column=0, columnspan=4)

    def run_game(self):

            guess = int(self.guess_num.get())
            self.guesses += 1

            if guess != self.number:
                print_text = "You guessed {0}.".format(guess)
                if guess < self.number:
                    print_text += "Your guess is less than the number  .. :(  Try Again"

                elif guess > self.number:
                    print_text += "Your guess is more than the number  .. :(  Try Again"



                if self.guesses ==6:
                    print_text = "Sorry..... U are not able to guess the number .. :(.. Play again to pick up the number"
                    self.text.delete(0.0, END)
                    self.text.insert(0.0, print_text)
                else:
                    self.text.delete(0.0, END)
                    self.text.insert(0.0, print_text)
                    self.guess_num.delete(0, END)





            else:
                guesses = str(self.guesses)
                print_text = "Your guess is correct :) "
                print_text += "You guessed it in **" + guesses + "** chance.."
                self.text.delete(0.0, END)
                self.text.insert(0.0, print_text)










root=Tk()
root.title("Guess my number game!")
app =Guess(root)
root.mainloop()


