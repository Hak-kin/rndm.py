import random
import time
import winsound
from tkinter import *
from playsound import playsound

with open('rand.txt', 'r') as f:
    array = []
    for row in f:
        array.append(row.strip())


def img(event):
    global b1, b2
    j = 10
    random.shuffle(array)
    for i in range(j):
        song = 'blip.wav'
        winsound.PlaySound(song, winsound.SND_FILENAME)
        b1 = PhotoImage(file=(array[i]))
        lab1['image'] = b1
        root.update()
        if i <= j - 4:
            time.sleep(0.005)
        else:
            time.sleep(0.15)

        if i == j-1:
            delimiter1 = '/'
            delimiter2 = '.'
            sndfile = array[i]
            sndfile = sndfile.split(delimiter1)
            sndfile[0] = 'snd'
            sndfile = delimiter1.join(sndfile)
            sndfile = sndfile.split(delimiter2)
            sndfile[1] = 'mp3'
            sndfile = delimiter2.join(sndfile)
            playsound(sndfile)
    return 0


root = Tk()
root.geometry('400x200')
root.title(random.choice(['Воля Закака!', 'Да вы издевайтесь!', 'В этом совершенно нет смысла...', 'Рандом - вот что я люблю!',
                          'Ready to die?', 'Какое-то стасянство', 'Не зря учил Python... не зря ведь?',
                          'Ручечка бы написала лучше =з=', 'А мы не забыли покормить Тею?']))
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='img/icon.png'))
root.bind('<1>', img)
font = PhotoImage(file='img/back.png')
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.5, rely=0.5, anchor=CENTER)
img('event')
root.mainloop()
