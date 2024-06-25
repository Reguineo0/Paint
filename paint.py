import base64
from tkinter import *
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageDraw

# Datos de la imagen del ícono en base64 (código abreviado)
icon ="""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"""

# Variables globales
color = 'black'
Width = 600
Height = 440

# Decodificar el ícono en formato PhotoImage
icondata = base64.b64decode(icon)
root = Tk()

# Funciones
def save():
    filename = filedialog.asksaveasfilename(
        initialfile="untitled.png", defaultextension=".png", filetypes=[("PNG files", "*.png")]
    )
    if filename:
        image.save(filename)

def change_color(c):
    global color
    color = c

def pick_color():
    global color
    picked = colorchooser.askcolor()[1]  # Seleccionar solo el código hexadecimal
    if picked:
        color = picked

def drawing(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval((x1, y1, x2, y2), fill=color, outline=color, width=vertical.get())
    draw.rectangle([x1, y1, x2 + vertical.get(), y2 + vertical.get()], outline=color, fill=color, width=vertical.get())

def on_closing():
    answer = messagebox.askyesnocancel("QUIT", "DO YOU WANT TO SAVE YOUR WORK?", parent=root)
    if answer is not None:
        if answer:
            save()
        root.destroy()

def new_canvas():
    canvas.delete('all')
    draw.rectangle([0, 0, Width, Height], fill='white')

# Configuración de la ventana principal
root.title("Paint")
root.geometry(f"{Width}x{Height+100}")
root.resizable(False, False)
root.wm_iconphoto(True, PhotoImage(data=icondata))

# Menú
menu_bar = Menu(root)
root.config(menu=menu_bar)
submenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New Canvas', command=new_canvas)
submenu.add_command(label='Save', command=save)

# Frames y widgets
frame = Frame(root)
frame.pack(fill='x')

color_frame = Frame(frame)
color_frame.pack(side='left', padx=10)

buttons = [
    ('black', 'grey', 'brown', 'orange', 'yellow', 'red', 'green', 'turquoise', 'indigo', 'purple', 'blue'),
    ('white', 'lime', 'pink', 'gold', 'cyan')
]

for i, row in enumerate(buttons):
    for j, color_name in enumerate(row):
        Button(color_frame, bg=color_name, width=3, command=lambda col=color_name: change_color(col)).grid(row=i, column=j, padx=2, pady=2)

vertical = Scale(frame, from_=1, to=20, orient=HORIZONTAL, label='Size', length=200)
vertical.pack(side='left', padx=10)

Button(frame, text='Erase', command=lambda: change_color('white')).pack(side='left', padx=10)
Button(frame, text='Color', command=pick_color).pack(side='left', padx=10)

canvas = Canvas(root, bg='white', width=Width, height=Height)
canvas.pack(fill='both', expand=True)
canvas.bind('<B1-Motion>', drawing)

# Imagen y dibujo
image = Image.new("RGB", (Width, Height), "white")
draw = ImageDraw.Draw(image)

# Centrar ventana
root.update()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Manejo de cierre de ventana
root.protocol("WM_DELETE_WINDOW", on_closing)

# Ejecutar la interfaz
root.mainloop()