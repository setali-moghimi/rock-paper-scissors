from tkinter import *
from random import *
window=Tk()
window.geometry('400x300')
window.title('sang kaghaz ghachi')
pc=0
player=0

def sang():
    global pc 
    global player
    global k
    k=randint(1, 3)
    if k==1:
        Label(window, text='nothing').pack()
    if k==2:
        pc+=1
        Label(window, text='lose', fg='red').pack()
    if k==3:
        player+=1
        Label(window, text='won', fg='green').pack()
    q.config(text='player:{} pc:{}'.format(player, pc))
def kagaz():
    global pc 
    global player
    global k
    k=randint(1, 3)
    if k==1:
        Label(window, text='won', fg='green').pack()
        player+=1
    if k==2:
        Label(window, text='nothing').pack()
    if k==3:
        pc+=1
        Label(window, text='lose', fg='red').pack()
    q.config(text='player:{} pc:{}'.format(player, pc))
def ghachi():
    global pc 
    global player
    global k
    k=randint(1, 3)
    if k==1:
        Label(window, text='lose', fg='red').pack()
        pc+=1
    if k==2:
        player+=1
        Label(window, text='won', fg='green').pack()
    if k==3:
        
        Label(window, text='nothing').pack()
    q.config(text='player:{} pc:{}'.format(player, pc))

q=Label(window ,  text='player:0 pc:0 ')
q.pack()
w=Button(window,  text='sang',  command=sang)
e=Button(window,  text='kaghaz',  command =kagaz)
r=Button (window,  text='ghachi',  command=ghachi)
w.pack()
e.pack()
r.pack()
window.mainloop()
if pc>player :
    global natije
    natije='lose'
if pc<player :
    natije='won'
if pc==player :
    natije='nothing'
o=player-pc


f=open('randemn bazy.txt',  'a')
f.write('\n pc:{}        plyer:{}       natije:{}         ekhtelaf:{}'.format(pc, player,natije,o))
f.close()




    






    


