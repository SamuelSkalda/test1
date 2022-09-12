import tkinter
canvas = tkinter.Canvas(width=600, height=300, bg='white')
canvas.pack()

pocetradov=10
VEL=40
busx, busy= 50, 50
s=[0]*40
obsadene=0
ulicka=0

def zafarbi(sedadlo,farba):
    canvas.itemconfig('sedadlo_'+str(sedadlo), fill=farba)
    
def kresli(x, y, pocet):
    cislo = 0
    for i in range(pocet):
        for j in range(4):
            cislo += 1
            canvas.create_rectangle(x+i*VEL, y+j*VEL,
                                   x+(i+1)*VEL-10, y+(j+1)*VEL-10,fill='green',
                                   tags='sedadlo_'+str(cislo))
            canvas.create_text(x+i*VEL+VEL/2-5, y+j*VEL+VEL/2-5, text=cislo)
            canvas.create_text(100, 230, text='Počet voľných: '+str(40-obsadene), tags='obs')
            canvas.create_text(107, 250, text='Počet obsadených: '+str(obsadene), tags='obs')
            canvas.create_text(100, 270, text='Počet voľných pri uličke: '+str(ulicka), tags='obs')

def klik(event):
    global obsadene
    if(busx < event.x < busx + VEL * pocetradov and
       busy < event.y < busy + VEL * 4):
        ix = (event.x - busx) // VEL
        iy = (event.y - busy) // VEL
        sedadlo = ix * 4 + iy + 1
        if s[sedadlo-1] == 0:
            zafarbi(sedadlo, 'red')
            obsadene += 1
            s[sedadlo-1] = 1
        else:
            zafarbi(sedadlo, 'green')
            obsadene -= 1
            s[sedadlo-1] = 0
    canvas.delete('obs')
    canvas.create_text(100, 230, text='Počet voľných: '+str(40-obsadene), tags='obs')
    canvas.create_text(107, 250, text='Počet obsadených: '+str(obsadene), tags='obs')
    canvas.create_text(100, 270, text='Počet voľných pri uličke: '+str(ulicka), tags='obs')

        
kresli(busx, busy, pocetradov)
canvas.bind('<Button-1>', klik)