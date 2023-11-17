from tkinter import *




class Btn:
    def __init__(self, text, x, y, width = 100, height = 80, bg_color = 'white') -> None:
        self.text, self.x, self.y, self.width, self.height, self.bg_color = text, x, y, width, height, bg_color
        btn = Button(text=self.text, command=lambda : click(self), border=0, font=('', 20), bg=self.bg_color)
        btn.place(x=x, y=y, width=width, height=height)


def click(btn: Btn):
    global main_input, response_label

    if btn.text not in ['AC', 'DEL', 'COPY', '=']:
        try:
            main_input.insert(END, btn.text)
        except:...
    elif btn.text == 'AC':
        main_input.delete(0, 'end')
        response_label['text'] = '0'
    elif btn.text == 'DEL':
        if len(main_input.get()) > 0:
            main_input.delete(len(main_input.get())-1)
    elif btn.text == 'COPY':
        Tk.clipboard_clear(window)
        Tk.clipboard_append(window, f'{main_input.get()} = {eval(main_input.get())}')
    elif btn.text == '=':
        try:
            
            response_label['text'] = eval(main_input.get())
        except:...
window = Tk()
window.title('Simple Calc')
window.geometry('400x500')
window.resizable(False, False)

main_input = Entry(font=('', 15))
main_input.place(x=0, y=0, width=400, height=40)

response_label = Label(text='0', font=('', 40))
response_label.place(x=0, y=40, width=300, height=60)

copy_btn = Btn('COPY', 300, 40, height=60)

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