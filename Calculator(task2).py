import tkinter as tk

def on_click(button_value):
    current_text = entry.get()
    
    if button_value == 'C':
        entry.delete(0, tk.END)
    elif button_value == '=':
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, 'Error')
    else:
        entry.insert(tk.END, button_value)


root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 24), bd=5, insertwidth=14, bg='lightgray', justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 1, 4)
]

for button in buttons:
    text, row, col, *args = button
    button = tk.Button(root, text=text, padx=10, pady=10, font=('Arial', 14), command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, sticky="nsew")
    button.config(bg='lightyellow', fg='black')

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)
    
root.mainloop()

