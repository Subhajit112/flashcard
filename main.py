from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")

current_word={}


def word_selection():
    global current_word
    current_word = random.choice(to_learn)
    current_card = current_word["French"]
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card, fill = "black")
    canvas.itemconfig(front, image=card_front)
    window.after(3000, flipcard)


def flipcard():
    current_english = current_word["English"]
    canvas.itemconfig(front, image= card_back)
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_english, fill = "white" )
    canvas.itemconfig(front, image=card_back)



window = Tk()
window.title("Flash Cards")
window.config(padx=50 , pady=50, bg=BACKGROUND_COLOR)



card_front = PhotoImage(file = "images/card_front.png")
card_back = PhotoImage(file = "images/card_back.png")
card_right = PhotoImage(file = "images/right.png")
card_wrong = PhotoImage(file = "images/wrong.png")



canvas = Canvas(height=563, width=800)
front= canvas.create_image(400,263, image = card_front)
card_title = canvas.create_text(400,150,text= "title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263,text= "word", font=("Ariel", 60, "italic"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row = 0, column= 0, columnspan= 2)



right_button = Button(image= card_right, highlightthickness=0, command= word_selection)
right_button.grid(row= 1, column=0)
cancel_button = Button(image= card_wrong, highlightthickness=0, command= word_selection)
cancel_button.grid(row= 1, column=1)


word_selection()


window.mainloop()
