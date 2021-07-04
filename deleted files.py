def reset_pass():
    email = entry_email.get()
    if email != '':
        try:
            auth.send_password_reset_email(email)
            entry_email.delete(0, END)
            send_email.config(fg='green', text='Sent', state=DISABLED)
        except:
            email_error.config(bg='red')
    else:
        email_error.config(bg='red')


def join_create():
    global img1, img2, frame_chat
    frame_chat = Frame(window, bg=color2)
    frame_chat.place(x=0, y=0, width=w, height=h)
    sub_y = 200
    img1 = ImageTk.PhotoImage(Image.open("hi.png"))
    img1_l = Label(frame_chat, image=img1, bg=color2)
    img1_l.place(x=20, y=h - 150)

    img2 = ImageTk.PhotoImage(Image.open("ship.png"))
    img2_l = Label(frame_chat, image=img2, bg=color2)
    img2_l.place(x=w - 200, y=-20)

    Label(frame_chat, bd=0, bg='grey').place(x=w / 2 - 51, y=49 + sub_y, width=102, height=27)

    join = Button(frame_chat, text='Join Chatroom', bg=color2, bd=0, command=Interface.join)
    join.place(x=w / 2 - 50, y=50 + sub_y, width=100, height=25)

    Label(frame_chat, bd=0, bg='grey').place(x=w / 2 - 61, y=99 + sub_y, width=122, height=27)

    create = Button(frame_chat, text='Create Chatroom', bg=color2, bd=0, command=Interface.create)
    create.place(x=w / 2 - 60, y=100 + sub_y, width=120, height=25)

    logout = Button(frame_chat, text='Logout', bd=0, bg=color2, relief=SOLID, command=frame_chat.destroy,
                    activebackground=color2, fg='tomato')
    logout.place(x=5, y=2, width=45, height=25)


def join():
    frame_join = Frame(frame_chat, bg=color2, bd=1, relief=SOLID)
    frame_join.place(x=-2, y=220, width=w + 4, height=220)

    close = Button(frame_join, text='❌', command=frame_join.destroy, bd=0)
    close.place(x=w - 25, y=5)

    l1 = Label(frame_join, text='Room ID:', anchor='w', bg=color2, fg=color1, )
    l1.place(x=w / 2 - 100, y=50, width=200, height=20)

    entry_roomid = Entry(frame_join, bd=1, relief=SOLID)
    entry_roomid.place(x=w / 2 - 100, y=70, width=200, height=23)

    join_error = Label(frame_join, bd=0, bg='grey')
    join_error.place(x=w / 2 - 51, y=139, width=102, height=27)

    join = Button(frame_join, text="Join", fg='#5A6FFA', bg=color2, bd=0, activeforeground='blue',
                  activebackground=color2)
    join.place(x=w / 2 - 50, y=140, width=100, height=25)


def create():
    frame_create = Frame(frame_chat, bg=color2, bd=1, relief=SOLID)
    frame_create.place(x=-2, y=220, width=w + 4, height=220)

    close = Button(frame_create, text='❌', command=frame_create.destroy, bd=0)
    close.place(x=w - 25, y=5)

    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    room_id = choice(alp) + choice(alp) + choice(alp) + choice(alp) + choice(alp)

    l1 = Label(frame_create, text=room_id, bg=color2, fg=color1, font='arial 25', anchor='center')
    l1.place(x=w / 2 - 100, y=50, width=200, height=28)

    copy_error = Label(frame_create, bd=0, bg='grey')
    copy_error.place(x=w / 2 - 36, y=99, width=72, height=27)

    copy = Button(frame_create, text="Copy", fg='dark grey', bg=color2, bd=0, activeforeground='grey',
                  activebackground=color2)
    copy.place(x=w / 2 - 35, y=100, width=70, height=25)

    create_error = Label(frame_create, bd=0, bg='grey')
    create_error.place(x=w / 2 - 51, y=144, width=102, height=27)

    create = Button(frame_create, text="Enter", fg='#5A6FFA', bg=color2, bd=0, activeforeground='blue',
                    activebackground=color2)
    create.place(x=w / 2 - 50, y=145, width=100, height=25)