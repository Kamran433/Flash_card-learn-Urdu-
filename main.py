import tkinter

window = tkinter.Tk()
window.title("Flash-Cards")
window.config(bg="white",height=1000,width=1000)
S = 3
urduuu = []
u = open("urdu_words.txt", "r")
for line in u:
    urduuu += line.split()
urdulist = urduuu
u.close()
englishh = []
e = open("English_meaning.txt", "r")
for linez in e:
    englishh += linez.split()
englishlist = englishh
e.close()
n = 0
score = 0
if (n == len(englishlist)):
    n = 0


    def yess(S):

        global n
        if (S == 0):
            canvas.itemconfig(langtext, text=englishlist[n])
            canvas.itemconfig(Lang, text="ENGLISH")
            n += 1
        else:
            try:
                window.after(1000, yess, S - 1)
            except TypeError:
                pass


    def no():
        canvas.itemconfig(langtext, text=urdulist[n])
        canvas.itemconfig(Lang, text="URDU")
        S = 3
        window.after(1000, yess, S - 1)


    def yes1():
        global score
        urdulist.pop(n)
        englishlist.pop(n)
        canvas.itemconfig(langtext, text=urdulist[n])
        canvas.itemconfig(Lang, text="URDU")
        S = 3
        window.after(1000, yess, S - 1)
else:
    def yess(S):
        global n
        if (S == 0):
            tick.config(text="⏳")
            canvas.itemconfig(langtext, text=englishlist[n])
            canvas.itemconfig(Lang, text="ENGLISH")
            n += 1
        else:
            try:
                window.after(1000, yess, S - 1)
                tick.config(text=S)
            except TypeError:
                pass


    def no():
        urdulist.pop(n)
        englishlist.pop(n)
        canvas.itemconfig(langtext, text=urdulist[n])
        canvas.itemconfig(Lang, text="URDU")
        S = 3
        window.after(1000, yess, S - 1)


    def yes1():
        global score
        score += 1
        sc.config(text=f"Score : {score}")
        tick.config(text="  ")
        tick.config(text="3")
        canvas.itemconfig(langtext, text=urdulist[n])
        canvas.itemconfig(Lang, text="URDU")
        S = 3
        window.after(1000, yess, S - 1)
imageshow = tkinter.PhotoImage(file="card.png")
imageyes = tkinter.PhotoImage(file="yes.png")
imageno = tkinter.PhotoImage(file="no.png")
canvas = tkinter.Canvas(width=500, height=500, highlightbackground="white")
canvas.create_image(253, 253, image=imageshow)
langtext = canvas.create_text(250, 180, text=urdulist[n], font=("Proxima Nova", 30, "italic", "bold"), fill="#6f73a5")
tdc = canvas.create_text(250, 250, text="in", font=("Proxima Nova", 30, "bold"), fill="white")
Lang = canvas.create_text(250, 320, text="URDU", font=("Proxima Nova", 30, "italic", "bold"), fill="#6f73a5")
canvas.grid(row=1, column=1,padx=20,pady=20)
no = tkinter.Button(image=imageno, command=no,pady=50,padx=50, highlightbackground="green",highlightcolor="white",
                    borderwidth=0)
yes = tkinter.Button(image=imageyes, command=yes1, pady=50,padx=50, highlightbackground="#b5b6dc", borderwidth=0,
                     bg="white")
no.grid(row=2, column=1,sticky="W")
yes.grid(row=2, column=1,sticky="E")
try:
    window.after(1000, yess, S - 1)
except TypeError:
    pass
tick = tkinter.Label(text="", bg="white", font=("Proxima Nova", 20, "italic"))
tick.grid(row=0, column=2,padx=20)
sc = tkinter.Label(text=f"Score : {score}", bg="white", font=("Proxima Nova", 20, "italic"))
sc.grid(row=0, column=0)
window.mainloop()
