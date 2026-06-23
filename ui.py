#importing
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from tkinter import *
from quiz_brain import QuizBrain #, sendScore
from prediction import GetData #gpa

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.gd = GetData() #gpa
        self.window = Tk()
        self.window.title("GPA Predictor")
        self.window.geometry('500x350')
        self.window.config( pady=10, padx=50, bg=THEME_COLOR)
        self.window.resizable(False, False)
        icon = PhotoImage(file="images\icon.png")
        self.window.iconphoto(False, icon)
        self.canvas = Canvas(height=200, width=400)
        self.question_text = self.canvas.create_text(180,
                                                     80,
                                                     width=350,
                                                     text="Some question text",
                                                     fill=THEME_COLOR,
                                                     font=('Helvetica',18,'bold'))
        self.canvas.grid(row=0, column=0, columnspan=4, pady=20)
        self.op_1 = Button(text=1, height=1,
                           width=2,padx=10,pady=10, font=('Helvetica',16,'bold'),
                           highlightthickness=0, command=self.op1)
        self.op_2 = Button(text=2, height=1,
                           width=2,padx=10,pady=10, font=('Helvetica',16,'bold'),
                           highlightthickness=0, command=self.op2)
        self.op_3 = Button(text=3, height=1,
                           width=2,padx=10,pady=10, font=('Helvetica',16,'bold'),
                           highlightthickness=0, command=self.op3)
        self.op_4 = Button(text=4, height=1,
                           width=2,padx=10,pady=10, font=('Helvetica',16,'bold'),
                           highlightthickness=0, command=self.op4)
        # self.nextButton = Button(text="Next", height=1,
        #                     font=('Helvetica',12,'bold'),
        #                    highlightthickness=0, command=self.destroy())
        #gpa starts
        #Definition of the components for the window
        self.hrsLabel = Label( text="Enter your hours of study per week:",font=('Helvetica',10,'bold') )
        self.gpaLabel = Label( text="Enter your last GPA:", font=('Helvetica',10,'bold'))
        self.subButton = Button( text="SUBMIT",padx=10, command=self.sub, font=('Helvetica',12,'bold'))
        self.gpaEntry = Entry(borderwidth=2,bg="#d3d7de",font=('Helvetica',10,'bold'))
        self.hrsEntry = Entry(borderwidth=2,bg="#d3d7de",font=('Helvetica',10,'bold'))
        #gpa ends
        

        self.op_1.grid(row=1, column=0)
        self.op_2.grid(row=1, column=1)
        self.op_3.grid(row=1, column=2)
        self.op_4.grid(row=1, column=3)
        # self.T_img = PhotoImage(file="images/true.png")
        # self.F_img = PhotoImage(file="images/false.png")
        # self.T_button = Button(image=self.T_img, height=100,
        #                        width=97, bg=THEME_COLOR,
        #                        highlightthickness=0, command=self.right_ans)
        # self.T_button.grid(row=2, column=0)
        # self.F_button = Button(image=self.F_img, height=100,
        #                        width=97, bg=THEME_COLOR,
        #                        highlightthickness=0, command=self.wrong_ans)
        # self.F_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.window.config(bg=THEME_COLOR)
            # self.Score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.window.config(bg=THEME_COLOR)
            self.canvas.itemconfig(self.question_text,
                                   text="You reached the end of Quiz.")
            # self.nextButton.grid(row=1, column=3)
            # self.T_button.config(state="disabled")
            # self.F_button.config(state="disabled")
            self.op_1.config(state="disabled")
            self.op_2.config(state="disabled")
            self.op_3.config(state="disabled")
            self.op_4.config(state="disabled")
            self.window.config(pady=0, padx=0,bg=THEME_COLOR)
            self.window.after(5000,self.gpa_brain())
           
        


            
            
            
    
    def op1(self):
        is_right = self.quiz.check_answer(1)
        self.feedback(is_right)

    def op2(self):
        is_right = self.quiz.check_answer(2)
        self.feedback(is_right)

    def op3(self):
        is_right = self.quiz.check_answer(3)
        self.feedback(is_right)

    def op4(self):
        is_right = self.quiz.check_answer(4)
        self.feedback(is_right)

    def feedback(self, tf):
        if tf:
            self.window.config(bg="green") #put canvas back if problem arises
        else:
            self.window.config(bg="red")

        self.window.after(1000, self.get_next_question)
    #gpa starts
    def sub(self):

        
        last_gpa = float(self.gpaEntry.get())
        study_hour = float(self.hrsEntry.get())
        print("gpa",last_gpa,"\nhrs:",study_hour)
        gpa = round(self.gd.reg.predict(self.gd.sc.transform([[last_gpa, study_hour]]))[0], 1)
        print("new gpa before adjustment: ",gpa)
        #delete from here (if needed)
        score = self.quiz.sendScore()-5 #sendScore function
        inc = abs(last_gpa-gpa)*0.2*score
        gpa+=inc
        #upto here
        if(gpa>10): gpa=10
        gpa=round(gpa,2)
        print("Predicted GPA: ", gpa if gpa <= 10 else 10)
        self.gd.error_have()
        pred = Label(self.window, text="Predicted GPA :  "+str(gpa),font=('Helvetica',12,'bold'),padx=10,pady=10)
        pred.place(x=150,y=240)
    #gpa ends

    def destroy(self):
        self.op_1.destroy()
        self.op_2.destroy()
        self.op_3.destroy()
        self.op_4.destroy()
        self.canvas.destroy()
    
    def gpa_brain(self):
         # clear window
        self.destroy()
        #gpa starts here
        # self.window.config(pady=0, padx=0, bg=THEME_COLOR)
        self.window.geometry('500x350')
        #Putting the components on the window
        self.gpaLabel.place(x=50,y=50)
        self.hrsLabel.place(x=50,y=100)
        self.subButton.place(x=210, y=170)
        self.gpaEntry.place(x=310,y=50)
        self.hrsEntry.place(x=310,y=100)
        self.window.mainloop()
        #gpa ends here

# def showQues(ques):
#     global ans
#     Question = Label(win, text=ques.text, padx=10,pady=10)
#     ans = ques.answer

# def answer(option):
#     if option == ans:
#         right()
#     else:
#         wrong()
    

# def wrong():
#     pass

# def right():
#     pass

# def op1():
#     answer(1)
# def op2():
#     answer(2)
# def op3():
#     answer(3)
# def op4():
#     answer(4)

    

 

# #Definitionof window components
# Question = Label(win, padx=10,pady=10)
# b1=Button(win, text="1",width=1, padx=10, command=op1)
# b2=Button(win, text="2",width=1, padx=10, command=op2)
# b3=Button(win, text="3",width=1, padx=10, command=op3)
# b4=Button(win, text="4",width=1, padx=10, command=op4)


# #Placing window components
# Question.place(x=60,y=50)
# b1.place(x=100,y=250)
# b2.place(x=175,y=250)
# b3.place(x=250,y=250)
# b4.place(x=325,y=250)