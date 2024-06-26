from tkinter import *
from PIL import Image,ImageTk
from sentence import make_challenge


class Typer():
    def __init__(self,root):
        self.root=root
        self.root.title("Typing")
        self.root.config(padx=50,pady=30)
        self.root.geometry("750x500")
        self.setup_ui()
        
    # Small logo at the top 
    def setup_ui(self):
        self.correct_word=0
        self.second=59
        self.time=Label(text="00:00",font=("Helvetica",20))
        self.time.grid(row=0,column=10)

        self.canvas=Canvas(width=100,height=100)
        self.canvas.grid(row=1,column=1,columnspan=10,pady=20)

        self.label_section()
        self.start_button()
        self.load_image()
       
    def create_newSentece(self):
         #Random sentence selected from the sentence list
        self.challenge_sentence=make_challenge()
        #COnvert sentence to list
        self.chanllenge_list=self.challenge_sentence.split()
        return self.chanllenge_list

    def load_image(self):
        self.img=Image.open("Keyboard.svg.png")
        self.img=self.img.resize((100,100))
        self.tkimg=ImageTk.PhotoImage(self.img)
        self.canvas.create_image(100//2,100//2,image=self.tkimg)

    #Text Field for user response
    def text_field(self):
        self.start.destroy()
        self.entry=Entry(text="",width=20,font=("Helvetica", 20))
        self.entry.focus_set()
        self.entry.grid(row=self.rw+2,column=1,columnspan=10,pady=10)
        self.grid[0].config(text=self.chanllenge_list[0],wraplength=300,bg="yellow",font=("Helvetica",14))
        self.clock()
    #Start Button
    def start_button(self):
        
        self.start=Button(text="Start",command=self.text_field,width=20)
        self.start.grid(row=self.rw+1,column=1,columnspan=10,pady=10)
    #Timer scripted using after
    def clock(self):
        #Capture the keyboard entry. 
        if self.second>=0:
            try:    
                self.entry.bind("<Key>",self.user_input)
            except TclError:
                print(TclError)
            
            min,sec= divmod(self.second,60)
            if self.second <= 9:
                self.time.config(text=f"0{min}:0{sec}",font=("Helvetica",20))
            else:
                self.time.config(text=f"0{min}:{sec}",font=("Helvetica",20))
            self.second-=1
            self.root.after(1000,self.clock)
        else:
        #Score to count the number of correct words.
            self.final_score()
            
    # Check the user input from the sentence list
    def user_input(self,event):
        self.user_word=self.entry.get().strip()
        if event.keysym =="space" and len(self.chanllenge_list) > 0:
            if self.chanllenge_list[0] == self.user_word:
                self.grid[0].config(text=self.chanllenge_list[0],wraplength=300,fg="green",font=("Helvetica",14))
                self.correct_word+=1
            else:
                self.grid[0].config(text=self.chanllenge_list[0],wraplength=300,fg="red",font=("Helvetica",14))
            self.grid[0].config(text=self.chanllenge_list[0],wraplength=300,bg="white",font=("Helvetica",14))
            self.chanllenge_list.pop(0)
            self.grid.pop(0)
            self.entry.delete(0,END)  

            if len(self.chanllenge_list) > 0:
                self.grid[0].config(text=self.chanllenge_list[0],wraplength=300,bg="yellow",font=("Helvetica",14))
            else:
                for label in self.backup_grid:
                    label.destroy()
                self.label_section()
                       
    #Create label as well as captures the lable info(grid)
    def label_section(self):
        row=2
        column=1
        self.grid=[]
        self.backup_grid=[]
        self.chanllenge_list=self.create_newSentece()
        for word in self.chanllenge_list:
            label=Label(self.root,text=word,wraplength=300,font=("Helvetica",14))
            label.grid(row=row,column=column)
            column+=1
            if column ==10:
                row +=1
                column=1
            self.grid.append(label)
            self.backup_grid.append(label)
        self.rw=row
    #Dispaly the score
    def final_score(self):
        try:
            self.entry.unbind("<Key>")
            self.entry.destroy()
        except TclError:
            print(TclError)
        self.score= Label(self.root,text=f"Congratulations!!!\n Your Score: {self.correct_word} wpm",fg="green",font=("Helvetica",14,"bold","italic"))
        self.score.grid(row=self.rw+2,column=1,columnspan=10,pady=20)
        self.new=Button(self.root,text="New Text",command=self.reset,width=20)
        self.new.grid(row=self.rw+3,column=1,columnspan=10,pady=10)
            
    
    #Reset the screen and setup new screen
    def reset(self):
        self.score.destroy()
        self.new.destroy()
        self.time.destroy()
        for label in self.backup_grid:
            label.destroy()
        self.setup_ui()

    
        
        
       
        
        
        