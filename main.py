from tkinter import *
from tkinter import messagebox
from tkinter import ttk


root = Tk()
root.title("Calculator")
#logic
def calc(key):
	global memory
	if key == "=":
		strl = "-+0123456789.*/"
		if calc_entru.get()[0] not in strl:
			calc_entru.insert(END, "Error")
			messagebox.showerror("Error", "Error")
#exclusion
		try:
			result = eval(calc_entru.get())
			calc_entru.insert(END, "=" + str(result))
		except :
			calc_entru.insert(END, 'Error')
			messagebox.showerror("Error")
#clear
	elif key == "C":
		calc_entru.delete(0, END)
#-/+
	elif key == "-/+":
		if "=" in calc_entru.get():
			calc_entru.delete(0, END)
		try:
			if calc_entru.get()[0] == "-":
				calc_entru.delete(0)
			else:
				calc_entru.insert(0, "-")
		except IndexError:
			pass
		else:
			if "=" in calc_entru.get():
				calc_entru.delete(0, END)
			calc_entru.insert(END, key)
			
#button
bttn_list = [
	"7","8","9","+","-",
	"4","5","6","*","/",
	"1","2","3","-/+","=",
	"0",".","C","",""
] 
r = 1
c = 0

for i in bttn_list:
	rel = ""
	cmd = lambda x=i: calc(x)
	ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
	c += 1
	if c > 4:
		c = 0
		r += 1

calc_entru = Entry(root, width=35)
calc_entru.grid(row=0, column=0,columnspan=5)

root.mainloop()
