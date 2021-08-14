############################## VARIABLE
score= 0
miss= 0
timeleft=60
SliderWord =''
count= 0

words=["Mango","ice Cream","BMW","CaterPillar","rudest.","First,Project.","Misspell","What?","<Major>",
"pharaoh","#Twitter","Weird.","Intelligence","Pronunciation","Handkerchief","logorrhea","Chiaroscurist","Weird",
"Intelligence","Pronunciation","Handkerchief","logorrhea","Chiaroscurist"]


# FUNCTION for slideing label
def label_slider():
    global count,SliderWord
    text="At last you took decision to increase your speed !!"
    if (count >=len(text)):
        count=0
        SliderWord=''
    SliderWord += text[count]
    count += 1
    Heading_Label.configure(text=SliderWord)
    Heading_Label.after(70,label_slider)

# Function for starting game
def StartGame(event):
    global score,miss
    
    if(timeleft==60):
        time()

    if (Box1.get()==WordLabel['text']):
        score += 1
        ScoreLabel.configure(text=score)
        HittingEnter_Label.configure(text=" ") 
    else: 
        miss+= 1
    random.shuffle(words)
    WordLabel.configure(text=words[0])
    Box1.delete(0,END)

# Function for remaining time
def time():
    global timeleft,score, miss
    if(timeleft > 0):
        timeleft -= 1
        Time_Label.configure(text=timeleft)
        Time_Label.after(1000,time)

    else:
        HittingEnter_Label.configure(text="correct = {} | Miss = {} | Total Score = {} ".format(score,miss,score-miss))
        rr=messagebox.askretrycancel("Notification","To play again hit RETRY")
        if (rr == True):
            ScoreLabel=0
            timeleft = 60
            miss=0
            Time_Label.configure(text=timeleft)
            WordLabel.configure(text=words[0])
            ScoreLabel.configure(text=score)

         

# IMPORTING Required libraries
from tkinter import *
import random
from tkinter import messagebox
 
# GUI Code
root= Tk()
root.title("Typing speed increser")
root.geometry("800x600+400+100")
root.configure(bg="light yellow")
root.iconbitmap("D:/dj.ico")



#Main  LABEL
Heading_Label=Label(root,text=" ",font=("airal",17,"bold"),
bg="light yellow",width= 40   )
Heading_Label.place(x=130,y=20)
label_slider()

# Our Score label
YourScore_label= Label(root,text="Your score",font=("blade runner",20,"italic bold"),bg="light yellow")
YourScore_label.place(x=55,y=75)

#Time left label
TimeLeft_label=Label(root,text="Time left",font=("blade runner",20,"italic bold"),bg="light yellow")
TimeLeft_label.place(x=600,y=75)

# calling function and label for words
random.shuffle(words)
WordLabel= Label(root,text=words[0],font=("airal",30,"bold"),bg="light yellow")
WordLabel.place(x=310,y=210)

# Label to say type word and hit enter
HittingEnter_Label=Label(root,text="Type word and Hit enter.",font=('airal',20,"bold"),bg="light yellow")
HittingEnter_Label.place(x=220,y=340)

#Label for our score
ScoreLabel=Label(root,text=score,font=("arial",20,"italic bold"),bg="light yellow")
ScoreLabel.place(x=105,y=110)

#label
Time_Label=Label(root,text=timeleft,font=("arial",20,"bold"),bg="light yellow")
Time_Label.place(x=640,y=110)

# ENTRY BOX
Box1=Entry(root,font=("bladerunner",25),bd=3,justify="center")
Box1.place(x=200,y=266)
Box1.focus_set()

# LOOP
root.bind("<Return>",StartGame)
root.mainloop()

#END