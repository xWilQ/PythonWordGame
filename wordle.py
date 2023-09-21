import tkinter as tk
import random as random
from tkinter import font

window = tk.Tk()
window.geometry("400x500") #Set the size of the window
window.title("Wordle.py")
dir = 'words.txt'
file1 = open(dir, "r") #Open the file with the words in it. (The file must be in the same folder as the script.)
Lines = file1.readlines() #Read list into Lines variable
 
word = Lines[random.randint(0, len(Lines)-1)].strip() #Takes a random word from the list
#print(word) #print the word to the console for testing purposes

userInput = ""
guessNum = 1
letterCount = 0
squares = []
wrongLetter = []

startLabel = tk.Label(text="Guess the word!", font=font.Font(size=24), fg="black")
startLabel.pack(padx=5, pady=5)

gridFrame = tk.Frame(master=window)
gridFrame.pack()

infoFrame = tk.Frame(master=window)
infoFrame.pack()

def Backspace(event):
    global letterCount
    global userInput
    if letterCount == 0: return

    userInput = userInput[:-1]
    letterCount -= 1
    squares[letterCount].config(text="?")
    squares[letterCount].config(bg="black")
    
     
def KeyPress(event):
    
    global letterCount
    global userInput
    
    if letterCount <= 4 and event.char.isalpha() == True:
        squares[letterCount].config(text=event.char.upper())
        
        if event.char in wrongLetter:
            squares[letterCount].config(bg="darkgrey")
        userInput = userInput + event.char
        letterCount += 1
    else : return

def Enter(event):
    
    global guessNum
    global userInput
    
    if letterCount < 5: return
    
    if userInput == word: #Check if the user input matches the word.
        Win()
        return
    
    for i in range(len(userInput)):
        
        #Checks if any of the letters the user inputed are in the word.
        if userInput[i] in word:
            squares[i].config(bg="yellow")
        else: 
            squares[i].config(bg="darkgrey")
            wrongLetter.append(userInput[i])

        #Checks if the letter happens to be in the right place in the word.
        if userInput[i] == word[i]:
            squares[i].config(bg="green")

    userInput = "" #Reset the user input
    guessNum += 1 #Adds another row of squares,
    if guessNum >= 6: #If the user has guessed 5 times, end the game.
        EndGame()
        return
    else:CreateSquares()


def CreateSquares():
    
    global letterCount
    letterCount = 0
    squares.clear()
    
    for i in range(5):
        square = tk.Label(master=gridFrame, text="?", font=font.Font(size=24), fg="white", bg="black",width=2, height=1)
        square.grid(row=guessNum, column=i, padx=5,pady=5, sticky="nsew")
        squares.append(square)

CreateSquares()

def EndGame():
    label = tk.Label(master=infoFrame, text="the word was " + word, font=font.Font(size=24), fg="black")
    label.pack()
    replayBtn = tk.Button(master=infoFrame, text="Play again", font=font.Font(size=14), width=10, relief="raised")
    replayBtn.pack(padx=5, pady=5)
    replayBtn.bind("<ButtonPress-1>", RestartGame)

def Win():
    label = tk.Label(master=infoFrame, text="You won!", font=font.Font(size=24), fg="black")
    label.pack()
    replayBtn = tk.Button(master=infoFrame, text="Play again", font=font.Font(size=14), width=10, relief="raised")
    replayBtn.pack(padx=5, pady=5)
    replayBtn.bind("<ButtonPress-1>", RestartGame)
    for i in range(len(word)):
        squares[i].config(bg="green")

def RestartGame(event):
    global guessNum
    global userInput
    global letterCount
    global squares
    global word
    
    for widget in gridFrame.winfo_children():
        widget.destroy()
    
    for widget in infoFrame.winfo_children():
        widget.destroy()
    
    guessNum = 1
    userInput = ""
    letterCount = 0
    squares.clear()
    wrongLetter.clear()
    word = Lines[random.randint(0, len(Lines)-1)].strip()
    CreateSquares()


window.bind("<Key>", KeyPress)
window.bind("<Return>", Enter)
window.bind("<BackSpace>", Backspace)
window.mainloop()