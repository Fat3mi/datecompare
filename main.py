#  پروژه مقایسه دو زمان باهم - توسعه نرم افزار - استاد مریم مقیمی - سید امید فاطمی

#============ Import ==============>
from tkinter import *
from jdatetime import *
import datetime as dt


#============ color Palette ==============>
c1 = '#1C0C5B' #Background
c2 = '#3D2C8D'
c3 = '#916BBF'
c4 = '#C996CC' #Font

#============ Functions ==============>

def Hide_cont():
    """ Hide Context Entries """
    context2.pack_forget()

def show_cont():
    """ Show Context Entries """
    context2.pack(side=TOP, fill="x")


def calculate():
    """ Calculate Age , Date Diffrence , Jalali To Gregorian And Gregorian To Jalali """
    try:
        ent_year = int(date1_ent.get())
        ent_month =  int(date2_ent.get())
        ent_day = int(date3_ent.get())
        ent_year2 = int(date1_ent2.get())
        ent_month2 =  int(date2_ent2.get())
        ent_day2 = int(date3_ent2.get())

    except ValueError:
        resault_dis.configure(text=" ! لطفاً کادر تاریخ را پر نمایید")

    if v.get() == 1:

        if ent_year > ent_year2 :
            d2 = dt.datetime(ent_year,ent_month,ent_day)
            d1 = dt.datetime(ent_year2,ent_month2,ent_day2)
            differ = d2.year - d1.year - ((d2.month, d2.day) < (d1.month, d1.day))
            res = (d2 - d1).days
            resault_dis.configure(text=f"اختلاف دوتاریخ مساوی با {differ} سال یا به عبارتی {res} روز است  ")
        else:
            d1 = dt.datetime(ent_year, ent_month, ent_day)
            d2 = dt.datetime(ent_year2, ent_month2, ent_day2)
            differ = d2.year - d1.year - ((d2.month, d2.day) < (d1.month, d1.day))
            res = (d2 - d1).days
            resault_dis.configure(text=f"اختلاف دوتاریخ مساوی با {differ} سال یا به عبارتی {res} روز است  ")

    elif v.get() == 2:

        if ent_year <= 1402:
            today = date.today()
            age = today.year - ent_year - ((today.month, today.day) < (ent_month, ent_day))
            resault_dis.configure(text=f"سن شما {age} است  ")
        elif ent_year >= 1402:
            today = dt.date.today()
            age = today.year - ent_year - ((today.month, today.day) < (ent_month, ent_day))
            resault_dis.configure(text=f"سن شما {age} است  ")
        else:
            resault_dis.configure(text="لطفاً کادر تاریخ را پر نمایید !")

    elif v.get() == 3:

        if ent_year <= 1402:
            resault_dis.configure(text="تاریخ را به میلادی وارد کنید ")
        else:
            miladi = date.fromgregorian(day=ent_day, month=ent_month, year=ent_year)
            resault_dis.configure(text=miladi)

    elif v.get() == 4:

        if ent_year <= 1402:
            shamsi = date(day=ent_day, month=ent_month, year=ent_year).togregorian()
            resault_dis.configure(text=shamsi)
        else:
            resault_dis.configure(text="تاریخ را به شمسی وارد کنید ")

#============== Window configuration ================>
window = Tk()
window.title("مقایسه دو تاریخ")
window.geometry("500x600")
window.resizable(width=False,height=False)
window.configure(bg=c1)
v =IntVar()

#================= Header ================>
Header_text = Frame(window , bg=c1)
Header_text.pack( side=TOP)

header = Label(Header_text,bg=c1 ,text="مقایسه دو تاریخ با هم ",fg=c4,font=("ariel",20,"bold"))
header.pack(side=TOP)

header_txt = Label(Header_text,bg=c1 ,text="ازبین گزینه های زیر یکی را انتخاب کنید ",fg=c4,font=("ariel",13,"bold"))
header_txt.pack(side=TOP)

