from tkinter import *
from tkinter.filedialog import askopenfilename
import easyocr
import cv2
from easygui import *

window = Tk()
icon = '../data/images/logo.ico'


def choice_and_output_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print(filename)

    destroy_window(window)

    img = cv2.imread(filename, 0)
    reader = easyocr.Reader(['fr', 'en'])
    results = reader.readtext(img)

    L = list()

    for result in results:
        L.append(result[1])

    print(L)

    window1 = Tk()
    window1.geometry('800x600')
    window1.title('My Application')
    window1.minsize(480, 360)
    window1.config(background='#4065A4')
    window1.iconbitmap(icon)


    ma_variable = StringVar()
    lab = Label(window1, text='Pays : '+L[5]+' '+L[6])
    lab.place(x=200, y=250)
    lab1 = Label(window1, text='Type de piece : ' + L[12])
    lab1.place(x=200, y=26)

    button = Button(window1, text='Valider', font=('Verdana', 15, 'bold'), fg='white', bg='blue', command=save)
    button.place(x=200,y=400)

    window1.mainloop()


def save():
    print('sauvegarde OK')

def destroy_window(window):
    window.destroy()


window.geometry('800x600')
window.title('My Application')
window.minsize(480, 360)
window.config(background='#4065A4')  # window['bg'] = 'gray' | #41B77F->Vert claire
window.iconbitmap(icon)

frame = Frame(window, bg='#4065A4')

w = 400
h = 250
lab_title = Label(frame, text='DATA EXTRACTION IN IMAGE', font=('Helvetica', 20, 'bold'), bg='#4065A4', fg='#FFFFFF')
lab_title.pack()
img = PhotoImage(file='../data/images/home.png').zoom(35).subsample(32)
canvas = Canvas(frame, width=w, height=h, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(w/2, h/2, image=img)
canvas.pack()
button = Button(frame, text='Choisir un fichier', font=('Verdana', 15, 'bold'), fg='white', bg='blue', command=choice_and_output_file)
button.pack()
frame.pack(expand=YES)

window.mainloop()



