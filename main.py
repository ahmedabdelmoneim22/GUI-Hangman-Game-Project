import random
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py;
from hangman_words import word_list
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
end_of_game = False
lives = 6
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
display = []
for _ in range(word_length):
    display += "_"
#while not end_of_game:
def GUESS():
    global lives
    #guess = input("Guess a letter: ").lower()
    guess = str(TheEntry.get())
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    #if guess in display:
    #    print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        #print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        liveLabel.configure(text=f"Lives:{lives}")
        if lives == 0:
            #end_of_game = True
            #print("You lose.")
            theEndResult.configure(text="You Lose",fg="red",background="white")
            TheButton.configure(state="disabled")
    # Join all the elements in the list and turn it into a String.
    #print(f"{' '.join(display)}")
    theresultLabel.configure(text=f"{' '.join(display)}")
    # Check if user has got all letters.
    if "_" not in display:
        #end_of_game = True
        #print("You win.")
        theEndResult.configure(text="You Win",fg="green",background="white")
        TheButton.configure(state="disabled")
    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    #print(stages[lives])
    stageslabel.configure(text=f"{stages[lives]}")
########################
import tkinter as tk
mainWindow = tk.Tk()
mainWindow.config(background="#696969")
mainWindow.title("Hangman Game")
mainWindow.geometry("265x500")
titleLabel = tk.Label(mainWindow, text="Guessing Word Game",
                      font=("Helvetica", 16, "bold"), width=20, background="#696969", fg="white")
titleLabel.grid(row=0, column=0, columnspan=2)
title2Label = tk.Label(mainWindow, text="Find the hidden word",
                       font=("Helvetica", 8, "bold"), background="#696969", fg="white")
title2Label.grid(row=1, column=0, columnspan=2)
from hangman_art import stages
# print(stages[6])
stageslabel = tk.Label(mainWindow, text=f"{stages[6]}",
                       font=("Helvetica", 16, "bold"), width=20, background="#696969", fg="red")
stageslabel.grid(row=2, column=0, columnspan=2)
liveLabel = tk.Label(mainWindow, text=f"Lives:{lives}",
                     font=("Helvetica", 8, "bold"), background="#696969")
liveLabel.place(x=200, y=60)
theresultLabel = tk.Label(mainWindow, text=f"----------------------",
                          font=("Helvetica", 12, "bold"), background="#696969")
theresultLabel.grid(row=3, column=0, columnspan=2)
ButtonLabel = tk.Label(mainWindow, text="Enter The Letter:",
                       font=("Helvetica", 12, "bold"), background="#696969")
ButtonLabel.grid(row=4, column=0, columnspan=2)
TheEntry = tk.Entry(mainWindow, font=("Helvetica", 8, "bold"), background="white")
TheEntry.grid(row=5, column=0, columnspan=2)
TheButton = tk.Button(mainWindow, text="Guess",
                      font=("Helvetica", 12, "bold"), background="#696969", width=11, command=GUESS)
TheButton.grid(row=6, column=0, columnspan=2)
theEndResult = tk.Label(mainWindow, text="--",
                        font=("Helvetica", 16, "bold"), width=20, background="#696969")
theEndResult.grid(row=7, column=0, columnspan=2)
mainWindow.resizable(False, False)
mainWindow.mainloop()
#####################
#####################



