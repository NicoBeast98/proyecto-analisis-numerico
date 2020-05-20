from tkinter import Tk, Frame, Label


# Tutorial de tkinter
# https://www.youtube.com/watch?v=V-_d5N4UJjw
class Ventana():

    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('''
Aproximacion de minimos cuadrados
        ''')
        self.raiz.config(bg='floral white')

    def main(self):
        self.frame()
        self.raiz.mainloop()

    def frame(self):
        frame = Frame()
        frame.pack(anchor='center')
        frame.config(
            bd=8,
            bg='LemonChiffon2',
            width='680',
            height='800',
            relief='groove',
            )

        Label(
            frame,
            text='Aproximador',
            bg='LemonChiffon2',
        ).place(x=20, y=20)


if __name__ == "__main__":
    ventana = Ventana()
    ventana.main()
