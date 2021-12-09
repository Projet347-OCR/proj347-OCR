from tkinter import *


# def sayHello():
#     print("Bonjour")
# 
# 
# def save():
#     lab['text'] = ma_variable.get()


# tk._test()
fenetre = Tk()
fenetre.geometry('800x600')
fenetre.title('Hello world')
fenetre['bg'] = 'red'
fenetre.resizable(height=False,width=False)

# label = Label(fenetre, text='Hello Word', font=('Verdana', 20, 'italic bold'), fg='white', bg='red')
# label.place(x=200,y=200)
# ma_variable = StringVar()
# lab = Label(fenetre, text='text modifiable')
# lab.place(x=200,y=250)
# entree = Entry(fenetre, textvariable=ma_variable)
# entree.place(x=200,y=300)
# button = Button(fenetre, text='Valider', font=('Verdana', 15, 'bold'), fg='white', bg='blue', command=save)
# button.place(x=200,y=400)
#
# mon_menu = Menu(fenetre)
#
# fichier = Menu(mon_menu, tearoff=0)
# fichier.add_command(label='Save', command=sayHello)
# fichier.add_command(label='Save As...')
# fichier.add_command(label='Quit')
#
# options = Menu(mon_menu, tearoff=0)
# options.add_command(label='Options')
#
# mon_menu.add_cascade(label='Fichier', menu=fichier)
# mon_menu.add_cascade(label='Repertoire')
# mon_menu.add_cascade(label='Options', menu=options)
#
# fenetre.config(menu=mon_menu)
#
# box = Frame(fenetre, bg='green')
# lab1 = Label(box, text='un texte')
# lab1.pack()
# lab2 = Label(box, text='un texte')
# lab2.pack()
#
# box.pack(expand=YES)

photo = PhotoImage(file='/data/images/(1)carte_identite3.jpg')
labp = Label(fenetre, image=photo)
labp.pack()

fenetre.mainloop()


