import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = tk.Tk()
window.title("AStext editor")
window.iconphoto(False, tk.PhotoImage(file='media/icon.png'))
window.geometry("1080x720")

textbox = tk.Text(width = 100,height = 44.5,font = 30)
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    textbox.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        textbox.insert(tk.END, text)
    window.title(f"AStext editor - {filepath}")
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = textbox.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"AStext editor - {filepath}")
buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(buttons, text="Open", command=open_file)
btn_save = tk.Button(buttons, text="Save As...", command=save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

buttons.grid(row=0, column=0, sticky="ns")
textbox.grid(row=0, column=1, sticky="nsew")

window.mainloop

