from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}


try:
    data = pandas.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
else:
    to_learn = data.to_dict(orient="records")



def get_new_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    my_new_word = random.choice(to_learn)
    current_word = my_new_word
    print(current_word)
    canvas.itemconfig(canvas_image, image = front_img)
    canvas.itemconfig(language, text ="French", fill = "black")
    canvas.itemconfig(guess_word, text = current_word["French"], fill = "black")
    flip_timer = window.after(2000, flip_card)



def flip_card():
    #global current_word
    #print(current_word)
    canvas.itemconfig(canvas_image, image = back_img)
    canvas.itemconfig(language, text ="English", fill = "white")
    canvas.itemconfig(guess_word, text = current_word["English"], fill = "white")

def remove_word():
    to_learn.remove(current_word)
    print(len(to_learn))
    get_new_word()
    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/to_learn.csv", index=False)




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(2000, flip_card)


canvas = Canvas(width=800,height=526,highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400,263, image=front_img)
language = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
guess_word = canvas.create_text(400, 263, text="trouve", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=get_new_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)


get_new_word()


window.mainloop()
