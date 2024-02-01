from tkinter import *
import random

attempts = 10
answer = random.randint(1,100)

def check_answer():
    global attempts
    global text
    attempts -= 1
    guess = int(entry_window.get())
    if answer == guess:
        text.set("You win! Congrats!")
        btn_check.pack_forget()
    elif attempts == 0:
        text.set("You are out of attempts!")
        btn_check.pack_forget()
    elif guess < answer:
        text.set("Incorrect! Guessed number is low \n you have "+str(attempts)+" attempts remaining - Go Higher!")
    elif guess > answer:
        text.set("Incorrect! Guessed number is high \n you have "+str(attempts)+" attempts remaining - Go Lower! ")

root = Tk()
root.title("Guess The Number")
root.geometry("500x300")

heading = Label(root, text = "Lets play the game!", font=("Helvetica", 15, "bold"))
heading.pack()

label = Label(root, text="Guess a number between 1 to 100")
label.pack()

entry_window = Entry(root, width=10, border=10, font=("lucida", 30,"bold"), bg = "blue", fg = "white")
entry_window.pack(pady=10)

btn_check = Button(root, text="Check", width = 7, height = 1, font=("lucida", 11), bg= "green", fg = "white", command=check_answer)
btn_check.pack(pady=10)

btn_quit = Button(root, text="Quit", width = 7, height = 1, font=("lucida", 11), bg = "red", fg = "white", command=root.destroy)
btn_quit.pack(pady=10)

text = StringVar()
text.set("You have 10 attempts remaining! Goodluck!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()
