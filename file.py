import tkinter as tk
import webbrowser
root=tk.Tk()

root.geometry("500x400")
root.title("My tkinter program")

def callback(url):
    webbrowser.open_new(url)

def home_page():
    home_frame=tk.Frame(main_frame)
    lb=tk.Label(home_frame,text="I like this code because\n it is my first real procet,\n copy and paste"     ,font=("Bold",20))
    lb.pack()
    
    lb1=tk.Label(home_frame,text="link"  ,fg="blue"  ,font=("Bold",9))
    lb1.pack()
    lb1.bind("<Button-1>",lambda e: callback("https://github.com/ziyaisayev/carculyator"))
    home_frame.pack(pady=20)

def menu_page():
    menu_frame=tk.Frame(main_frame)
    lb=tk.Label(menu_frame,text="it takes color from the\n picture and give\n HEX code ",font=("Bold",20))
    lb.pack()
    
    
    lb1=tk.Label(menu_frame,text="link",fg="blue"    ,font=("Bold",9))
    lb1.pack()
    lb1.bind("<Button-1>",lambda e: callback("https://github.com/ziyaisayev/color-picker"))
    menu_frame.pack(pady=20)
def contact_page():
    contact_frame=tk.Frame(main_frame)


    lb2=tk.Label(contact_frame,text="do you ever seen paint\n in python Look, if you want try get photos\n in the github",font=("Bold",15))
    lb2.pack()

    
    lb1=tk.Label(contact_frame,text="link"    ,fg="blue",font=("Bold",9))
    lb1.pack()
    lb1.bind("<Button-1>",lambda e: callback("https://github.com/ziyaisayev/paint-in-python"))
    
    
    contact_frame.pack(pady=20)

def about_page():
    about_frame=tk.Frame(main_frame)
    lb=tk.Label(about_frame,text="PLEASE LIKE CODES IN THE GITHUB",font=("Bold",16))
    lb.pack()
    about_frame.pack(pady=20)

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def hide_indicate():
    home_indicate.config(bg="#c3c3c3")
    menu_indicate.config(bg="#c3c3c3")
    contact_indicate.config(bg="#c3c3c3")
    about_indicate.config(bg="#c3c3c3")

def indicate(lb,page):
    hide_indicate()
    lb.config(bd=0,bg="#158aff")
    delete_pages()
    page()

options_frame=tk.Frame(root,bg="#c3c3c3")
home_btn=tk.Button(options_frame,text="Carculatior",font=("Bond",13),fg="#158aff",bd=0,bg="#c3c3c3",command= lambda: indicate(home_indicate,home_page))
home_btn.place(x=10,y=50)

home_indicate=tk.Label(options_frame,text="",bd=0,bg="#c3c3c3")
home_indicate.place(x=3,y=50,width=5,height=40)

menu_btn=tk.Button(options_frame,text="color picker",font=("Bond",13),fg="#158aff",bd=0,bg="#c3c3c3",command= lambda: indicate(menu_indicate,menu_page))
menu_btn.place(x=10,y=100)
menu_indicate=tk.Label(options_frame,text="",bd=0,bg="#c3c3c3")
menu_indicate.place(x=3,y=100,width=5,height=40)

contact_btn=tk.Button(options_frame,text="paint",font=("Bond",13),fg="#158aff",bd=0,bg="#c3c3c3",command= lambda: indicate(contact_indicate,contact_page))
contact_btn.place(x=10,y=150)
contact_indicate=tk.Label(options_frame,text="",bd=0,bg="#c3c3c3")
contact_indicate.place(x=3,y=150,width=5,height=40)

about_btn=tk.Button(options_frame,text="you must",font=("Bond",13),fg="#158aff",bd=0,bg="#c3c3c3",command= lambda: indicate(about_indicate,about_page))
about_btn.place(x=10,y=200)
about_indicate=tk.Label(options_frame,text="",bd=0,bg="#c3c3c3")
about_indicate.place(x=3,y=200,width=5,height=40)
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(True)
options_frame.configure(width=100,height=400)






main_frame=tk.Frame(root,highlightbackground="black",highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(True)
main_frame.configure(width=500,height=400)

lb2=tk.Label(main_frame,text="About Me",font=("Roman",30))
lb2.place(x=100,y=100)

root.mainloop()