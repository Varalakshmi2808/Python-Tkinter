from tkinter import *


class miles_to_kms:
    def __init__(self, window):
        window.title('miles to kilometers')
        window.minsize(height=300, width=300)
        label = Label(window, text='Converting miles to kilometers', font=('Times new roman', 17, 'bold'), fg='blue',pady=20,padx=100)
        label.grid(row=0, column=0)

        frame = Frame(window, height=10, width=120, padx=50, pady=20, relief="ridge", bd=10)
        frame.grid(row=1, column=0)
        label = Label(frame, text='Enter miles:', width=10, padx=10, pady=10, fg='red', font=('Arial', 10))
        label.grid(row=0, column=0)
        label = Label(frame, text='miles')
        label.grid(row=0, column=2)

        self.input = Entry(frame)
        self.input.grid(row=0, column=1)

        self.km = Label(frame, text='0')
        self.km.grid(row=1, column=1)

        label = Label(frame, text='kilometers', pady=10)
        label.grid(row=1, column=2)

        label = Label(frame, text='Equals to', pady=10)
        label.grid(row=1, column=0)

        calculate = Button(frame, text='Calculate', command=self.convert, bg='green', font=('Arial', 10))
        calculate.grid(row=2, column=1, pady=10)

    def convert(self):
        miles = float(self.input.get())
        kms = round(miles * 1.609)
        self.km.config(text=f"{kms}")


class celcius_to_fahrenheit:
    def __init__(self, window):
        # window.title('miles to kilometers')
        # window.minsize(height=300,width=300)
        label = Label(window, text='Converting celsius to fahrenheit', font=('Times new roman', 17, 'bold'), fg='blue',padx=50)
        label.grid(row=0, column=1)

        frame = Frame(window, height=10, width=120, padx=50, pady=20, relief="ridge", bd=10)
        frame.grid(row=1, column=1)
        label = Label(frame, text='Enter celsius:', width=10, padx=10, pady=10, fg='red', font=('Arial', 10))
        label.grid(row=0, column=0)
        label = Label(frame, text='celsius')
        label.grid(row=0, column=2)

        self.input = Entry(frame)
        self.input.grid(row=0, column=1)

        self.km = Label(frame, text='0')
        self.km.grid(row=1, column=1)

        label = Label(frame, text='fahrenheit', pady=10)
        label.grid(row=1, column=2)

        label = Label(frame, text='Equals to', pady=10)
        label.grid(row=1, column=0)

        calculate = Button(frame, text='Calculate', command=self.c_to_f, bg='green', font=('Arial', 10))
        calculate.grid(row=2, column=1, pady=10)

    def c_to_f(self):
        c= float(self.input.get())
        f = round(c* (9/5)+32)
        self.km.config(text=f"{f}")


if __name__ == '__main__':
    window = Tk()
    obj = miles_to_kms(window)
    obj1 = celcius_to_fahrenheit(window)
    window.mainloop()
