from tkinter import *
from PIL import ImageTk, Image
confirm=[]
def appendLarge ():
    confirm.append(15)
    print(confirm)
def appendMedium ():
    confirm.append(12)
    print(confirm)
def appendSmall ():
    confirm.append(8)
    print(confirm)
def total ():
    tot=0
    for i in confirm:
        tot=tot+i 
    print(tot)
    newwindow=Toplevel(window)
    newwindow['background']='light blue'
    newwindow.title("new window")
    newwindow.geometry('500x500')
    labelnew=Label(newwindow,text='TOTAL price \n ' +str(tot)+' EGP' ,font=('calibre','18','normal'),background='light blue')
    labelnew.pack(pady=30)
    buttonNEW=Button(newwindow,text="OK",font=('calibre','17','normal'),command=newwindow.destroy)
    buttonNEW.place(x=222,y=400)
   
def OpenLarge():                     #new window for large 
    newwindow=Toplevel(window)
    newwindow['background']='khaki'
    newwindow.title("new window")
    newwindow.geometry('500x500')
    labelnew=Label(newwindow,text='Large size \n price 15 EGP',font=('calibre','15','normal'),background='khaki')
    labelnew.pack(pady=30)
    buttonLarge=Button(newwindow,text="add",font=('calibre','17','normal'),command=appendLarge )
    buttonLarge.place(x=235,y=400)
    buttonLargeDE=Button(newwindow,text="confirm",font=('calibre','17','normal'),command=newwindow.destroy)
    buttonLargeDE.place(x=215,y=450)


#new window for medium
def OpenMedium():
    newwindow=Toplevel(window)
    newwindow['background']='light yellow'
    newwindow.title("new window")
    newwindow.geometry('500x500')
    labelnew=Label(newwindow,text='Medium size \n price 12 EGP',font=('calibre','15','normal'),background='light yellow')
    labelnew.pack(pady=30)
    buttonMedium=Button(newwindow,text="add",font=('calibre','17','normal'),command=appendMedium)
    buttonMedium.place(x=235,y=400)
    buttonMediumDE=Button(newwindow,text="confirm",font=('calibre','17','normal'),command=newwindow.destroy)
    buttonMediumDE.place(x=215,y=450)
#new window for small
def OpenSmall():
    newwindow=Toplevel(window)
    newwindow['background']='light cyan'
    newwindow.title("new window")
    newwindow.geometry('500x500')
    labelnew=Label(newwindow,text='Small size \n price 8 EGP',font=('calibre','15','normal'),background='light cyan')
    labelnew.pack(pady=30)
    buttonSmall=Button(newwindow,text="add",font=('calibre','17','normal'),command=appendSmall)
    buttonSmall.place(x=235,y=400)
    buttonSmallDE=Button(newwindow,text="confirm",font=('calibre','17','normal'),command=newwindow.destroy)
    buttonSmallDE.place(x=215,y=450)
window=Tk()
window.geometry("1000x500")

#open image
#label photo
image1=Image.open("logo.png")
test=ImageTk.PhotoImage(image1)
#large photo 
imagel=Image.open("large.jpeg")
large=ImageTk.PhotoImage(imagel)
#medium photo
image2=Image.open("index.jpeg")
Medium=ImageTk.PhotoImage(image2)
#small photo
image3=Image.open("small.jpeg")
small=ImageTk.PhotoImage(image3)

#install title 
window.title("Shop")

#install label
label1=Label(window,image=test)
label1.place(x=350,y=0)
label1.image=test
label2=Label(window,text="welome to our shop",font=('calibre','20','bold'),fg="green")
label2.place(x=350,y=0)

#install 3 buttons of sizes
#large butt
button1=Button(window,image=large,command=OpenLarge)
button1.place(x=0,y=200)
#medium butt
button2=Button(window,image=Medium,command=OpenMedium)
button2.place(x=350,y=285)
#small butt
button3=Button(window,image=small,command=OpenSmall)
button3.place(x=730,y=200)

button4=Button(window,text="close and confirm",bd='6',activebackground='yellow',font=('calibre','13','normal'),command=window.destroy)
button4.place(x=850,y=455)

button5=Button(window,text="See Total price",bd='6',activebackground='purple',bg='yellow',font=('calibre','15','normal'),command=total)
button5.place(x=840,y=100)

window.mainloop()