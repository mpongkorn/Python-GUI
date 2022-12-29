# GUI-Calculator.py

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

############# CSV #####################
import csv

def writetocsv(data):
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)

########### GUI ###################

GUI = Tk()
GUI.title('โปรแกรมเครื่อวคิดเลขแม่ค้า')
GUI.geometry('700x500')

L1 = ttk.Label(GUI, text='กรอกจำนวนกุ้ง (กิโลกรัม)', font=('none',20))
L1.pack()

v_qty = StringVar() # ตัวแปรพิเศษเอาไว้เก็บค่า
v_price = StringVar()

E1 = ttk.Entry(GUI,	 textvariable=v_qty, width=7, justify='right', font=('none',20))
E1.pack(pady=5)

L2 = ttk.Label(GUI, text='กรอกราคา (บาทต่อกิโลกรัม)', font=('none',20))
L2.pack()

E2 = ttk.Entry(GUI, textvariable=v_price, width=7, justify='right', font=('None',20))
E2.pack(pady=5)

def calc():
	print('กำลังคำนวณ...กรุณารอสักครู่')
	qty = float(v_qty.get()) # .get() ดึงข้อมูลจากตัวแปรที่เป็น StringVar แต่จะเป็นข้อความไม่ใช่ตัวเลขโดยตรง
	price = float(v_price.get())
	bath = qty*price
	messagebox.showinfo('รวมราคาทั้งหมดจากการคำนวณ', 'ต้องจ่ายเงินทั้งหมด {:,.2f} บาท'.format(bath))
	# :,.2f คือใส่ comma ทุกสามหลักและแสดงจุดทศนิยม 2 ตำแหน่ง
	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	data = ['กุ้ง', '{:,.2f}'.format(bath), dt]
	writetocsv(data)

B1 = ttk.Button(GUI, text='คำนวณ show messagebox', command=calc)
B1.pack(ipadx=10, ipady=5)

E3 = ttk.Entry(GUI, width=7, justify='right', font=('none',20))
E3.pack(pady=5)

def calc_insert():
	qty = float(v_qty.get())
	price = float(v_price.get())
	bath = qty*price
	E3.insert(0, bath)
	data = ['กุ้ง', '{:,.2f}'.format(bath)]
	writetocsv(data)

B2 = ttk.Button(GUI, text='คำนวณ insert', command=calc_insert)
B2.pack(ipadx=10, ipady=5)

def deleteText():
	E1.delete(0, END)
	#E2.delete(0, END)
	E3.delete(0, END)

B3 = ttk.Button(GUI, text='ล้างข้อมูล', command=deleteText)
B3.pack()

GUI.mainloop()
