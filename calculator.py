import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Create the display
display = tk.Entry(root, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Initialize variables
current_input = ""
first_number = None
operator = None

# Button click handlers
def number_click(num):
    global current_input
    current_input += str(num)
    display.delete(0, tk.END)
    display.insert(0, current_input)

def operator_click(op):
    global first_number, operator, current_input
    if current_input:
        first_number = float(current_input)
        operator = op
        current_input = ""
        display.delete(0, tk.END)

def calculate():
    global current_input, first_number, operator
    if first_number is not None and operator and current_input:
        second_number = float(current_input)
        try:
            if operator == "+":
                result = first_number + second_number
            elif operator == "-":
                result = first_number - second_number
            elif operator == "×":
                result = first_number * second_number
            elif operator == "÷":
                result = first_number / second_number
            display.delete(0, tk.END)
            display.insert(0, str(result))
            current_input = str(result)
        except ZeroDivisionError:
            display.delete(0, tk.END)
            display.insert(0, "Error")
            current_input = ""
        finally:
            first_number = None
            operator = None

def clear():
    global current_input, first_number, operator
    current_input = ""
    first_number = None
    operator = None
    display.delete(0, tk.END)

# Create buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 14), command=calculate)
    elif text in ["+", "-", "×", "÷"]:
        btn = tk.Button(root, text=text, font=("Arial", 14), command=lambda op=text: operator_click(op))
    else:
        btn = tk.Button(root, text=text, font=("Arial", 14), command=lambda num=text: number_click(num))
    
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Clear button
clear_btn = tk.Button(root, text="C", font=("Arial", 14), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Configure grid weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()