#================= Radio Buttons ================>

header_rbtn = Frame(window, bg=c1)
header_rbtn.pack(side=TOP)

space1 = Label(header_rbtn , bg=c1)
space1.pack(side=TOP)

rbtn1 = Radiobutton(header_rbtn,text="محاسبه سن",bg=c1,fg=c4, command=Hide_cont , variable=v , value=2)
rbtn1.pack(side=RIGHT)

rbtn2 = Radiobutton(header_rbtn,text="مقایسه دو تاریخ",bg=c1,fg=c4 , command=show_cont , variable=v , value=1)
rbtn2.pack(side=RIGHT)

rbtn3 = Radiobutton(header_rbtn,text="تبدیل به شمسی",bg=c1,fg=c4 , command=Hide_cont , variable=v , value=3)
rbtn3.pack(side=RIGHT)

rbtn4 = Radiobutton(header_rbtn,text="تبدیل به میلادی",bg=c1,fg=c4 , command=Hide_cont , variable=v , value=4)
rbtn4.pack(side=RIGHT)

#================= Context ================>
context = Frame(window,bg=c2)
context.pack(side=TOP,fill="x")

context_txt = Label(context,bg=c2 ,text="تاریخ را وارد کنید ",fg=c4,font=("ariel",13,"bold"))
context_txt.pack(side=TOP)

context_entry = Frame(window,bg=c2)
context_entry.pack(side=TOP,fill="x")

date1 = Label(context,text="سال",bg=c2,fg=c4)
date1.pack(side=LEFT)

date1_ent = Entry(context,fg=c3)
date1_ent.pack(side=LEFT)

date2 = Label(context,text="ماه",bg=c2,fg=c4)
date2.pack(side=LEFT)

date2_ent = Entry(context,fg=c3)
date2_ent.pack(side=LEFT)

date3 = Label(context,text="روز",bg=c2,fg=c4)
date3.pack(side=LEFT)

date3_ent = Entry(context,fg=c3)
date3_ent.pack(side=LEFT)

#=================Context2================>

context2 = Frame(window,bg=c2 )
context2.pack(side=TOP,fill="x")

context_txt2 = Label(context2,bg=c2 ,text="تاریخ دوم ",fg=c4,font=("ariel",13,"bold"))
context_txt2.pack(side=TOP)

context_entry2 = Frame(window,bg=c2)
context_entry2.pack(side=TOP,fill="x")

date1_2 = Label(context2,text="سال",bg=c2,fg=c4)
date1_2.pack(side=LEFT)

date1_ent2 = Entry(context2,fg=c3)
date1_ent2.pack(side=LEFT)

date2_2 = Label(context2,text="ماه",bg=c2,fg=c4)
date2_2.pack(side=LEFT)

date2_ent2 = Entry(context2,fg=c3)
date2_ent2.pack(side=LEFT)

date3_2 = Label(context2,text="روز",bg=c2,fg=c4)
date3_2.pack(side=LEFT)

date3_ent2 = Entry(context2,fg=c3)
date3_ent2.pack(side=LEFT)

#================= Submit Button ================>

context_btn = Frame(window,bg=c2, height= 25)
context_btn.pack(side=BOTTOM,fill="x")

space = Label(context_btn,bg=c2)
space.pack(side=TOP)

ct_btn= Button(context_btn,text= "محاسبه" ,width=20 , bg=c2 , fg=c4 , command = calculate )
ct_btn.pack(side=TOP)

space = Label(context_btn,bg=c2)
space.pack(side=TOP)


gap = Frame(window,height=12, bg=c1)
gap.pack(side=BOTTOM)


#================= Resault Frame ================>

resault = Frame(window)
resault.pack(side=BOTTOM)

resault_dis = Label(resault,text="",width=46 , height=16 , bg=c3,font=("ariel",13,"bold"))

resault_dis.pack(side=BOTTOM)

window.mainloop()


# 1402/01/23 ~ SeyyedOmidFatemi® ~