from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวณค่าตีแบตมินตันต่อคน')
GUI.geometry('400x250')

F1 = ttk.LabelFrame(GUI)
F1.pack()

v_hr = StringVar()
L1 = ttk.Label(F1, text='กรอกจำนวนชั่วโมง', font=('none',14))
L1.grid(column=0, row=0)
E1 = ttk.Entry(F1, textvariable=v_hr, width=7, justify='right', font=('none',16))
E1.grid(column=1, row=0)

v_ball = StringVar()
L2 = ttk.Label(F1, text='กรอกจำนวนลูกแบตที่ใช้ไปทั้งหมด', font=('none',14))
L2.grid(column=0, row=1)
E2 = ttk.Entry(F1, textvariable=v_ball, width=7, justify='right', font=('none',16))
E2.grid(column=1, row=1)

v_ppl = StringVar()
L3 = ttk.Label(F1, text='กรอกจำนวนคนที่เล่นทั้งหมด', font=14)
L3.grid(column=0, row=2)
E3 = ttk.Entry(F1, textvariable=v_ppl, width=7, justify='right', font=('none',16))
E3.grid(column=1, row=2)

L4 = ttk.Label(F1, text='ราคาที่ต้องจ่ายคนละ', font=14)
L4.grid(column=0, row=3)
E4 = ttk.Entry(F1, width=7, justify='right', font=('none',16))
E4.grid(column=1, row=3)

def calc(event=None):
	try:
		hr = float(v_hr.get())
		ball = float(v_ball.get())
		ppl = float(v_ppl.get())
		cost_per_hr = float(79)
		cost_per_ball = float(46.67)
		price = ((cost_per_hr*hr) + (cost_per_ball*ball))/ppl
		E4.insert(0, price)
	except:
		messagebox.showwarning('กรอกข้อมูลผิด','กรอกข้อมูลได้เฉพาะตัวเลข กรุณากรอกข้อมูลใหม่')
		v_hr.set('0')
		v_ball.set('0')
		v_ppl.set('0')

def clr():
	E1.delete(0, END)
	E2.delete(0, END)
	E3.delete(0, END)
	E4.delete(0, END)

B1 = ttk.Button(GUI, text='คำนวณ', command=calc)
B1.pack(ipady=5, pady=3)
B2 = ttk.Button(GUI, text='ล้างค่า', command=clr)
B2.pack(ipady=5, pady=3)

E1.bind('<Return>', calc)
E2.bind('<Return>', calc)
E3.bind('<Return>', calc) # ต้องใส่คำว่า event=None ไว้ใน function ด้วย

GUI.mainloop()