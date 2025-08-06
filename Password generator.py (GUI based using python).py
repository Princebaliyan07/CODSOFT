import tkinter as tk
import random
import string

# This function runs when the button is clicked
def generate_password():
# Get the number from the user
    length = length_entry.get()

# Check if input is a number
    if not length.isdigit():
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Please enter a number")
        return

    length = int(length)
    if length <=3:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Too Short number entered please enter number more than 2")
        return

# Make a list of characters to choose from
    all_characters = string.ascii_letters + string.digits 

# Create the password
    password = ""
    for _ in range(length):
        password += random.choice(all_characters)

# Show the password in the entry box
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

#Now Creating main application window(GUI)............
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x200")

# Label for instructions
label = tk.Label(window, text="ENTER THE PASSWORD LENGTH:")
label.pack(pady=10)

# Entry box to type the length
length_entry = tk.Entry(window)
length_entry.pack()

# Button to generate the password
generate_button = tk.Button(window, text="GENERATE THE PASSWORD", command=generate_password)
generate_button.pack(pady=10)

# Entry box to show the result
result_entry = tk.Entry(window, width=60)
result_entry.pack(pady=5)

window.mainloop()
