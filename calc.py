import tkinter as tk

ACTIONS = ('+', '-', '*', '/')
BUTTON_PARAMS = {'width': 3, 'height': 2}
Y = 200
X0 = 83
BUTTON_SPACE = 50
ENTRY_WIDTH = 30

window = tk.Tk()
window.title('Calculator')
window.geometry('350x350')
window.resizable(False, False)

buttons = [tk.Button(window, text=action, **BUTTON_PARAMS) for action in ACTIONS]
[button.place(x=(X0 + BUTTON_SPACE * i), y=Y) for button, i in zip(buttons, range(len(ACTIONS)))]
# map(lambda button, i: button.place(x=(X0 + BUTTON_SPACE * i), y=Y), buttons, range(len(ACTIONS)))

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

# button_add = tk.Button(window, text='+', **BUTTON_PARAMS)
# button_add.place(x=X0, y=Y)
# button_sub = tk.Button(window, text='-', **BUTTON_PARAMS)
# button_sub.place(x=X0+BUTTON_SPACE, y=Y)
# button_mul = tk.Button(window, text='*', **BUTTON_PARAMS)
# button_mul.place(x=X0+BUTTON_SPACE*2, y=Y)
# button_div = tk.Button(window, text='/', **BUTTON_PARAMS)
# button_div.place(x=X0+BUTTON_SPACE*3, y=Y)

window.mainloop()
