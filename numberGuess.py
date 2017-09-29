from random import *
def guessGame():
       top = input("How hard should this be? 1-")
       rand = randint(1, top)
       game = 1
       guesses = 1
       while game:
              guess = input("What number am I thinking of? ")
              if guess == rand:
                     print "You got it in",guesses,"guesses!"
                     game = 0
              elif guess > rand:
                     print "Guess again, maybe a little less."
                     guesses += 1
              else:
                     print "Guess again, maybe a little more."
                     guesses += 1
       main()

def guessGameReverse():
       bottom = 1
       top = input("How hard should this be? 1-")
       print "Pick a number between 1 and",str(top)+"."
       game = 1
       guess = 0
       while game:
              cpuguess = int(top-(top-bottom)/2)
              print "Your number is:",cpuguess
              guess += 1
              hint = raw_input("Lower or higher? ")
              if hint == "l":
                     top = cpuguess
              elif hint == "h":
                     bottom = cpuguess
              else:
                     print "Either you cheated or I guessed it in",guess,"guesses!"
                     game = 0
       main()

def main():
       gametype = raw_input("What game do you want to play? G/R ")
       if gametype == "g":
              guessGame()
       elif gametype == "r":
              guessGameReverse()

main()
