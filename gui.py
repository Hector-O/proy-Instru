import tkinter as tk
import serial

textos = [  "./img/poli1.png",
            "Proyecto de Instrumentación",
            "./img/escom1.png", 
            "Se detectó movimiento a:",
            "./img/apagado.png",
            f"Instrumentación\n José Luis Hernandéz Aguilar",
            f"Héctor Manuel García Osorio\nJuan Manuel González Rodríguez\n3CV11"
        ]
color_fondo="gainsboro"
bytes = b'\x00'
serialcomm = serial.Serial("COM3", 9600)

ventana = tk.Tk()
ventana.config(bg=color_fondo)

ventana.title("Sensor de movimiento Piroeléctrico 3CV11")
ventana.config(width=550, height=500)

for i in range(4):
    ventana.rowconfigure(i, weight=1, minsize=50)

for i in range(3):
    ventana.columnconfigure(i, weight=1, minsize=75)

cont = 0
prueba = 1


def handle_enter(event):
    if serialcomm.in_waiting:
        bytes = serialcomm.read()
        
        entero = int.from_bytes(bytes, "big")
        valor = (-0.0203030303*(entero-12)+4)+0.9
        #porcentaje=4/valor
        #final=100*porcentaje

        frame = tk.Frame(master=ventana, relief=tk.RAISED, borderwidth=0)
        frame.config(bg=color_fondo) 
        frame.grid(row=1, column=0, padx=5, pady=5, columnspan=3)
        label = tk.Label(master=frame, text=f"{textos[3]} {valor} voltaje", anchor="e")
        label.config(bg=color_fondo)
        label.pack(padx=5, pady=5)

ventana.bind("<Enter>", handle_enter)


frame = tk.Frame(master=ventana, relief=tk.RAISED, borderwidth=0)
frame.config(bg=color_fondo)
img = tk.PhotoImage(file=f"{textos[cont]}")
label_img= tk.Label(frame, image=img)
label_img.config(width=200, height=150, bg=color_fondo)
frame.grid(row=0, column=0, padx=5, pady=5)
cont=cont+1
label_img.pack(padx=5, pady=5)

frame = tk.Frame(master=ventana, relief=tk.RAISED, borderwidth=0)
frame.config(bg=color_fondo)
frame.grid(row=0, column=1, padx=5, pady=5)
label = tk.Label(master=frame, text=f"{textos[cont]}")
label.config(bg=color_fondo)
cont=cont+1
label.pack(padx=5, pady=5)

frame = tk.Frame(master=ventana, relief=tk.RAISED, borderwidth=0)
frame.config(bg=color_fondo)
img1 = tk.PhotoImage(file=f"{textos[cont]}")
label_img1= tk.Label(frame, image=img1)
label_img1.config(width=200, height=150, bg=color_fondo)
frame.grid(row=0, column=2, padx=5, pady=5)
cont=cont+1
label_img1.pack(padx=5, pady=5)

cont=cont+1


frame = tk.Frame(master=ventana, relief=tk.RAISED, borderwidth=1)
frame.config(bg="darkgray")
img2 = tk.PhotoImage(file=f"{textos[cont]}")
label_img1= tk.Label(frame, image=img2)
label_img1.config(width=250, height=250, bg=color_fondo)
frame.grid(row=2, column=0, padx=5, pady=5, columnspan=3, )
cont=cont+1
label_img1.pack(padx=5, pady=5)

frame = tk.Frame(master=ventana, relief=tk.RAISED, borderwidth=0)
frame.config(bg=color_fondo)
frame.grid(row=3, column=0, padx=5, pady=5, columnspan=1)
label = tk.Label(master=frame, text=f"{textos[cont]}")
label.config(bg=color_fondo)
cont=cont+1
label.pack(padx=5, pady=5, side=tk.RIGHT)

frame = tk.Frame(master=ventana, relief=tk.RAISED, borderwidth=0)
frame.config(bg=color_fondo)
frame.grid(row=3, column=2, padx=5, pady=5, columnspan=1)
label = tk.Label(master=frame, text=f"{textos[cont]}")
label.config(bg=color_fondo)
cont=cont+1
label.pack(padx=5, pady=5, side=tk.LEFT)


i=0
frame = tk.Frame(master=ventana, relief=tk.RAISED, borderwidth=0)
frame.config(bg=color_fondo) 
frame.grid(row=1, column=0, padx=5, pady=5, columnspan=3)
label = tk.Label(master=frame, text=f"{textos[3]} {i} voltaje", anchor="e")
label.config(bg=color_fondo)
cont=cont+1
label.pack(padx=5, pady=5)


ventana.mainloop()