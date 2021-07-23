from tkinter import *

color1_text = '#191919'
color2_litegrey = '#EDF1F4'
from PIL import Image, ImageTk
from pathlib import Path


def on_closing():
    create_button.config(state=NORMAL)
    window_create.destroy()


ASSETS_PATH = Path(__file__).resolve().parent / "assets"

window_create = Tk()
w1,h1 = 500,300
sub_y = 0
window_create.geometry(f'{w1}x{h1}')
window_create.protocol("WM_DELETE_WINDOW", on_closing)
window_create.title('Create Room')
frame_create = Frame(window_create, bg=color2_litegrey)
frame_create.place(x=0, y=0, width=500, height=300)

l1 = Label(window_create, text='Room Title:', anchor='w', bg=color2_litegrey, fg=color1_text, ).place(x=w / 2 - 100,
                                                                                                      y=30 + sub_y,
                                                                                                      width=200,
                                                                                                      height=20)
l2 = Label(window_create, text='Password:', anchor='w', bg=color2_litegrey, fg=color1_text, )

entry1_error = Label(window_create, bd=0, bg='grey')
entry1_error.place(x=w / 2 - 101, y=49 + sub_y, width=202, height=25)

entry1 = Entry(window_create, bd=0, relief=SOLID)
entry1.place(x=w / 2 - 100, y=50 + sub_y, width=200, height=23)

entry2_error = Label(window_create, bd=0, bg='grey')

entry2 = Entry(window_create, bd=0, relief=SOLID)


def fun():
    if password.get():  # True
        pass_option.config(image=lock_img)
        l2.place(x=w / 2 - 100, y=80 + sub_y, width=200, height=20)
        entry2_error.place(x=w / 2 - 101, y=99 + sub_y, width=202, height=25)
        entry2.place(x=w / 2 - 100, y=100 + sub_y, width=200, height=23)
        create_main_error.place(x=w / 2 - 51, y=149 + sub_y, width=102, height=27)
        create_main.place(x=w / 2 - 50, y=150 + sub_y, width=100, height=25)
    else:  # False
        pass_option.config(image=lockopen_img)
        l2.place(x=- 1000, y=80 + sub_y, width=200, height=20)
        entry2_error.place(x=- 1001, y=99 + sub_y, width=202, height=25)
        entry2.place(x=- 1000, y=100 + sub_y, width=200, height=23)
        create_main_error.place(x=w / 2 - 51, y=99 + sub_y, width=102, height=27)
        create_main.place(x=w / 2 - 50, y=100 + sub_y, width=100, height=25)


lock_img = Image.open(ASSETS_PATH / "lock.png")
lock_img = lock_img.resize((30, 30))
lock_img = ImageTk.PhotoImage(lock_img)

lockopen_img = Image.open(ASSETS_PATH / "lock_open.png")
lockopen_img = lockopen_img.resize((30, 30))
lockopen_img = ImageTk.PhotoImage(lockopen_img)

password = BooleanVar()
pass_option = Checkbutton(frame_create, image=lockopen_img, anchor='w', fg='black',
                          activebackground=color2_litegrey, activeforeground='black',
                          variable=password, bd=0, bg=color2_litegrey, command=fun)
pass_option.place(x=w / 2 + 82, y=sub_y + 45, width=50, height=30)

create_main_error = Label(frame_create, bd=0, bg='grey')
create_main_error.place(x=w / 2 - 51, y=99 + sub_y, width=102, height=27)
create_main = Button(frame_create, text='Sign Up', fg='#5A6FFA', bg=color2_litegrey, bd=0, activeforeground='blue',
                     activebackground=color2_litegrey)
create_main.place(x=w / 2 - 50, y=100 + sub_y, width=100, height=25)

window_create.mainloop()
