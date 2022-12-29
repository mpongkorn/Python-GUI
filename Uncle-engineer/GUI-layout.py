
from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('GUI layout using Python')
GUI.geometry('800x600')

#pack
L1 = ttk.Label(GUI,text='Hello this is pack', font='None,20')
L1.pack()

#place
L2 = Label(GUI, text='Hello this is place', font='none,0')
L2.place(x=400, y=100)

# Never mix grid and pack in the same master window
# https://stackoverflow.com/questions/23584325/cannot-use-geometry-manager-pack-inside

#grid
# using grid and pack in the same master window, you have to use Frame
F1 = ttk.LabelFrame(GUI) #มีกรอบรอบเฟรมที่สร้างขึ้น
F1.place(x=250, y=300)

#F1 = Frame(GUI)
#F1.place(x=250, y=300)

L3 = Label(F1, text='Hello this is grid-1', font='None,20', bg='red') #bg=backgrounf คือสีพื้นหลัง
L3.grid(column=0, row=0)

L4 = Label(F1, text='Hello this is grid-2', font='None,20',fg='red') #fg=foreground คือสีตัวหนังสือ
L4.grid(column=2, row=0)

L5 = Label(F1, text='Hello this is grid-3', font='None,0', bg='blue')
L5.grid(column=3, row=1)

GUI.mainloop()

# .pack .place .grid
# Lable แสดงข้อความในโปรแกรม
# Entry สร้างช่องกรอกข้อมูล
# StingVar ตัวแปรพิเศษใช้เก็บข้อมูลใน GUI