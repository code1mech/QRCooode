from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage


class Qr_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator | Developed by Harshit Mangla")
        self.root.resizable(False, False)

        title = Label(self.root, text="  QR Code Generator", font=("times new roman", 40), bg='#053246', fg='white',
                      anchor='w').place(x=0, y=0, relwidth=1)

        # ****** Student Details Window ****
        # ******Variables****************
        self.var_stu_code = IntVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()

        stu_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        stu_Frame.place(x=50, y=100, width=500, height=380)
        stu_title = Label(stu_Frame, text="Student Details", font=("goudy old style", 20), bg='#043256',
                          fg='white').place(x=0, y=0, relwidth=1)

        lbl_stu_code = Label(stu_Frame, text="Student ID ", font=("times new roman ", 15, 'bold'), bg='white').place(
            x=20, y=60)
        lbl_name = Label(stu_Frame, text="Name", font=("times new roman ", 15, 'bold'), bg='white').place(x=20, y=100)
        lbl_department = Label(stu_Frame, text="Department ", font=("times new roman ", 15, 'bold'), bg='white').place(
            x=20, y=140)
        lbl_designation = Label(stu_Frame, text="Designation ", font=("times new roman ", 15, 'bold'),
                                bg='white').place(x=20, y=180)

        txt_stu_code = Entry(stu_Frame, font=("times new roman ", 15), textvariable=self.var_stu_code,
                             bg='lightyellow').place(x=200, y=60)
        txt_name = Entry(stu_Frame, font=("times new roman ", 15), textvariable=self.var_name, bg='lightyellow').place(
            x=200, y=100)
        txt_department = Entry(stu_Frame, font=("times new roman ", 15), textvariable=self.var_department,
                               bg='lightyellow').place(x=200, y=140)
        txt_designation = Entry(stu_Frame, font=("times new roman ", 15), textvariable=self.var_designation,
                                bg='lightyellow').place(x=200, y=180)

        btn_generate = Button(stu_Frame, text="QR Generate", command=self.generate,
                              font=("times new roman", 18, 'bold'), bg='#2196f3', fg='white').place(x=90, y=250,
                                                                                                    width=180,
                                                                                                    height=30)
        btn_generate = Button(stu_Frame, text="Clear", command=self.clear, font=("times new roman", 18, 'bold'),
                              bg='#607d8b', fg='white').place(x=282, y=250, width=120, height=30)

        self.msg = ''
        self.lbl_msg = Label(stu_Frame, text=self.msg, font=("times new roman ", 20), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=310, relwidth=1)

        # ****** QR Code ****
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=250, height=380)
        qr_title = Label(qr_Frame, text="Student QR Code", font=("goudy old style", 20), bg='#043256',
                         fg='white').place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_Frame, text='No QR\nAvailable', font=('times new roman', 15), bg='#3f51b5', fg='white',
                             bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=200, height=180)

    def clear(self):
        self.var_stu_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if type(self.var_stu_code.get()) != int:
            self.msg = 'Student ID must be in integer'
            self.lbl_msg.config(text=self.msg, fg='red')
        if self.var_stu_code.get() == '' or self.var_name.get() == '' or self.var_department.get() == '' or self.var_designation.get() == '':
            self.msg = 'All fields are required'
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            self.msg = 'QR Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg, fg='green')
            qr_data = (
                f"Student ID: {self.var_stu_code.get()}\n Student Name :{self.var_name.get()}\n Department:{self.var_department.get()}\n Designation : {self.var_designation.get()}")
            qr_code = qrcode.make(qr_data)
            print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])
            qr_code.save("Student_QR/Stu" + str(self.var_stu_code.get()) + '.png')
            # ***QR Code image update
            self.im = ImageTk.PhotoImage(file="Student_QR/Stu" + str(self.var_stu_code.get()) + '.png')
            self.qr_code.config(image=self.im)
            # ******updating notification*********
            self.msg = 'QR Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg, fg='green')


root = Tk()
obj = Qr_Generator(root)
root.mainloop()