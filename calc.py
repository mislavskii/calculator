import tkinter as tk


def get_values():
    return map(
        float, (number1_entry.get(), number2_entry.get())
    )


def output_result(result):
    result_entry.delete(0, 'end')
    result_entry.insert(0, result)


def add():
    num1, num2 = get_values()
    output_result(num1 + num2)


def sub():
    num1, num2 = get_values()
    output_result(num1 - num2)


def mul():
    num1, num2 = get_values()
    output_result(num1 * num2)


def div():
    num1, num2 = get_values()
    output_result(num1 / num2)


ACTIONS = {'+': add, '-': sub, '*': mul, '/': div}
BUTTON_PARAMS = {'width': 3, 'height': 2}
Y = 200
X0 = 83
BUTTON_SPACE = 50
ENTRY_WIDTH = 30

window = tk.Tk()
window.title('Calculator')
window.geometry('350x350')
window.resizable(False, False)

buttons = [tk.Button(window, text=action, command=ACTIONS[action], **BUTTON_PARAMS) for action in ACTIONS]
[button.place(x=(X0 + BUTTON_SPACE * i), y=Y) for button, i in zip(buttons, range(len(ACTIONS)))]
# map(lambda button, i: button.place(x=(X0 + BUTTON_SPACE * i), y=Y), buttons, range(len(ACTIONS)))

# button_add = tk.Button(window, text='+', command=add, **BUTTON_PARAMS)
# button_add.place(x=X0, y=Y)
# button_sub = tk.Button(window, text='-', command=sub, **BUTTON_PARAMS)
# button_sub.place(x=X0 + BUTTON_SPACE, y=Y)
# button_mul = tk.Button(window, text='*', command=mul, **BUTTON_PARAMS)
# button_mul.place(x=X0 + BUTTON_SPACE * 2, y=Y)
# button_div = tk.Button(window, text='/', command=div, **BUTTON_PARAMS)
# button_div.place(x=X0 + BUTTON_SPACE * 3, y=Y)

number1_entry = tk.Entry(window, width=ENTRY_WIDTH)
number1_entry.place(x=X0, y=75)
number1_label = tk.Label(window, text='Enter the first number:')
number1_label.place(x=X0, y=50)

number2_entry = tk.Entry(window, width=ENTRY_WIDTH)
number2_entry.place(x=X0, y=150)
number2_label = tk.Label(window, text='Enter the second number:')
number2_label.place(x=X0, y=125)

result_entry = tk.Entry(window, width=ENTRY_WIDTH)
result_entry.place(x=X0, y=300)
result_label = tk.Label(window, text='Result:')
result_label.place(x=X0, y=275)

window.mainloop()
