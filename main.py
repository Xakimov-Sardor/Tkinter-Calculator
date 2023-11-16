from tkinter import *




class Btn:
    def __init__(self, text, x, y, width = 100, height = 80) -> None:
        self.text, self.x, self.y, self.width, self.height = text, x, y, width, height
        btn = Button(text=self.text, command=lambda : click(self))
        btn.place(x=x, y=y, width=width, height=height)


def click(btn: Btn):
    global main_input, response_label

    if btn.text not in ['AC', 'DEL']:
        try:
            main_input.insert(END, btn.text)
            response_label['text'] = eval(main_input.get())
        except:...
    elif btn.text == 'AC':
        main_input.delete(0, 'end')
        response_label['text'] = '0'

    elif btn.text == 'DEL':
        main_input.delete(len(main_input.get())-1)
        response_label['text'] = eval(main_input.get())
window = Tk()
window.title('Simple Calc')
window.geometry('400x500')

main_input = Entry()
main_input.place(x=0, y=0, width=400, height=40)

response_label = Label(text='0', font=('', 40))
response_label.place(x=0, y=40, width=400, height=60)

btn_ac = Btn('AC', 0, 100, width=200)
btn_bck = Btn('DEL', 200, 100)
btn_div = Btn('/', 300, 100)

btn_7 = Btn('7', 0, 180)
btn_8 = Btn('8', 100, 180)
btn_9 = Btn('9', 200, 180)
btn_mul = Btn('*', 300, 180)

btn_4 = Btn('4', 0, 260)
btn_5 = Btn('5', 100, 260)
btn_6 = Btn('6', 200, 260)
btn_dec = Btn('-', 300, 260)

btn_1 = Btn('1', 0, 340)
btn_2 = Btn('2', 100, 340)
btn_3 = Btn('3', 200, 340)
btn_dec = Btn('-', 300, 340)

btn_0 = Btn('0', 0, 420)
btn_point = Btn('.', 100, 420)
btn_equal = Btn('=', 200, 420, width=200)


window.mainloop()