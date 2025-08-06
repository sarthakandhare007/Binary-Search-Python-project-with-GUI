import tkinter as tk
from tkinter import messagebox

def binary_search_visual(arr, target):
    steps = []
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        steps.append(f"Checking middle index {mid}: {arr[mid]}")
        if arr[mid] == target:
            steps.append(f"🎯 Found {target} at index {mid}")
            return steps
        elif arr[mid] < target:
            steps.append(f"{target} > {arr[mid]} → Search right half")
            low = mid + 1
        else:
            steps.append(f"{target} < {arr[mid]} → Search left half")
            high = mid - 1
    steps.append("❌ Target not found.")
    return steps

def on_search():
    try:
        input_list = list(map(int, entry_list.get().split(',')))
        input_list.sort()
        target = int(entry_target.get())
        result = binary_search_visual(input_list, target)
        text_result.delete('1.0', tk.END)
        text_result.insert(tk.END, f"Sorted List: {input_list}\n\n")
        for line in result:
            text_result.insert(tk.END, line + "\n")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers separated by commas.")

# GUI setup
root = tk.Tk()
root.title("Binary Search Visualizer")
root.geometry("500x450")
root.config(padx=20, pady=20)

# Widgets
label_list = tk.Label(root, text="Enter sorted list (comma separated):")
label_list.pack()
entry_list = tk.Entry(root, width=50)
entry_list.pack()

label_target = tk.Label(root, text="Enter number to search:")
label_target.pack()
entry_target = tk.Entry(root, width=20)
entry_target.pack()

btn_search = tk.Button(root, text="Search", command=on_search)
btn_search.pack(pady=10)

text_result = tk.Text(root, height=15, width=60)
text_result.pack()

root.mainloop()
