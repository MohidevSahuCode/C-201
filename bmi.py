from tkinter import *
window = Tk()

def calculate_bmi():
    weight = int(weight_entry.get())
    height = int(height_entry.get())/100
    bmi = weight/(height*height)
    bmi = round(bmi,1)
    name = username.get()

    resut_label.destroy()
    msg=''

    if bmi <18.5:
        msg="You are underweight"
    elif bmi > 18.5 and bmi <=24.9:
        msg="is in normal range"
    elif bmi > 25 and bmi<=29.9:
        msg="You are overweight"
    elif bmi > 30:
        msg="You are obese"
    else:
        msg="Something went wrong!!!"

    output_label = Label(resut_frame,text=name+" Your BMI is "+str(bmi)+" and "+msg,bg='lightcyan',font=("calibri",12),width=42)
    output_label.place(x=20,y=40)
    output_label.pack()

window.title("BMI CALCULATOR")
window.geometry("380x400")
window.configure(bg="lightcyan")

app_label = Label(window,text="BMI Calculator",fg='black',bg='lightcyan',font=("calibri",20),bd=5)
app_label.place(x=50 , y=20)

name_label = Label(window,text="Your name",fg='black',bg='lightcyan',font=("calibri",12),bd=5)
name_label.place(x=20 , y=90)

username = Entry(window , text="", bd=2,width=22)
username.place(x=150,y=92)

height_label = Label(window,text="Enter height (cm)",fg='black',bg='lightcyan',font=("calibri",12))
height_label.place(x=20 , y=140)

height_entry = Entry(window,text="",bd=2,width=15)
height_entry.place(x=150 , y=142)

weight_label = Label(window,text="Enter weight (kg)",fg='black',bg='lightcyan',font=("calibri",12))
weight_label.place(x=20 , y=185)

weight_entry = Entry(window,text="",bd=2,width=15)
weight_entry.place(x=150 , y=187)

calculate_button = Button(window,text="CALCULATE",fg='black',bg='red',bd=4,command=calculate_bmi)
calculate_button.place(x=20 , y=250)

resut_frame = LabelFrame(window,text="Result",fg='black',bg='lightcyan',font=("calibri",12))
resut_frame.pack(padx=20,pady=20)
resut_frame.place(x=20,y=300)

resut_label = Label(resut_frame,text=" ",bg='lightcyan',font=("calibri",12),width=33)
resut_label.place(x=20,y=20)
resut_label.pack()

window.mainloop()