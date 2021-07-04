import tkinter

parent_widget = tkinter.Tk()


def check(e):
    v = listbox_widget.get(tkinter.ANCHOR)
    print(v)


listbox_entries = ["Entry 1", "Entry 2",
                   "Entry 3", "Entry 4"]
listbox_widget = tkinter.Listbox(parent_widget, activestyle='none', cursor='hand2')
listbox_widget.selection_anchor(0)
listbox_widget.bind('<<ListboxSelect>>', check)

for entry in listbox_entries:
    listbox_widget.insert(tkinter.END, entry)

listbox_widget.pack()
tkinter.mainloop()
