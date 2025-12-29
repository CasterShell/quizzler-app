import tkinter

THEME_COLOR = "#375362"

from tkinter import *



class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR,pady=20,padx=20)

        #--------------- Canvas Settings ---------------------------
        self.canvas = tkinter.Canvas(background="white",height=250, width=300)
        self.question_text = self.canvas.create_text(150,125,text="some question text",
                                                     font=("arial",20,"italic"),fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image,highlightthickness=0,)
        self.true_button.grid(row=2, column= 0)
        self.false_button = Button(image=false_image,highlightthickness=0)
        self.false_button.grid(row=2,column=1)

        #------------------- score settings -----------------------
        self.score_value = 0
        self.score = tkinter.Label(text=f"Score:{self.score_value}",bg=THEME_COLOR, fg="white",
                                   font=("Arial",12,"bold"))
        self.score.grid(row = 0, column = 1,sticky="e")

        self.window.mainloop()