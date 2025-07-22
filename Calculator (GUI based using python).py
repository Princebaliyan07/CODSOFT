import tkinter as tk
from tkinter import messagebox

#Function to perform calculation
def calculate():
    try:
#Get values from user 
        no1 = float(entry1.get())
        no2= float(entry2.get())
        op = operation.get()

# Now after getting both values from user He/She Perform the selected operation and will get result
        if op == '+':
            result = no1 + no2
        elif op == '-':
            result = no1 - no2
        elif op == '*':
            result = no1 * no2
        elif op == '/':
            if no2 == 0:
                messagebox.showerror("Error" , "that num1 Cannot divide by zero or Undefined.")
                return
            result = no1 / no2
        else:
            messagebox.showerror("Error" , "that invalid operation selected.")
            return

# Displaying the result
        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


#Now Creating main application window(GUI).............
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x215")

#for user inputs
tk.Label(root, text="Please Enter first number :").grid(row=0,column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0,column=1)

tk.Label(root, text="     Please Enter second number:").grid(row=1,column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1,column=1)
#for operations
tk.Label(root, text="Select operation:").grid(row=2,column=0)
operation = tk.StringVar(root)
operation.set("+")
tk.OptionMenu(root, operation, "+", "-", "*", "/").grid(row=2,column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3,columnspan=2)
#And for result display
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=2)

root.mainloop()