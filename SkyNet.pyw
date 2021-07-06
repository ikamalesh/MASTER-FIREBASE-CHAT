import json
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import pyrebase
from PIL import Image, ImageTk

firebaseConfig = {
    'apiKey': "AIzaSyBlB2OBLZU3ku6-CjGZmdsNY_ujSw5aC-U",
    'authDomain': "noted-flash-306012.firebaseapp.com",
    'databaseURL': "https://noted-flash-306012-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "noted-flash-306012",
    'storageBucket': "noted-flash-306012.appspot.com",
    'messagingSenderId': "822280810171",
    'appId': "1:822280810171:web:23bb2f142d57126afa039e"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()


class Interface():
    def __init__(self, window):
        global w, h  # 425
        w, h = 900, 600
        window.geometry(f"{w}x{h}+50+50")
        window.resizable(0, 0)
        window.title("SkyNet Messenger")
        Interface.login_page()

    def login_page():
        global img, access, entry1, entry2, color1, color2, entry1_error, entry2_error, signin
        img = ImageTk.PhotoImage(Image.open("alien_simple.png"))
        sub_y = 50
        color1, color2 = '#191919', '#EDF1F4'
        frame_login = Frame(window, bg=color2)
        frame_login.place(x=0, y=0, width=w, height=h)

        logo = Label(frame_login, image=img, bg=color2)
        logo.place(x=w / 2 - 128 / 2, y=60)

        l1 = Label(frame_login, text='SkyNet ID:', bg=color2, fg=color1, anchor='w')
        l1.place(x=w / 2 - 100, y=180 + sub_y, width=200, height=20)

        l2 = Label(frame_login, text='Password:', bg=color2, anchor='w', fg=color1)
        l2.place(x=w / 2 - 100, y=230 + sub_y, width=200, height=20)

        def element1_event(event):
            entry1_error.config(bg='grey')

        def element2_event(event):
            entry2_error.config(bg='grey')

        def login_bind(event):
            Interface.login()

        entry1_error = Label(frame_login, bd=0, bg='grey')
        entry1_error.place(x=w / 2 - 101, y=199 + sub_y, width=202, height=25)
        entry2_error = Label(frame_login, bd=0, bg='grey')
        entry2_error.place(x=w / 2 - 101, y=249 + sub_y, width=202, height=25)

        entry1 = Entry(frame_login, bd=0, relief=SOLID)
        entry1.place(x=w / 2 - 100, y=200 + sub_y, width=200, height=23)
        entry1.bind('<Button>', element1_event)
        entry1.bind('<Return>', login_bind)
        entry2 = Entry(frame_login, bd=0, relief=SOLID, show='●')
        entry2.place(x=w / 2 - 100, y=250 + sub_y, width=200, height=23)
        entry2.bind('<Button>', element2_event)
        entry2.bind('<Return>', login_bind)
        access = BooleanVar()

        remember = Checkbutton(frame_login, text='Stay signed in', anchor='w', fg=color1, activebackground=color2,
                               variable=access, bd=0, bg=color2)
        remember.select()
        remember.place(x=w / 2 - 100, y=290 + sub_y, width=200, height=23)

        forgot = Button(frame_login, text='Forgot your password?', fg='#5A6FFA', bg=color2, bd=0,
                        activeforeground='blue', command=Interface.forgot_page, activebackground=color2)
        forgot.place(x=w / 2 - 100, y=320 + sub_y, width=200, height=25)

        new = Button(frame_login, text='Get a new SkyNet ID', fg='#5A6FFA', bg=color2, bd=0, activeforeground='blue',
                     activebackground=color2, command=Interface.new_id)
        new.place(x=w / 2 - 100, y=350 + sub_y, width=200, height=25)

        signin_error = Label(frame_login, bd=0, bg='grey')
        signin_error.place(x=w / 2 - 51, y=399 + sub_y, width=102, height=27)

        signin = Button(frame_login, text='Sign In', fg='#5A6FFA', bg=color2, bd=0, activeforeground='blue',
                        activebackground=color2, command=Interface.login)
        signin.place(x=w / 2 - 50, y=400 + sub_y, width=100, height=25)

        about = Button(frame_login, text='About', bd=0, bg=color2, relief=SOLID, activebackground=color2,command=Interface.about_page)
        about.place(x=0, y=2, width=45, height=25)

        help = Button(frame_login, text='Help', bd=0, bg=color2, relief=SOLID, activebackground=color2,command=Interface.help_page)
        help.place(x=46, y=2, width=45, height=25)

        with open('cred.json') as data_file:
            data_loaded = json.load(data_file)
        if data_loaded['cred'] == True:
            entry1.insert(0, data_loaded['id'])
            entry2.insert(0, data_loaded['password'])
        else:
            pass

    def about_page():
        global img3
        frame_about = Frame(window, bg=color2)
        frame_about.place(x=0, y=0, width=w, height=h)
        back = Button(frame_about, text='Back', bd=0, bg=color2, relief=SOLID, command=frame_about.destroy,
                     activebackground=color2, fg=color1)
        back.place(x=0, y=2, width=45, height=25)

        img3 = ImageTk.PhotoImage(Image.open("space_ship.png"))
        logo = Label(frame_about, image=img3, bg=color2)
        logo.place(x=w / 2 - 128 / 2, y=60)

        l1 = Label(frame_about, text='SkyNet Messenger (10.1.0.228-in)',bg=color2, font='calibri 12',fg=color1)
        l1.place(x=w/2-200, y=200,width=400,height=25)

        l2 = Label(frame_about, text='Copyright Notices',bg=color2, font='calibri 12',fg='blue')
        l2.place(x=w/2-200, y=250,width=400,height=25)

        l3 = Label(frame_about, text='Privacy Policy', bg=color2, font='calibri 12', fg='blue')
        l3.place(x=w / 2 - 200, y=290, width=400, height=25)

        l4 = Label(frame_about, text='Terms of Service', bg=color2, font='calibri 12', fg='blue')
        l4.place(x=w / 2 - 200, y=330, width=400, height=25)

        l5 = Label(frame_about, text='© 2020-2021 SkyNet Inc. All rights reserved. (India)', bg=color2, font='calibri 12', fg=color1)
        l5.place(x=w / 2 - 200, y=h-100, width=400, height=25)

    def help_page():
        frame_help = Frame(window, bg=color2)
        frame_help.place(x=0,y=0,width=w,height=h)
        back = Button(frame_help, text='Back', bd=0, bg=color2, relief=SOLID, command=frame_help.destroy,
                     activebackground=color2, fg=color1)
        back.place(x=0, y=2, width=45, height=25)

        l1 = Label(frame_help, text='Service starting soon...', bg=color2, font='calibri 12', fg=color1)
        l1.place(x=w / 2 - 200, y=250, width=400, height=25)

    def forgot_page():
        window.title("SkyNet Messenger | Reset Password")

        def email_event(event):
            email_error.config(bg='grey')

        def bind_reset(event):
            Interface.reset_pass()

        global email_error, entry_email, send_email
        frame_forgot = Frame(window, bg=color2)
        frame_forgot.place(x=0, y=0, width=w, height=h)

        logo = Label(frame_forgot, image=img, bg=color2)
        logo.place(x=w / 2 - 128 / 2, y=60)

        l1 = Label(frame_forgot, text='Enter your Email ID:', anchor='w', fg=color1, bg=color2)
        l1.place(x=w / 2 - 100, y=180 + 50, width=200, height=20)

        email_error = Label(frame_forgot, bd=0, bg='grey')
        email_error.place(x=w / 2 - 101, y=199 + 50, width=202, height=25)

        entry_email = Entry(frame_forgot, bd=0, relief=SOLID)
        entry_email.place(x=w / 2 - 100, y=200 + 50, width=200, height=23)
        entry_email.bind('<Button>', email_event)
        entry_email.bind('<Return>', bind_reset)
        send_email_error = Label(frame_forgot, bd=0, bg='grey')
        send_email_error.place(x=w / 2 - 51, y=299, width=102, height=27)

        send_email = Button(frame_forgot, text="Send email", fg='#5A6FFA', bg=color2, bd=0, activeforeground='blue',
                            activebackground=color2, command=Interface.reset_pass)
        send_email.place(x=w / 2 - 50, y=300, width=100, height=25)

        def back_cmd2():
            window.title("SkyNet Messenger")
            frame_forgot.destroy()

        back = Button(frame_forgot, text='Back', bd=0, bg=color2, relief=SOLID, command=back_cmd2,
                      activebackground=color2, fg=color1)
        back.place(x=0, y=2, width=45, height=25)

    def login():
        signin.config(text='Checking...')
        signin.update()
        global crt_email, crt_password, empty, name_id
        username = entry1.get()
        password = entry2.get()
        crt_email = False
        crt_password = False
        empty = False
        if username != '' and password != '':
            if '@' in username:  # EMAIL ID
                email_id = username
                map_get = db.child('map').child(email_id.replace('.', '<dot>')).get().val()
                if map_get != None:
                    name_id = db.child('user_details').child(map_get).child('name').get().val()
                    # print('Email OK')
                    crt_email = True
                    # print('Checking Password')
                    try:
                        auth.sign_in_with_email_and_password(email_id, password)
                        # print('Password OK')
                        crt_password = True
                    except:
                        # print('Password NOT OK')
                        crt_password = False
                else:
                    # print('Email NOT OK')
                    crt_email = False

            else:  # SKYNET ID
                try:
                    email_id = db.child('user_details').child(username).child('email').get().val()
                    if email_id != None:
                        name_id = db.child('user_details').child(username).child('name').get().val()
                        # print('Email OK')
                        crt_email = True
                        # print('Checking Password')
                        try:
                            auth.sign_in_with_email_and_password(email_id, password)
                            # print('Password OK')
                            crt_password = True
                        except:
                            # print('Password NOT OK')
                            crt_password = False
                    else:
                        # print('Email NOT OK')
                        crt_email = False
                except:
                    crt_email = False
        else:
            empty = True

        if empty == False:
            if crt_email == True:
                entry1_error.config(bg='light green')
                if crt_password == True:
                    entry1_error.config(bg='grey')
                    entry2_error.config(bg='grey')
                    if access.get() == True:
                        line = {"cred": True, "id": username, "password": password}
                    else:
                        line = {"cred": False}
                    with open('cred.json', 'w') as f:
                        json.dump(line, f)
                    print('APPROVED')
                    print('username', name_id)
                    entry1.delete(0, END), entry2.delete(0, END)
                    Interface.main_console()
                else:
                    entry2_error.config(bg='red')
            else:
                entry1_error.config(bg='red')
        else:
            print('FILL')
        signin.config(text='Sign In')

    def reset_pass():
        email = entry_email.get()
        if email != '':
            try:
                auth.send_password_reset_email(email)
                entry_email.delete(0, END)
                email_error.config(bg='grey')
                send_email.config(fg='green', text='Sent', state=DISABLED)
            except:
                email_error.config(bg='red')
        else:
            email_error.config(bg='red')

    def main_console():
        window.title("SkyNet Messenger")
        frame_console = Frame(window, bg=color2)
        frame_console.place(x=0, y=0, width=w, height=h)
        global text_box, msg_box

        def bind_send(e):
            Interface.send()

        msg_box = Entry(frame_console, bd=1, relief=SOLID)
        msg_box.place(x=10, y=h - 25 - 20, width=w - 100, height=30)
        msg_box.bind('<Return>', bind_send)
        send_error = Label(frame_console, bd=0, bg='grey')
        send_error.place(x=w - 80 - 2, y=h - 25 - 20, width=72, height=30)

        send = Button(frame_console, text="Send", fg='green', bg=color2, bd=0, activeforeground='dark green',
                      activebackground=color2, command=Interface.send)
        send.place(x=w - 80 - 1, y=h - 25 - 19, width=70, height=28)

        scrollbar = Scrollbar(frame_console)
        text_box = Text(frame_console, height=10, width=10, yscrollcommand=scrollbar.set, bd=1, relief=SOLID, selectbackground='white',selectforeground='black',cursor='arrow')
        text_box.place(x=10, y=50, width=w - 20 - 10, height=h - 120)

        scrollbar.config(command=text_box.yview)
        scrollbar.place(x=w - 10 - 10, y=50, width=20, height=h - 120)

        def logout_cmd():
            v = messagebox.askokcancel('Confirm', 'Are you sure you want to logout now?')
            if v == True:
                my_stream.close()
                frame_console.destroy()
            else:
                pass

        def reload_cmd():
            global first_iter, my_stream
            reload.config(state=DISABLED)
            my_stream.close()
            first_iter = True
            Interface.read()
            reload.config(state=NORMAL)

        logout = Button(frame_console, text='Logout', bd=0, bg=color2, relief=SOLID, command=logout_cmd,
                        activebackground=color2, fg=color1)
        logout.place(x=10, y=2, width=50, height=25)

        reload = Button(frame_console, text='Reload', bd=0, bg=color2, relief=SOLID, command=reload_cmd,
                        activebackground=color2, fg=color1)
        reload.place(x=70, y=2, width=50, height=25)

        Interface.read()

        def on_closing():
            if messagebox.askokcancel('Confirm', 'Are you sure you want to exit now?'):
                window.destroy()
            else:
                pass
        window.protocol("WM_DELETE_WINDOW", on_closing)

    def send():
        global sent
        sent = True
        msg = msg_box.get()
        if msg != '':
            now = datetime.now()
            time = now.strftime("%H:%M %d/%m/%Y")
            final = f"{time} {f'{name_id}': >15}: {msg}"
            db.child('messages').push(final)

    def read():
        global first_iter, my_stream
        first_iter = True

        def stream_handler(message):
            global first_iter, sent
            # print('25', message)
            data = message["data"]
            # print('27', data)  # {'title': 'Pyrebase', "body": "etc..."}

            if first_iter == False:
                # print('30', data)
                text_box.config(state=NORMAL)
                text_box.insert(END, f"{data}\n")
                text_box.see(END)
                text_box.config(state=DISABLED)
                try:
                    if sent == True:
                        msg_box.delete(0, END)
                        sent = False
                    else:
                        pass
                except:
                    pass
            if first_iter == True:
                try:
                    text_box.config(state=NORMAL)
                    text_box.delete(1.0, END)
                    text_box.config(state=DISABLED)
                    for item in data:
                        # print('35', data[item])
                        text_box.config(state=NORMAL)
                        text_box.insert(END, f"{data[item]}\n")
                        text_box.see(END)
                        text_box.config(state=DISABLED)
                    first_iter = False
                except TypeError:
                    pass

        my_stream = db.child("messages").stream(stream_handler,stream_id=name_id)

    def new_id():
        global img2, aentry1_error, aentry2_error, aentry3_error, aentry4_error, aentry1, aentry2, aentry3, aentry4, asignup, asignup_error
        window.title("SkyNet Messenger | New Account")
        frame_new = Frame(window, bg=color2)
        frame_new.place(x=0, y=0, width=w, height=h)

        def back_cmd1():
            window.title("SkyNet Messenger")
            frame_new.destroy()

        back = Button(frame_new, text='Back', bd=0, bg=color2, relief=SOLID, command=back_cmd1,
                      activebackground=color2, fg=color1)
        back.place(x=0, y=2, width=45, height=25)

        img2 = ImageTk.PhotoImage(Image.open("space_ship.png"))
        logo = Label(frame_new, image=img2, bg=color2)
        logo.place(x=w / 2 - 128 / 2, y=60)

        sub_y = 50

        l1 = Label(frame_new, text='Name:', bg=color2, fg=color1, anchor='w')
        l1.place(x=w / 2 - 100, y=180 + sub_y, width=200, height=20)

        l2 = Label(frame_new, text='Email Id:', bg=color2, anchor='w', fg=color1)
        l2.place(x=w / 2 - 100, y=230 + sub_y, width=200, height=20)

        l3 = Label(frame_new, text='SkyNet ID:', bg=color2, anchor='w', fg=color1)
        l3.place(x=w / 2 - 100, y=280 + sub_y, width=200, height=20)

        l4 = Label(frame_new, text='Password:', bg=color2, anchor='w', fg=color1)
        l4.place(x=w / 2 - 100, y=330 + sub_y, width=200, height=20)

        ###############################
        def bind_1(event):
            aentry1_error.config(bg='grey')

        def bind_2(event):
            aentry2_error.config(bg='grey')

        def bind_3(event):
            aentry3_error.config(bg='grey')

        def bind_4(event):
            aentry4_error.config(bg='grey')

        aentry1_error = Label(frame_new, bd=0, bg='grey')
        aentry1_error.place(x=w / 2 - 101, y=199 + sub_y, width=202, height=25)
        aentry2_error = Label(frame_new, bd=0, bg='grey')
        aentry2_error.place(x=w / 2 - 101, y=249 + sub_y, width=202, height=25)

        aentry3_error = Label(frame_new, bd=0, bg='grey')
        aentry3_error.place(x=w / 2 - 101, y=299 + sub_y, width=202, height=25)

        aentry4_error = Label(frame_new, bd=0, bg='grey')
        aentry4_error.place(x=w / 2 - 101, y=349 + sub_y, width=202, height=25)
        ################################
        aentry1 = Entry(frame_new, bd=0, relief=SOLID)  # Name
        aentry1.place(x=w / 2 - 100, y=200 + sub_y, width=200, height=23)
        aentry1.bind('<Button>', bind_1)

        aentry2 = Entry(frame_new, bd=0, relief=SOLID, )  # Email
        aentry2.place(x=w / 2 - 100, y=250 + sub_y, width=200, height=23)
        aentry2.bind('<Button>', bind_2)
        aentry3 = Entry(frame_new, bd=0, relief=SOLID)  # SkyNetID
        aentry3.place(x=w / 2 - 100, y=300 + sub_y, width=200, height=23)
        aentry3.bind('<Button>', bind_3)
        aentry4 = Entry(frame_new, bd=0, relief=SOLID, show='●')  # Password
        aentry4.place(x=w / 2 - 100, y=350 + sub_y, width=200, height=23)
        aentry4.bind('<Button>', bind_4)
        ###############################
        asignup_error = Label(frame_new, bd=0, bg='grey')
        asignup_error.place(x=w / 2 - 51, y=424 + sub_y, width=102, height=27)

        asignup = Button(frame_new, text='Sign Up', fg='#5A6FFA', bg=color2, bd=0, activeforeground='blue',
                         activebackground=color2, command=Interface.signup)
        asignup.place(x=w / 2 - 50, y=425 + sub_y, width=100, height=25)

    def signup():
        global proceed_signup
        asignup.config(state=DISABLED, text='Signing up...')
        asignup.update()
        name = aentry1.get().title()
        emailid = aentry2.get()
        skynetid = aentry3.get()
        password = aentry4.get()
        proceed_signup = False
        if name and emailid and skynetid and password != '':
            if len(password) >= 6:  # PASSWORD OK
                aentry4_error.config(bg='grey')
                if db.child('map').child(emailid.replace('.', '<dot>')).get().val() == None:  # FRESH EMAIL
                    aentry2_error.config(bg='grey')
                    if '@' or '.com' or '.co.in' in emailid:  # Email validation
                        aentry2_error.config(bg='grey')
                        if db.child('user_details').child(skynetid).get().val() == None:  # FRESH ID
                            aentry3_error.config(bg='grey')
                            try:
                                aentry2_error.config(bg='grey')
                                auth.create_user_with_email_and_password(emailid, password)
                                db.child('map').child(emailid.replace('.', '<dot>')).set(skynetid)
                                db.child('user_details').child(skynetid).set({'email': emailid, 'name': name})
                                proceed_signup = True
                            except:
                                # print('Email Invalid')
                                aentry2_error.config(bg='red')
                        else:
                            # print('ID Exists')
                            aentry3_error.config(bg='red')
                    else:
                        # print('Email invalid')
                        aentry2_error.config(bg='red')
                else:
                    # print('Email exists')
                    aentry2_error.config(bg='red')
            else:
                # print('MIN 6 CHAR PASSWORD')
                aentry4_error.config(bg='red')
        else:
            print('FILL')

        if proceed_signup == True:
            aentry1.delete(0, END), aentry2.delete(0, END), aentry3.delete(0, END), aentry4.delete(0, END)
            asignup.config(state=DISABLED, text='Created')
        else:
            asignup.config(state=NORMAL, text='Sign Up')


if __name__ == '__main__':
    global my_stream
    window = Tk()
    app = Interface(window)
    window.mainloop()
    try:
        my_stream.close()
    except:
        pass
