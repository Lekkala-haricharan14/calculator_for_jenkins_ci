import tkinter as tk
from calculator import add, subtract, multiply, divide

def calculate(operation):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

app = tk.Tk()
app.title("Simple Python Calculator")

tk.Label(app, text="Enter number 1:").pack()
entry1 = tk.Entry(app)
entry1.pack()

tk.Label(app, text="Enter number 2:").pack()
entry2 = tk.Entry(app)
entry2.pack()

tk.Button(app, text="Add", command=lambda: calculate("add")).pack()
tk.Button(app, text="Subtract", command=lambda: calculate("subtract")).pack()
tk.Button(app, text="Multiply", command=lambda: calculate("multiply")).pack()
tk.Button(app, text="Divide", command=lambda: calculate("divide")).pack()

result_label = tk.Label(app, text="Result: ")
result_label.pack()

app.mainloop()
