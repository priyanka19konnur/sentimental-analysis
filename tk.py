import tkinter as tk
def handler():
	name=box.get()
	label.config(text=f"Hello {name}")

root=tk.Tk()
box=tk.Entry(root)
btn=tk.Button(root,text="submit",fg="yellow",bg="red",command=handler)
box.grid(row=0,column=0)
btn.grid(row=0,column=1)
label=tk.Label(root,text="")
label.grid(row=1,column=0)
root.mainloop()