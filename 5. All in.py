from tkinter import *
from tkinter import ttk
import jdatetime
from tkinter import messagebox

win = Tk()


# داده هاي پيش فرض محاسبات حقوق

days_in_month = 30
monthly_working_hours = 220
daily_required_hours = 7.33
overtime_rate = 1.40
night_work_rate = 0.35
friday_work_rate = 0.40
holiday_work_rate = 0.40
insurance_rate = 0.07
housing_allowance = 30000000
food_allowance = 22000000
seniority_allowance = 5000000
child_allowance = 16625550
marriage_allowance = 5000000
mission_allowance = 0



def calculate_required_hours():

    required_hours = days_in_month * daily_required_hours

    return required_hours

###############################
def calculate_overtime_hours(worked_hours, required_hours):

    overtime_hours = worked_hours - required_hours

    if overtime_hours < 0:
        overtime_hours = 0

    return overtime_hours


###############################

def calculate_shortage_hours(worked_hours, required_hours):

    shortage_hours = required_hours - worked_hours

    if shortage_hours < 0:
        shortage_hours = 0

    return shortage_hours

###############################

def calculate_normal_hours(worked_hours, overtime_hours):

    normal_hours = worked_hours - overtime_hours

    return normal_hours

##############################

def calculate_daily_wage(monthly_salary):

    daily_wage = monthly_salary / days_in_month

    return daily_wage

###############################

def calculate_hourly_wage(monthly_salary):

    hourly_wage = monthly_salary / monthly_working_hours

    return hourly_wage

###############################

def calculate_overtime_pay(hourly_wage, overtime_hours):

    overtime_pay = hourly_wage * overtime_hours * overtime_rate

    return overtime_pay

###############################

def calculate_night_work_pay(hourly_wage, night_hours):

    night_work_pay = hourly_wage * night_hours * night_work_rate

    return night_work_pay

###############################

def calculate_holiday_work_pay(hourly_wage, holiday_hours):

    holiday_work_pay = hourly_wage * holiday_hours * holiday_work_rate

    return holiday_work_pay

###############################

def calculate_mission_pay(mission_hours):

    mission_pay = mission_hours * mission_allowance

    return mission_pay

###############################

def calculate_housing_allowance():

    housing_pay = housing_allowance

    return housing_pay

##############################

def calculate_food_allowance():

    food_pay = food_allowance

    return food_pay

#############################

def calculate_seniority_allowance():

    seniority_pay = seniority_allowance

    return seniority_pay

#############################

def calculate_child_allowance(children):

    child_pay = children * child_allowance

    return child_pay

#############################

def calculate_marriage_allowance(marital_status):

    if marital_status == 'متاهل':

        marriage_pay = marriage_allowance

    else:

        marriage_pay = 0

    return marriage_pay

#############################

#Gross Salary

def calculate_gross_salary(base_salary,
                           overtime_pay,
                           night_work_pay,
                           holiday_work_pay,
                           mission_pay,
                           housing_pay,
                           food_pay,
                           seniority_pay,
                           child_pay,
                           marriage_pay):

    gross_salary = base_salary + overtime_pay + night_work_pay + holiday_work_pay + mission_pay + housing_pay + food_pay + seniority_pay + child_pay + marriage_pay

    return gross_salary

#############################

#کسورات

#بيمه

def calculate_insurance(gross_salary):

    insurance = gross_salary * insurance_rate

    return insurance

#جمع کل کسورات
def calculate_total_deductions(insurance, tax, other_deductions):

    total_deductions = insurance + tax + other_deductions

    return total_deductions

#خالص پرداختي

def calculate_net_salary(gross_salary, total_deductions):

    net_salary = gross_salary - total_deductions

    return net_salary


# 1. Main Page


def main_page():


    win.title('منوي اصلي')
    win.iconbitmap('cool_bitty_kitty.ico')
    win.state('zoomed')


#Main page

#Top frame
    frm_top = Frame(win, bg='white', width=1920, height=540)

    title = Label(frm_top,
                  text='پروژه محاسبات عملکرد ماهانه',
                  font=('B Nazanin', 40),
                  bg='white',
                  )

    frm_top.place(x=0, y=0)
    title.place(x=800, y=250, anchor='center')


#Bottom frame
    frm_bottom = Frame(win, bg='silver', width=1920, height=540)

    frm_bottom.place(x=0, y=540)


#Boxes
    box1 = Frame(win, bg='gray', width=250, height=250)
    box2 = Frame(win, bg='gray', width=250, height=250)
    box3 = Frame(win, bg='gray', width=250, height=250)

    box1.place(x=200, y=415)
    box2.place(x=635, y=415)
    box3.place(x=1070, y=415)


#images
    img1 = PhotoImage(file='Bt4.png')
    img2 = PhotoImage(file='Bt5.png')
    img3 = PhotoImage(file='Bt6.png')

    img1 = img1.subsample(4, 4)
    img2 = img2.subsample(4, 4)
    img3 = img3.subsample(4, 4)


#Buttons
    btn1 = Button(box1,
                  image=img1,
                  command = employee_page)

    btn2 = Button(box2,
                  image=img2,
                  command = payroll_page)

    btn3 = Button(box3,
                  image=img3,
                  command = report_page)


    btn1.pack()
    btn2.pack()
    btn3.pack()


# نگه داشتن عکس ها
    win.img1 = img1
    win.img2 = img2
    win.img3 = img3



# 2. Submit employee page


def employee_page():

    win.withdraw()

    employee_win = Toplevel(win)

    employee_win.title('ثبت نام کارمند')
    employee_win.configure(bg='silver')
    employee_win.iconbitmap('cool_bitty_kitty.ico')
    employee_win.state('zoomed')

#توابع مربوط به سه دکمه دسترسي سريع در منو سمت راست

    def go_payroll():

        employee_win.withdraw()
        payroll_page()


    def go_employee():

        employee_win.withdraw()
        employee_page()


    def go_report():

        employee_win.withdraw()
        report_page()


# تابع خطا وارد کردن شماره ملي تکراري

    def check_national_id(event):

        national_id = ent6.get()

        file = open('employees.txt', 'r', encoding='utf-8')

        for i in file:

            if "'national_id': '" + national_id + "'" in i:

                messagebox.showerror('شماره ملي وارد شده تکراري است.')

                ent6.delete(0, END)

                file.close()

                return 'break'

        file.close()
        ent2.focus()
        return 'break'

    
# Save employee function
    

    def save_employee():
        entries = [ent2, ent3, ent4, ent5, ent6,
                   ent8, ent9,ent10, ent11, ent12,
                   ent13, ent14, ent15, ent16, ent17, ent18, ent19, ent20]

        empty = False

        for ent in entries:
            if ent.get() == '':
                ent.config(bg='red')
                empty = True
            else:
                ent.config(bg='white')

        if empty:
            messagebox.showwarning('هشدار', 'لطفاً اطلاعات فرم را کامل کنید.')
            return

        employee = {
            'full_name': ent2.get(),
            'birth_place': ent3.get(),
            'birth_date': ent4.get(),
            'gender': ent5.get(),
            'national_id': ent6.get(),

            'marital_status': ent8.get(),
            'children': ent9.get(),

            'education': ent10.get(),
            'field_of_study': ent11.get(),
            'university': ent12.get(),

            'job_position': ent13.get(),
            'job_title': ent14.get(),
            'service_group': ent15.get(),
            'service_unit': ent16.get(),
            'insurance': ent17.get(),
            'contract_type': ent18.get(),
            'base_salary': ent19.get(),
            'bonus': ent20.get()
        }

        file = open('employees.txt', 'a', encoding='utf-8')
        file.write(str(employee) + '\n')
        file.close()
        messagebox.showinfo('ذخیره اطلاعات', 'اطلاعات با موفقیت ذخیره شد.')

        for ent in entries:
            ent.delete(0, END)
            ent.config(bg='white')

        ent2.focus()


# Check number for ent9

    def check_ent9(event):

        text = ent9.get()

        if not text.isdigit():

            messagebox.showerror('خطا', 'لطفاً عدد وارد کنید.')

            ent9.delete(0, END)
            ent9.focus()

            return 'break'


        ent10.focus()

        return 'break'


# Check number for ent19

    def check_ent19(event):

        text = ent19.get()

        if not text.isdigit():

            messagebox.showerror('خطا', 'لطفاً عدد وارد کنید.')

            ent19.delete(0, END)
            ent19.focus()

            return 'break'

        ent20.focus()


        return 'break'


# Check number for ent20

    def check_ent20(event):

        text = ent20.get()

        if not text.isdigit():

            messagebox.showerror('خطا', 'لطفاً عدد وارد کنید.')

            ent20.delete(0, END)
            ent20.focus()

            return 'break'

        save_employee()

        return 'break'

# Clear form function
    

    def clear_form():

        ent2.delete(0, END)
        ent2.config(bg='white')

        ent3.delete(0, END)
        ent3.config(bg='white')

        ent4.delete(0, END)
        ent4.config(bg='white')
        
        ent5.delete(0, END)
        ent5.config(bg='white')

        ent6.delete(0, END)
        ent6.config(bg='white')

        ent8.delete(0, END)
        ent8.config(bg='white')

        ent9.delete(0, END)
        ent9.config(bg='white')

        ent10.delete(0, END)
        ent10.config(bg='white')

        ent11.delete(0, END)
        ent11.config(bg='white')

        ent12.delete(0, END)
        ent12.config(bg='white')

        ent13.delete(0, END)
        ent13.config(bg='white')

        ent14.delete(0, END)
        ent14.config(bg='white')

        ent15.delete(0, END)
        ent15.config(bg='white')

        ent16.delete(0, END)
        ent16.config(bg='white')

        ent17.delete(0, END)
        ent17.config(bg='white')

        ent18.delete(0, END)
        ent18.config(bg='white')

        ent19.delete(0, END)
        ent19.config(bg='white')

        ent20.delete(0, END)
        ent20.config(bg='white')

# تابع چک کردن فرم
    def check_form(event):

        if (ent2.get() != '' and
            ent3.get() != '' and
            ent4.get() != '' and
            ent5.get() != '' and
            ent6.get() != '' and
            ent8.get() != '' and
            ent9.get() != '' and
            ent10.get() != '' and
            ent11.get() != '' and
            ent12.get() != '' and
            ent13.get() != '' and
            ent14.get() != '' and
            ent15.get() != '' and
            ent16.get() != '' and
            ent17.get() != '' and
            ent18.get() != '' and
            ent19.get() != '' and
            ent20.get() != ''):

            btn4.config(state='normal')

        else:

            btn4.config(state='disabled')
#تابع ورود شماره ملي جهت ثبت نام

    numbers = '0123456789'
    def check_ent6(event):
        text = ent6.get()

        if len(text) >= 10:
            return 'break'

        if event.char not in numbers:
            return 'break'
                
#Frames


# Left frame top
    frm = LabelFrame(employee_win,
                     text='اطلاعات خانوار',
                     bg='silver',
                     labelanchor='n',
                     font=('B Nazanin', 16,),
                     width=400,
                     height=150
                     )

    frm.place(x=250, y=50)


# Left frame bottom
    frm1 = LabelFrame(employee_win,
                      text='اطلاعات تحصيلي',
                      bg='silver',
                      labelanchor='n',
                      font=('B Nazanin', 16,),
                      width=400,
                      height=200
                      )

    frm1.place(x=250, y=270)


# Right frame
    frm2 = LabelFrame(employee_win,
                      text='اطلاعات فردي',
                      bg='silver',
                      labelanchor='n',
                      font=('B Nazanin', 16,),
                      width=400,
                      height=350
                      )

    frm2.place(x=750, y=50)


# Bottom frame
    frm3 = LabelFrame(employee_win,
                      text='اطلاعات شغلي',
                      bg='silver',
                      labelanchor='n',
                      font=('B Nazanin', 16,),
                      width=900,
                      height=240
                      )

    frm3.place(x=250, y=500)



#Right frame labels


    lbl2 = Label(frm2,
                 text='نام و نام خانوادگي',
                 bg='silver',
                 anchor='e',
                 font=('B Nazanin', 14)
                 )

    lbl3 = Label(frm2,
                 text='محل تولد',
                 bg='silver',
                 anchor='e',
                 font=('B Nazanin', 14)
                 )

    lbl4 = Label(frm2,
                 text='سال تولد',
                 bg='silver',
                 anchor='e',
                 font=('B Nazanin', 14)
                 )

    lbl5 = Label(frm2,
                 text='جنسيت',
                 bg='silver',
                 anchor='e',
                 font=('B Nazanin', 14)
                 )

    lbl6 = Label(frm2,
                 text='شماره ملي',
                 bg='silver',
                 anchor='e',
                 font=('B Nazanin', 14)
                 )


    lbl2.place(x=370, y=100, anchor='e')
    lbl3.place(x=370, y=150, anchor='e')
    lbl4.place(x=370, y=200, anchor='e')
    lbl5.place(x=370, y=250, anchor='e')
    lbl6.place(x=370, y=50, anchor='e')



# Entries


    ent2 = Entry(frm2, width=25, font=('B Nazanin', 11))
    ent3 = Entry(frm2, width=25, font=('B Nazanin', 11))
    ent4 = Entry(frm2, width=25, font=('B Nazanin', 11))
    ent5 = Entry(frm2, width=25, font=('B Nazanin', 11))
    ent6 = Entry(frm2, width=25, font=('B Nazanin', 11))

    ent2.bind('<Return>', lambda event: ent3.focus())    
    ent3.bind('<Return>', lambda event: ent4.focus())
    ent4.bind('<Return>', lambda event: ent5.focus())
    ent5.bind('<Return>', lambda event: ent8.focus())
    ent6.bind('<KeyPress>', check_ent6)
    ent6.bind('<Return>', check_national_id)


    ent2.place(x=40, y=100, anchor='w')
    ent3.place(x=40, y=150, anchor='w')
    ent4.place(x=40, y=200, anchor='w')
    ent5.place(x=40, y=250, anchor='w')
    ent6.place(x=40, y=50, anchor='w')



# اطلاعات خانوار


    lbl8 = Label(frm,
                 text='وضعيت تاهل',
                 font=('B Nazanin', 14),
                 bg='silver')

    lbl9 = Label(frm,
                 text='تعداد فرزند',
                 font=('B Nazanin', 14),
                 bg='silver')


    lbl8.place(x=370, y=20, anchor='e')
    lbl9.place(x=370, y=70, anchor='e')


    ent8 = Entry(frm, width=25, font=('B Nazanin', 11))
    ent9 = Entry(frm, width=25, font=('B Nazanin', 11))

    ent8.bind('<Return>', lambda event: ent9.focus())
    ent9.bind('<Return>', check_ent9)
    
    ent8.place(x=50, y=10)
    ent9.place(x=50, y=55)



# اظلاعات تحصيلي


    lbl10 = Label(frm1,
                  text='مدرک تحصيلي',
                  font=('B Nazanin', 14),
                  bg='silver')

    lbl11 = Label(frm1,
                  text='رشته تحصيلي',
                  font=('B Nazanin', 14),
                  bg='silver')

    lbl12 = Label(frm1,
                  text='دانشگاه',
                  font=('B Nazanin', 14),
                  bg='silver')


    lbl10.place(x=370, y=20, anchor='e')
    lbl11.place(x=370, y=70, anchor='e')
    lbl12.place(x=370, y=120, anchor='e')


    ent10 = Entry(frm1, width=25, font=('B Nazanin', 11))
    ent11 = Entry(frm1, width=25, font=('B Nazanin', 11))
    ent12 = Entry(frm1, width=25, font=('B Nazanin', 11))

    ent10.bind('<Return>', lambda event: ent11.focus())
    ent11.bind('<Return>', lambda event: ent12.focus())
    ent12.bind('<Return>', lambda event: ent13.focus())


    ent10.place(x=50, y=10)
    ent11.place(x=50, y=55)
    ent12.place(x=50, y=105)



# اطلاعات شغلي


    lbl13 = Label(frm3,
                  text='سمت شغلي',
                  font=('B Nazanin', 14),
                  bg='silver')

    lbl14 = Label(frm3,
                  text='عنوان شغلي',
                  font=('B Nazanin', 14),
                  bg='silver')

    lbl15 = Label(frm3,
                  text='گروه خدمت',
                  font=('B Nazanin', 14),
                  bg='silver')

    lbl16 = Label(frm3,
                  text='واحد خدمت',
                  font=('B Nazanin', 14),
                  bg='silver')

    lbl17 = Label(frm3,
                  text='نوع بيمه',
                  font=('B Nazanin', 14),
                  bg='silver')

    lbl18 = Label(frm3,
                  text='نوع قرارداد',
                  font=('B Nazanin', 14),
                  bg='silver')

    lbl19 = Label(frm3,
                  text='حقوق پايه (ريال)',
                  font=('B Nazanin', 14),
                  bg='silver')

    lbl20 = Label(frm3,
                  text='کارانه (ريال)',
                  font=('B Nazanin', 14),
                  bg='silver')


    lbl13.place(x=880, y=20, anchor='e')
    lbl14.place(x=880, y=70, anchor='e')
    lbl15.place(x=880, y=120, anchor='e')
    lbl16.place(x=880, y=170, anchor='e')
    lbl17.place(x=370, y=20, anchor='e')
    lbl18.place(x=370, y=70, anchor='e')
    lbl19.place(x=370, y=120, anchor='e')
    lbl20.place(x=370, y=170, anchor='e')


    ent13 = Entry(frm3, width=25, font=('B Nazanin', 11))
    ent14 = Entry(frm3, width=25, font=('B Nazanin', 11))
    ent15 = Entry(frm3, width=25, font=('B Nazanin', 11))
    ent16 = Entry(frm3, width=25, font=('B Nazanin', 11))
    ent17 = Entry(frm3, width=25, font=('B Nazanin', 11))
    ent18 = Entry(frm3, width=25, font=('B Nazanin', 11))
    ent19 = Entry(frm3, width=25, font=('B Nazanin', 11))
    ent20 = Entry(frm3, width=25, font=('B Nazanin', 11))

    ent13.bind('<Return>', lambda event: ent14.focus())
    ent14.bind('<Return>', lambda event: ent15.focus())
    ent15.bind('<Return>', lambda event: ent16.focus())
    ent16.bind('<Return>', lambda event: ent17.focus())
    ent17.bind('<Return>', lambda event: ent18.focus())
    ent18.bind('<Return>', lambda event: ent19.focus())
    ent19.bind('<Return>', check_ent19)
    ent20.bind('<Return>', check_ent20)

    ent13.place(x=550, y=20, anchor='w')
    ent14.place(x=550, y=70, anchor='w')
    ent15.place(x=550, y=120, anchor='w')
    ent16.place(x=550, y=170, anchor='w')
    ent17.place(x=50, y=20, anchor='w')
    ent18.place(x=50, y=70, anchor='w')
    ent19.place(x=50, y=120, anchor='w')
    ent20.place(x=50, y=170, anchor='w')

#اينتري هاي چک کردن فرم

    ent2.bind('<KeyRelease>', check_form)
    ent3.bind('<KeyRelease>', check_form)
    ent4.bind('<KeyRelease>', check_form)
    ent5.bind('<KeyRelease>', check_form)
    ent6.bind('<KeyRelease>', check_form)
    ent8.bind('<KeyRelease>', check_form)
    ent9.bind('<KeyRelease>', check_form)
    ent10.bind('<KeyRelease>', check_form)
    ent11.bind('<KeyRelease>', check_form)
    ent12.bind('<KeyRelease>', check_form)
    ent13.bind('<KeyRelease>', check_form)
    ent14.bind('<KeyRelease>', check_form)
    ent15.bind('<KeyRelease>', check_form)
    ent16.bind('<KeyRelease>', check_form)
    ent17.bind('<KeyRelease>', check_form)
    ent18.bind('<KeyRelease>', check_form)
    ent19.bind('<KeyRelease>', check_form)
    ent20.bind('<KeyRelease>', check_form)

# Right frame


    frm_right = Frame(
        employee_win,
        bg='gainsboro',
        width=700,
        height=1080
    )

    frm_right.place(x=1170, y=0)


    btn1 = Button(frm_right,
                  text = 'ثبت نام کاربر',
                  width = 15,
                  height = 2,
                  command = go_employee)

    btn1.place(x=100, y=300)


    btn2 = Button(frm_right,
                  text = 'محاسبه حقوق',
                  width = 15,
                  height = 2,
                  command = go_payroll)

    btn2.place(x=100, y=360)


    btn3 = Button(frm_right,
                  text = 'دريافت فيش',
                  width= 15,
                  height = 2,
                  command = go_report)

    btn3.place(x=100, y=420)


#دکمه هاي ثبت نهايي و پاک کردن فرم

    btn4 = Button(employee_win,
                  text='ثبت اطلاعات',
                  width=15,
                  height=2,
                  state='disabled',
                  command=save_employee)

    btn4.place(x=250, y=750)


    btn5 = Button(employee_win,
                  text='پاک کردن فرم',
                  width=15,
                  height=2,
                  command=clear_form)

    btn5.place(x=400, y=750)

# 3. CALCULATE PAGE

def payroll_page():

    win.withdraw()

    payroll_win = Toplevel(win)

    payroll_win.title('محاسبات کارکرد ماهانه')
    payroll_win.configure(bg='silver')
    payroll_win.iconbitmap('cool_bitty_kitty.ico')
    payroll_win.state('zoomed')


#توابع مربوط به سه دکمه دسترسي سريع در منو سمت راست

    def go_payroll():

        payroll_win.withdraw()
        payroll_page()


    def go_employee():

        payroll_win.withdraw()
        employee_page()


    def go_report():

        payroll_win.withdraw()
        report_page()


#تابع حساب کردن ماليات بر درآمد

    def calculate_tax(taxable_salary):

        if taxable_salary <= 40000000:
            tax = 0

        elif taxable_salary <= 80000000:
            tax = (taxable_salary - 40000000) * 0.10

        elif taxable_salary <= 100000000:
            tax = (80000000 - 40000000) * 0.10
            tax = tax + (taxable_salary - 80000000) * 0.15

        elif taxable_salary <= 120000000:
            tax = (80000000 - 40000000) * 0.10
            tax = tax + (100000000 - 80000000) * 0.15
            tax = tax + (taxable_salary - 100000000) * 0.20

        elif taxable_salary <= 140000000:
            tax = (80000000 - 40000000) * 0.10
            tax = tax + (100000000 - 80000000) * 0.15
            tax = tax + (120000000 - 100000000) * 0.20
            tax = tax + (taxable_salary - 120000000) * 0.25

        else:
            tax = (80000000 - 40000000) * 0.10
            tax = tax + (100000000 - 80000000) * 0.15
            tax = tax + (120000000 - 100000000) * 0.20
            tax = tax + (140000000 - 120000000) * 0.25
            tax = tax + (taxable_salary - 140000000) * 0.30

        return tax

#تابع ذخيره اطلاعات
    def calculate_payroll():

        daily_hours = float(ent_daily_hours.get())
        holiday_hours = float(ent_holiday_hour.get())
        night_hours = float(ent_night_working_hour.get())
        mission_hours = float(ent_mission.get())

        required_hours = monthly_working_hours

        worked_hours = daily_hours * 30
        

        if worked_hours > required_hours:
            extra_hours = worked_hours - required_hours
            deficit_hours = 0

        else:
            extra_hours = 0
            deficit_hours = required_hours - worked_hours

        normal_hours = worked_hours - extra_hours

        lbl_monthly_hours.config(text=required_hours)
        lbl_normal_hours.config(text=normal_hours)
        lbl_extra_hours.config(text=extra_hours)
        lbl_deficit_hours.config(text=deficit_hours)


        base_salary = float(lbl_employee_salary.cget('text'))
        bonus = float(lbl_bonus.cget('text'))


        food = food_allowance
        housing = housing_allowance

        
        children = int(lbl_employee_children.cget('text'))
        child = children * child_allowance


        hourly_salary = round (base_salary / monthly_working_hours,1)
        overtime = round(hourly_salary * extra_hours * overtime_rate,1)
        night = round (hourly_salary * night_hours * night_work_rate,1)
        holiday = round (hourly_salary * holiday_hours * holiday_work_rate,1)
        mission = round(mission_hours * hourly_salary,1)


        lbl_base_salary.config(text=int(base_salary))
        lbl_bonus.config(text=int (bonus))

        lbl_food.config(text=round(food))
        lbl_housing.config(text=round(housing))
        lbl_child.config(text=(child))

        lbl_overtime.config(text=round(overtime))
        lbl_night.config(text=round(night))
        lbl_holiday.config(text=round(holiday))
        lbl_mission.config(text=round(mission))

        gross_salary = round(base_salary
        + bonus
        + food
        + housing
        + child
        + overtime
        + night
        + holiday
        + mission, 1)


        deficit_amount = round (hourly_salary * deficit_hours,1)

        insurance = round(gross_salary * insurance_rate,1)

        taxable_salary = gross_salary
        tax = round(calculate_tax(taxable_salary),1)

        lbl_deficit.config(text=round(deficit_amount))
        lbl_insurance.config(text=round(insurance))
        lbl_tax.config(text=round(tax))


        total_deductions = round(
            deficit_amount
            + insurance
            + tax,1)

        lbl_total_deductions.config(text=round(total_deductions,1))
                                    
        net_salary = gross_salary - total_deductions

        lbl_net_salary.config(text=round(net_salary))


        payroll_data['national_id'] = lbl_employee_national_id.cget('text')
        payroll_data['employee_name'] = lbl_employee_name.cget('text')
        payroll_data['job_title'] = lbl_employee_job.cget('text')
        payroll_data['employee_id'] = lbl_employee_national_id.cget('text')

        payroll_data['daily_hours'] = daily_hours
        payroll_data['holiday_hours'] = holiday_hours
        payroll_data['night_hours'] = night_hours
        payroll_data['mission_hours'] = mission_hours

        payroll_data['monthly_hours'] = required_hours
        payroll_data['worked_hours'] = worked_hours
        payroll_data['normal_hours'] = normal_hours
        payroll_data['overtime_hours'] = extra_hours
        payroll_data['deficit_hours'] = deficit_hours

        payroll_data['base_salary'] = base_salary
        payroll_data['bonus'] = bonus
        payroll_data['food'] = food
        payroll_data['housing'] = housing
        payroll_data['child'] = child
        payroll_data['overtime'] = overtime
        payroll_data['night'] = night
        payroll_data['holiday'] = holiday
        payroll_data['mission'] = mission

        payroll_data['gross_salary'] = gross_salary

        payroll_data['deficit_amount'] = deficit_amount
        payroll_data['insurance'] = insurance
        payroll_data['tax'] = tax
        payroll_data['total_deductions'] = total_deductions

        payroll_data['net_salary'] = net_salary

        payroll_data['year'] = ent_year.get()
        payroll_data['month'] = ent_month.get()

        btn4.config(state='normal')
        


#تابع دکمه پاک کردن فرم

    def clear_payroll_form():

        search_box_ent.delete(0, END)

        ent_daily_hours.delete(0, END)
        ent_holiday_hour.delete(0, END)
        ent_night_working_hour.delete(0, END)
        ent_mission.delete(0, END)

        ent_year.set('')
        ent_month.set('')

        ent_year.config(state='disabled')
        ent_month.config(state='disabled')

        ent_daily_hours.config(state='disabled')
        ent_holiday_hour.config(state='disabled')
        ent_night_working_hour.config(state='disabled')
        ent_mission.config(state='disabled')

        lbl_employee_name.config(text='')
        lbl_employee_national_id.config(text='')
        lbl_employee_job.config(text='')
        lbl_employee_salary.config(text='')
        lbl_employee_marital_status.config(text='')
        lbl_employee_children.config(text='')
        lbl_employee_position.config(text='')
        lbl_employee_insurance.config(text='')

        lbl_monthly_hours.config(text='')
        lbl_normal_hours.config(text='')
        lbl_extra_hours.config(text='')
        lbl_deficit_hours.config(text='')

        lbl_base_salary.config(text='')
        lbl_bonus.config(text='')
        lbl_food.config(text='')
        lbl_housing.config(text='')
        lbl_child.config(text='')
        lbl_overtime.config(text='')
        lbl_night.config(text='')
        lbl_holiday.config(text='')
        lbl_mission.config(text='')

        lbl_deficit.config(text='')
        lbl_insurance.config(text='')
        lbl_tax.config(text='')
        lbl_total_deductions.config(text='')
        lbl_net_salary.config(text='')

        btn4.config(state='disabled')
        btn5.config(state='disabled')
        btn6.config(state='disabled')

        btn_search_employee.config(state='disabled')

        search_box_ent.focus()        
                
# تابع محدود کردن شماره ملی

    def check_national_id_length(event):
        text = search_box_ent.get()

        if len(text) > 10:
            search_box_ent.delete(10, END)
            return

        if len(text) == 10:
            btn_search_employee.config(state='normal')

        else:
            btn_search_employee.config(state='disabled')

#تابع دکمه جستجو
            

    def search_employee(event = None):

        national_id = search_box_ent.get()

        file = open('employees.txt', 'r', encoding='utf-8')

        found = False

        for i in file:

            if "'national_id': '" + national_id + "'" in i:
                found = True

                btn5.config(state='normal')

                full_name = i.split("'full_name': '")[1].split("'")[0]
                national_id = i.split("'national_id': '")[1].split("'")[0]
                job_title = i.split("'job_title': '")[1].split("'")[0]
                
                base_salary = i.split("'base_salary': '")[1].split("'")[0]
                bonus = i.split("'bonus': '")[1].split("'")[0]

                
                marital_status = i.split("'marital_status': '")[1].split("'")[0]
                number_of_children = i.split("'children': '")[1].split("'")[0]
                job_position = i.split("'job_position': '")[1].split("'")[0]
                insurance_type = i.split("'insurance': '")[1].split("'")[0]

                lbl_employee_name.config(text=full_name)
                lbl_employee_national_id.config(text=national_id)
                lbl_employee_job.config(text=job_title)
                
                lbl_employee_salary.config(text=base_salary)
                lbl_employee_marital_status.config(text=marital_status)
                lbl_employee_children.config(text=number_of_children)
                lbl_employee_position.config(text=job_position)
                lbl_employee_insurance.config(text=insurance_type)

                lbl_base_salary.config(text=base_salary)
                lbl_bonus.config(text=bonus)
                
                lbl_food.config(text=food_allowance)
                lbl_housing.config(text=housing_allowance)
                lbl_child.config(text=child_allowance)

                ent_year.config(state='readonly')
                ent_month.config(state='readonly')

                ent_daily_hours.config(state='normal')
                ent_holiday_hour.config(state='normal')
                ent_night_working_hour.config(state='normal')
                ent_mission.config(state='normal')

        file.close()

        if found == False:

            messagebox.showerror(
                                 'کاربر ثبت نشده است.')        

###### تابع دکمه ذخيره سازي 

    payroll_data = {}

    def save_payroll():
        national_id = payroll_data['national_id']
        year = payroll_data['year']
        month = payroll_data['month']

        file = open('payroll.txt', 'r', encoding='utf-8')

        for i in file:

            if ("'national_id': '" + national_id + "'" in i and
                "'year': '" + year + "'" in i and
                "'month': '" + month + "'" in i):

                file.close()

                messagebox.showerror(
                    'خطا',
                    'برای این تاریخ و کاربر فیش حقوقی صادر شده است.\nتاریخ جدید را وارد کنید.'
                )

                return

        file.close()

        file = open('payroll.txt', 'a', encoding='utf-8')

        file.write(str(payroll_data) + '\n')

        file.close()

        messagebox.showinfo(
            'ذخیره اطلاعات',
            'فیش حقوقی صادر و ذخیره شد.'
        )

        clear_payroll_form()


#تابع دکمه هاي بررسي کننده
            
    def check_payroll_inputs(event=None):

        if (ent_daily_hours.get() != '' and
            ent_holiday_hour.get() != '' and
            ent_night_working_hour.get() != '' and
            ent_mission.get() != ''):

            btn6.config(state='normal')

        else:

            btn6.config(state='disabled')


# Top frame

    frm = LabelFrame(payroll_win,
            text = 'جستجوي کارمند',
            bg='silver',
            labelanchor = 'n',
            font = ('B nazanin', 14,),
            width=920,
            height=130
            )
    frm.place(x=500, y=20, anchor='n')


    search_box = Label(frm,
                       text='لطفا شماره ملي کارمند را اينجا وارد کنيد',
                       bg='silver',
                       font= ('B nazanin', 14)
                       )
    search_box.place(x=900, y=40, anchor='e')


    search_box_ent = Entry(frm,
                           width=25,
                           bg='white',
                           font = ('B nazanin', 12)
                           )
    search_box_ent.place(x=620, y=40, anchor='e')

    btn_search_employee  = Button(frm,
                  text='جستجو',
                  width=15,
                  height=1,
                  state='disabled',
                  command = search_employee
                  )
    btn_search_employee.place(x=410, y=40, anchor='e')
    
    search_box_ent.bind('<KeyRelease>', check_national_id_length)
        
# Left frames

    frm1_left_top = LabelFrame(payroll_win,
        text = 'مزاياي قانوني (ريال)',
        bg='silver',
        labelanchor = 'n',
        font = ('B nazanin', 16,),
        width=500,
        height=220
    )

    frm1_left_top.place(x=40, y=150)

    lef_top_base_salary = Label(frm1_left_top,
                                text='حقوق پايه',
                                bg='silver',
                                font= ('B nazanin', 14))
    lef_top_base_salary.place(x=490, y=10, anchor='e')

    lef_top_bonus = Label(frm1_left_top,
                               text='کارانه',
                               bg='silver',
                               font= ('B nazanin', 14)
                               )
    lef_top_bonus.place(x=490, y=45, anchor='e')

    lef_top_grocery = Label(frm1_left_top,
                                 text='حق خار و بار',
                                 bg='silver',
                                 font= ('B nazanin', 14)
                                 )
    lef_top_grocery.place(x=490, y=80, anchor='e')

    lef_top_housing = Label(frm1_left_top,
                                 text='حق مسکن',
                                 bg='silver',
                                 font= ('B nazanin', 14)
                                 )
    lef_top_housing.place(x=490, y=120, anchor='e')

    lef_top_children = Label(frm1_left_top,
                             text='حق اولاد',
                             bg='silver',
                             font= ('B nazanin', 14)
                             )
    lef_top_children.place(x=490, y=160, anchor='e')


    lef_top_extra_hour = Label(frm1_left_top,
                               text='اضافه کاري',
                               bg='silver',
                               font= ('B nazanin', 14)
                               )
    lef_top_extra_hour.place(x=250, y=10, anchor='e')


    lef_top_night_work = Label(frm1_left_top,
                               text='شب کاري',
                               bg='silver',
                               font= ('B nazanin', 14)
                               )
    lef_top_night_work.place(x=250, y=45, anchor='e')

    lef_top_work_holiday = Label(frm1_left_top,
                                 text='کار در تعطيلات',
                                 bg='silver',
                                 font= ('B nazanin', 14)
                                 )
    lef_top_work_holiday.place(x=250, y=80, anchor='e')

    lef_top_mission = Label(frm1_left_top,
                            text='حق ماموريت',
                            bg='silver',
                            font= ('B nazanin', 14)
                            )
    lef_top_mission.place(x=250, y=120, anchor='e')



#نوشته هاي ظاهر شونده جلوي ليبل ها مزاياي قانوني

    lbl_base_salary = Label(frm1_left_top,
                            text='',
                            bg='silver',
                            font= ('B nazanin', 14)
                            )

    lbl_base_salary.place(x=280, y=-5)


    lbl_bonus = Label(frm1_left_top,
                      text='',
                      bg='silver',
                      font= ('B nazanin', 14)
                      )

    lbl_bonus.place(x=280, y=30)


    lbl_food = Label(frm1_left_top,
                     text='',
                     bg='silver',
                     font= ('B nazanin', 14))

    lbl_food.place(x=280, y=65)


    lbl_housing = Label(frm1_left_top,
                        text='',
                        bg='silver',
                        font= ('B nazanin', 14))

    lbl_housing.place(x=280, y=105)


    lbl_child = Label(frm1_left_top,
                      text='',
                      bg='silver',
                      font= ('B nazanin', 14))

    lbl_child.place(x=280, y=140)


    lbl_overtime = Label(frm1_left_top,
                         text='',
                         bg='silver',
                         font= ('B nazanin', 14))

    lbl_overtime.place(x=20, y=-5)


    lbl_night = Label(frm1_left_top,
                      text='',
                      bg='silver',
                      font= ('B nazanin', 14))

    lbl_night.place(x=20, y=30)


    lbl_holiday = Label(frm1_left_top,
                        text='',
                        bg='silver',
                        font= ('B nazanin', 14))

    lbl_holiday.place(x=20, y=60)


    lbl_mission = Label(frm1_left_top,
                        text='',
                        bg='silver',
                        font= ('B nazanin', 14))

    lbl_mission.place(x=20, y=90)


############ فريم کسورات قانوي ##############

    frm_mid_left = LabelFrame(payroll_win,
        text = 'کسورات قانوني (ريال)',
        bg='silver',
        labelanchor = 'n',
        font = ('B nazanin', 16,),
        width=500,
        height=170
    )
    frm_mid_left.place(x=40, y=380)


    frm_mid_left_deficit = Label(frm_mid_left,
                    text='کسر کار',
                    bg='silver',
                    font= ('B nazanin', 14)
                    )
    frm_mid_left_deficit.place(x=490, y=30, anchor='e')

    frm_mid_left_insurance = Label(frm_mid_left,
                                 text='سهم بيمه کارمند ',
                                 bg='silver',
                                 font= ('B nazanin', 14)
                                 )
    frm_mid_left_insurance.place(x=490, y=100, anchor='e')

    frm_mid_left_tax = Label(frm_mid_left,
                             text='ماليات',
                             bg='silver',
                             font= ('B nazanin', 14)
                             )
    frm_mid_left_tax.place(x=250, y=30, anchor='e')


    frm_mid_left_deduction = Label(frm_mid_left,
                                   text='جمع کسورات',
                                   bg='silver',
                                   font= ('B nazanin', 16)
                                   )
    frm_mid_left_deduction.place(x=250, y=100, anchor='e')


###########ليبل هاي ظاهر شونده کسورات قانوني #############

    lbl_deficit = Label(frm_mid_left,
                    text='',
                    bg='silver',
                    font= ('B nazanin', 14))

    lbl_deficit.place(x=280, y=10)


    lbl_insurance = Label(frm_mid_left,
                          text='',
                          bg='silver',
                          font= ('B nazanin', 14))

    lbl_insurance.place(x=280, y=85)


    lbl_tax = Label(frm_mid_left,
                    text='',
                    bg='silver',
                    font= ('B nazanin', 14)
                    )

    lbl_tax.place(x=20, y=10)


    lbl_total_deductions = Label(frm_mid_left,
                                 text='',
                                 bg='silver',
                                 font= ('B nazanin', 14)
                                 )

    lbl_total_deductions.place(x=20, y=85)

    
################## خالص پرداختي ##############

    frm_bottom_left = LabelFrame(payroll_win,
        text = 'خالص پرداختي (ريال)',
        bg='silver',
        labelanchor = 'n',
        font = ('B nazanin', 16,),
        width=500,
        height=100
    )
    frm_bottom_left.place(x=40, y=550)

    frm_bottom_left_int_salary = Label(frm_bottom_left,
                                       text='به عدد',
                                       bg='silver',
                                       font= ('B nazanin', 14)
                                       )
    frm_bottom_left_int_salary.place(x=490, y=20, anchor='e')

#################ليبل هاي ظاهرشونده خالص پرداختي  ##############

    lbl_net_salary = Label(frm_bottom_left,
                       text='',
                       bg='silver',
                       font= ('B nazanin', 14))

    lbl_net_salary.place(x=160, y=5)


    lbl_net_salary_text = Label(frm_bottom_left,
                                text='',
                                bg='silver',
                                width=30)

    lbl_net_salary_text.place(x=120, y=80)

    

# Labels inside frm2_mid

    frm2_mid = LabelFrame(payroll_win,
        text = 'اطلاعات کارکرد',
        bg='silver',
        labelanchor = 'n',
        font = ('B nazanin', 16,),
        width=300,
        height=550
    )

    frm2_mid.place(x=550, y=150)
    date = Label(frm2_mid,
                 text='تاريخ',
                 bg='silver',
                 font= ('B nazanin', 14)
                 )
    date.place(x=270, y=30, anchor='e')

    monthly_hours = Label(frm2_mid,
                          text='ساعت کار موظف ماه',
                          bg='silver',
                          font= ('B nazanin', 14)
                          )
    monthly_hours.place(x=270, y=85, anchor='e')


    daily_hours = Label(frm2_mid,
                        text='ساعت کارکرد روزانه',
                        bg='silver',
                        font= ('B nazanin', 14)
                        )
    daily_hours.place(x=270, y=140, anchor='e')

    normal_working_hours = Label(frm2_mid,
                                 text='ساعت کار عادي',
                                 bg='silver',
                                 font= ('B nazanin', 14)
                                 )
    normal_working_hours.place(x=270, y=195, anchor='e')

    extra_hour = Label(frm2_mid,
                       text='ساعت اضافه کاري',
                       bg='silver',
                       font= ('B nazanin', 14)
                       )
    extra_hour.place(x=270, y=250, anchor='e')

    deficit_working_hour = Label(frm2_mid,
                                 text='ساعت کسر کار',
                                 bg='silver',
                                 font= ('B nazanin', 14)
                                 )
    deficit_working_hour.place(x=270, y=305, anchor='e')

    holiday_hours = Label(frm2_mid,
                          text='ساعت کار روزهاي ',
                          bg='silver',
                          font= ('B nazanin', 14)
                          )
    holiday_hours.place(x=270, y=360, anchor='e')

    holiday_hours = Label(frm2_mid,
                          text='تعطيل',
                          bg='silver',
                          font= ('B nazanin', 14)
                          )
    holiday_hours.place(x=270, y=395, anchor='e')

    night_working_hour = Label(frm2_mid,
                               text='ساعت شب کاري',
                               bg='silver',
                               font= ('B nazanin', 14)
                               )
    night_working_hour.place(x=270, y=450, anchor='e')

    mission = Label(frm2_mid,
                    text='ساعت ماموريت',
                    bg='silver',
                    font= ('B nazanin', 14)
                    )
    mission.place(x=270, y=490, anchor='e')


# entries inside frm2_mid 

    ent_year = ttk.Combobox(frm2_mid,
                            font= ('B nazanin', 8),
                            values=('1405', '1406'),
                            width=12,
                            state='disabled'
                            )
    ent_year.place(x=5, y=25)


    ent_month = ttk.Combobox(frm2_mid,
                             font= ('B nazanin', 8),
                             values=('فروردين', 'ارديبهشت', 'خرداد', 'تير',
                                     'مرداد', 'شهريور', 'مهر', 'آبان',
                                     'آذر', 'دي', 'بهمن', 'اسفند'),
                             width=12,
                             state='disabled'
                             )
    ent_month.place(x=120, y=25)

    ent_daily_hours = Entry(frm2_mid,
                            width=6,
                            bg='white',
                            font= ('B nazanin', 12),
                            state = 'disabled'
                            )
    ent_daily_hours.place(x=50, y=135)
    ent_daily_hours.bind('<KeyRelease>', check_payroll_inputs)
    ent_daily_hours.bind('<Return>', lambda event: ent_holiday_hour.focus())


    ent_holiday_hour = Entry(frm2_mid, width=6,
                             bg='white',
                             font= ('B nazanin', 12),
                             state = 'disabled'
                             )
    ent_holiday_hour.place(x=50, y=370)
    ent_holiday_hour.bind('<KeyRelease>', check_payroll_inputs)
    ent_holiday_hour.bind('<Return>', lambda event: ent_night_working_hour.focus())


    ent_night_working_hour = Entry(frm2_mid,
                                   width=6,
                                   bg='white',
                                   font= ('B nazanin', 12),
                                   state = 'disabled'
                                   )
    ent_night_working_hour.place(x=50, y=440)
    ent_night_working_hour.bind('<KeyRelease>', check_payroll_inputs)
    ent_night_working_hour.bind('<Return>', lambda event: ent_mission.focus())



    ent_mission = Entry(frm2_mid,
                        width=6,
                        bg='white',
                        font= ('B nazanin', 12),
                        state = 'disabled'
                        )
    ent_mission.place(x=50, y=480)
    ent_mission.bind('<KeyRelease>', check_payroll_inputs)
    

######################## اطلاعات ظاهر شونده اطلاعات کارکرد ########################


    lbl_monthly_hours = Label(frm2_mid,
                        text='',
                        bg='silver',
                        font= ('B nazanin', 14)
                        )

    lbl_monthly_hours.place(x=50, y=70)


    lbl_normal_hours = Label(frm2_mid,
                             text='',
                             bg='silver',
                             font= ('B nazanin', 14)
                             )

    lbl_normal_hours.place(x=50, y=180)


    lbl_extra_hours = Label(frm2_mid,
                            text='',
                            bg='silver',
                            font= ('B nazanin', 14)
                            )

    lbl_extra_hours.place(x=50, y=235)


    lbl_deficit_hours = Label(frm2_mid,
                              text='',
                              bg='silver',
                              font= ('B nazanin', 14)
                              )

    lbl_deficit_hours.place(x=50, y=290)


################# مشخصات کارمند #################

    frm3_right = LabelFrame(payroll_win,
        text = 'مشخصات کارمند',
        bg='silver',
        labelanchor = 'n',
        font = ('B nazanin', 16,),
        width=300,
        height=550
    )

    frm3_right.place(x=860, y=150)

############# ليبل هاي ثابت در ستون مشخصات  کارمند براي جستجو #######


    lbl_employee_name_title = Label(frm3_right,
          text='نام و نام خانوادگی',
          bg='silver',
          font=('B nazanin', 14)
          )
    lbl_employee_name_title.place(x=280, y=50, anchor='e')


    lbl_national_ID = Label(frm3_right,
          text='شماره ملی',
          bg='silver',
          font=('B nazanin', 14)
          )
    lbl_national_ID.place(x=280, y=110, anchor='e')


    lbl_Job_title = Label(frm3_right,
          text='عنوان شغلی',
          bg='silver',
          font=('B nazanin', 14)
          )
    lbl_Job_title.place(x=280, y=170, anchor='e')


    lbl_base_salary_title = Label(frm3_right,
          text='حقوق پایه (ريال)',
          bg='silver',
          font=('B nazanin', 14)
          )
    lbl_base_salary_title.place(x=280, y=230, anchor='e')
    

    lbl_marital_status = Label(frm3_right,
          text='وضعيت تاهل',
          bg='silver',
          font=('B nazanin', 14)
          )
    lbl_marital_status.place(x=280, y=290, anchor='e')

    lbl_number_of_children = Label(frm3_right,
          text='تعداد فرزند',
          bg='silver',
          font=('B nazanin', 14)
          )
    lbl_number_of_children.place(x=280, y=350, anchor='e')

    lbl_job_position = Label(frm3_right,
          text='سمت شغلي',
          bg='silver',
          font=('B nazanin', 14)
          )
    lbl_job_position.place(x=280, y=410, anchor='e')


    lbl_insurance_type = Label(frm3_right,
          text='نوع بيمه',
          bg='silver',
          font=('B nazanin', 14)
          )
    lbl_insurance_type.place(x=280, y=470, anchor='e')


############ ليبل هاي ظاهر شونده در فريم مشخصات کارمند بعد از جستجو شماره ملي #########

    lbl_employee_name = Label(frm3_right,
                              text='',
                              bg='silver',
                              font = ('B Nazanin', 14)
                              )
    lbl_employee_name.place(x=90, y=35)


    lbl_employee_national_id = Label(frm3_right,
                                     text='',
                                     bg='silver',
                                     font = ('B Nazanin', 14)
                                     )
    lbl_employee_national_id.place(x=90, y=95)


    lbl_employee_job = Label(frm3_right,
                             text='',
                             bg='silver',
                             font = ('B Nazanin', 14)
                             )
    lbl_employee_job.place(x=90, y=155)


    lbl_employee_salary = Label(frm3_right,
                                text='',
                                bg='silver',
                                font = ('B Nazanin', 14)
                                )
    lbl_employee_salary.place(x=90, y=215)


    lbl_employee_marital_status = Label(frm3_right,
                                    text='',
                                    bg='silver',
                                    font = ('B Nazanin', 14)
                                   )
    lbl_employee_marital_status.place(x=90, y=275)

    lbl_employee_children = Label(frm3_right,
                                  text='',
                                  bg='silver',
                                  font = ('B Nazanin', 14)
                                 )
    lbl_employee_children.place(x=90, y=335)


    lbl_employee_position = Label(frm3_right,
                                  text='',
                                  bg='silver',
                                  font = ('B Nazanin', 14)
                                  )
    lbl_employee_position.place(x=90, y=395)


    lbl_employee_insurance = Label(frm3_right,
                                   text='',
                                   bg='silver',
                                   font = ('B Nazanin', 14)
                                   )
    lbl_employee_insurance.place(x=90, y=455)
        

# Right frame

    frm_right = Frame(payroll_win,
        bg='gainsboro',
        width=700,
        height=1080
    )

    frm_right.place(x=1170, y=0)


    btn1 = Button(frm_right,
                  text='ثبت نام کاربر',
                  width=15,
                  height=2,
                  command = go_employee
                  )
    btn1.place(x=100, y=300)

    btn2 = Button(frm_right,
                  text='محاسبه حقوق',
                  width=15,
                  height=2,
                  command = go_payroll
                  )
    btn2.place(x=100, y=360)

    btn3 = Button(frm_right,
                  text='دريافت فيش',
                  width=15,
                  height=2,
                  command = go_report
                  )
    btn3.place(x=100, y=420)


#دکمه هاي ثبت نهايي و پاک کردن فرم

    btn4 = Button(payroll_win,
                  text='ذخيره اطلاعات',
                  width=15,
                  height=2,
                  state='disabled',
                  command=save_payroll
                  )

    btn4.place(x=40, y=750)


    btn5 = Button(payroll_win,
                  text='پاک کردن فرم',
                  width=15,
                  height=2,
                  state='disabled',
                  command = clear_payroll_form
                  )
    btn5.place(x=170, y=750)

    btn6 = Button(payroll_win,
                  text = 'محاسبه عملکرد',
                  width = 15,
                  height = 2,
                  state='disabled',
                  command = calculate_payroll
                  )

    btn6.place(x=300, y=750)


# 4. Report page

def report_page():

    win.withdraw()

    report_win = Toplevel(win)

    report_win.title('مشاهده فيش حقوقي')
    report_win.configure(bg='silver')
    report_win.iconbitmap('cool_bitty_kitty.ico')
    report_win.state('zoomed')


#توابع مربوط به سه دکمه دسترسي سريع در منو سمت راست


    def go_employee():

        report_win.withdraw()
        employee_page()


    def go_payroll():

        report_win.withdraw()
        payroll_page()


    def go_report():
        payroll_win.withdraw()
        report_page()


# تابع دکمه جستجو

    def search_employee():

        national_id = ent1.get()

        file = open('payroll.txt', 'r', encoding='utf-8')

        found = False

        for i in file:

            if national_id in i:

                found = True

                full_name = i.split("'employee_name': '")[1].split("'")[0]
                job_title = i.split("'job_title': '")[1].split("'")[0]
                national_id = i.split("'national_id': '")[1].split("'")[0]

                lbl6.config(text=full_name)
                lbl7.config(text=job_title)
                lbl8.config(text=national_id)

                ent_year.config(state='readonly')
                ent_month.config(state='readonly')

                btn_form_delete.config(state='normal')
                btn_show_payroll.config(state='disabled')

        file.close()
        if found == False:

            messagebox.showerror(
                                 'کاربر ثبت نشده است.')      

#تابع بررسي انتخاب سال و ماه
            
    def check_year_month(event=None):

        if ent_year.get() != '' and ent_month.get() != '':
            btn_show_payroll.config(state='normal')
        else:
            btn_show_payroll.config(state='disabled')
            

############### تابع فيش حقوقي نهايي

    def show_payroll_page(national_id, month, year):

        see_payroll_win = Toplevel(report_win)

        see_payroll_win.title('مشاهده فيش حقوقي')
        see_payroll_win.iconbitmap('cool_bitty_kitty.ico')
        see_payroll_win.configure(bg='silver')
        see_payroll_win.geometry('1000x750')
        see_payroll_win.resizable(False, False)
        see_payroll_win.attributes('-topmost', True)

        see_payroll_win.grab_set()
        employee_name = ''
        job_title = ''
        service_unit = ''

        file = open('employees.txt', 'r', encoding='utf-8')

        for i in file:

            if "'national_id': '" + national_id + "'" in i:

                employee_name = i.split("'full_name': '")[1].split("'")[0]
                job_title = i.split("'job_title': '")[1].split("'")[0]
                service_unit = i.split("'service_unit': '")[1].split("'")[0]

                break

        file.close()


# گرفتن اطلاعات فیش از payroll.txt

        file = open('payroll.txt', 'r', encoding='utf-8')

        for i in file:

            if "'national_id': '" + national_id + "'" in i:

                if "'month': '" + month + "'" in i:

                    if "'year': '" + year + "'" in i:

                        daily_hours = i.split("'daily_hours': ")[1].split(",")[0]
                        holiday_hours = i.split("'holiday_hours': ")[1].split(",")[0]
                        night_hours = i.split("'night_hours': ")[1].split(",")[0]
                        mission_hours = i.split("'mission_hours': ")[1].split(",")[0]

                        monthly_hours = i.split("'monthly_hours': ")[1].split(",")[0]
                        worked_hours = i.split("'worked_hours': ")[1].split(",")[0]
                        overtime_hours = i.split("'overtime_hours': ")[1].split(",")[0]
                        deficit_hours = i.split("'deficit_hours': ")[1].split(",")[0]

                        base_salary = i.split("'base_salary': ")[1].split(",")[0]
                        bonus = i.split("'bonus': ")[1].split(",")[0]
                        food = i.split("'food': ")[1].split(",")[0]
                        child = i.split("'child': ")[1].split(",")[0]
                        overtime = i.split("'overtime': ")[1].split(",")[0]
                        night = i.split("'night': ")[1].split(",")[0]
                        holiday = i.split("'holiday': ")[1].split(",")[0]
                        mission = i.split("'mission': ")[1].split(",")[0]
                        gross_salary = i.split("'gross_salary': ")[1].split(",")[0]

                        insurance = i.split("'insurance': ")[1].split(",")[0]
                        tax = i.split("'tax': ")[1].split(",")[0]
                        deficit_amount = i.split("'deficit_amount': ")[1].split(",")[0]
                        total_deductions = i.split("'total_deductions': ")[1].split(",")[0]

                        break

        file.close()

        
        frame_see_payroll = Frame(see_payroll_win,
                                  bg='white',
                                  relief='sunken',
                                  bd=3
                                  )

        frame_see_payroll.place(relx=0.5,
                                rely=0.5,
                                anchor='center',
                                width=1000,
                                height=750
                                )

        top_frame_see = Frame(frame_see_payroll,
                              bg='white'
                              )

        top_frame_see.place(x=0,
                            y=0,
                            width=1000,
                            height=60
                            )

        line = Frame(frame_see_payroll, bg='black')

        line.place(x=0,
                   y=60,
                   width=1000,
                   height=2
                   )
        top_frame_infos = Frame(frame_see_payroll, bg='white')

        top_frame_infos.place(x=0,
                            y=63,
                            width=1000,
                            height=110
                            )

        line2 = Frame(frame_see_payroll, bg='black')

        line2.place(x=0,
                   y=174,
                   width=1000,
                   height=2
                   )

        salary_box_right = LabelFrame(frame_see_payroll,
                                text = 'کارکرد (ساعت)',
                                bg='white',
                                labelanchor = 'n',
                                font = ('B nazanin', 14,),
                                width=300,
                                height=465
                                )
        salary_box_right.place (x = 670, y = 180)

        salary_box_mid = LabelFrame(frame_see_payroll,
                                text = 'مزا يا(ريال)',
                                bg='white',
                                labelanchor = 'n',
                                font = ('B nazanin', 14,),
                                width=300,
                                height=465
                                )
        salary_box_mid.place (x = 350, y = 180)


        salary_box_left = LabelFrame(frame_see_payroll,
                                text = ' کسورات  (ريال)',
                                bg='white',
                                labelanchor = 'n',
                                font = ('B nazanin', 14,),
                                width=300,
                                height=465
                                )
        salary_box_left.place (x = 30, y = 180)

        
# Label of top_frame_see


        title_label = Label(top_frame_see,
                                text='فيش حقوقي',
                                bg='white',
                                font= ('B nazanin', 14))
        title_label.place(x=650, y=30, anchor='e')


        title_label_month = Label(top_frame_see,
                     text='',
                     width = 10,
                     bg='white',
                     font = ('B nazanin' ,14)
                     )

        title_label_month.place(x=570, y=30, anchor='e')


        title_label_year = Label(top_frame_see,
                                 text='',
                                 width = 10,
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        title_label_year.place(x=460, y=30, anchor='e')



#Labels of top_frame_infos
        
        salary_box_label1 = Label(top_frame_infos,
                                text='نام و نام خانوادگي',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label1.place(x=940, y=25, anchor='e')        
        
        
        salary_box_label2 = Label(top_frame_infos,
                                text='شماره ملي',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label2.place(x=940, y=85, anchor='e')


        salary_box_label3 = Label(top_frame_infos,
                                text='سمت شغلي',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label3.place(x=490, y=25, anchor='e')


        salary_box_label4 = Label(top_frame_infos,
                                text='محل خدمت',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label4.place(x=490, y=85, anchor='e')


#ليبل هاي ظاهر شونده top_frame_infos


        salary_box_show1 = Label(top_frame_infos,
                     text='',
                     width = 20,
                     bg='white',
                     font = ('B nazanin' ,14)
                     )

        salary_box_show1.place(x=800, y=25, anchor='e')


        salary_box_show2 = Label(top_frame_infos,
                                 text='',
                                 width = 20,
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show2.place(x=800, y=85, anchor='e')


        salary_box_show3 = Label(top_frame_infos,
                                 text='',
                                 width = 30,
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show3.place(x=350, y=25, anchor='e')


        salary_box_show4 = Label(top_frame_infos,
                                 text='',
                                 width = 30,
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show4.place(x=350, y=85, anchor='e')

        salary_box_show1.config(text=employee_name)
        salary_box_show2.config(text=national_id)
        salary_box_show3.config(text=job_title)
        salary_box_show4.config(text=service_unit)

        title_label_month.config(text=month)
        title_label_year.config(text=year)

        

#Labels of  salary_box_right

        salary_box_label1 = Label(salary_box_right,
                                text='کارکرد موثر ماه',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label1.place(x=290, y=15, anchor='e')        
        
        
        salary_box_label2 = Label(salary_box_right,
                                text='کارکرد روزانه',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label2.place(x=290, y=60, anchor='e')


        salary_box_label3 = Label(salary_box_right,
                                text='ساعت اضافه کاري',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label3.place(x=290, y=110, anchor='e')


        salary_box_label4 = Label(salary_box_right,
                                text='ساعت کسر کار',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label4.place(x=290, y=160, anchor='e')


        salary_box_label5 = Label(salary_box_right,
                                text='ساعت کار روزهاي',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label5.place(x=290, y=210, anchor='e')

        salary_box_label6 = Label(salary_box_right,
                                text='تعطيل',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label6.place(x=290, y=240, anchor='e')

        salary_box_label7 = Label(salary_box_right,
                                text='ساعت شب کاري',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label7.place(x=290, y=290, anchor='e')

        salary_box_label8 = Label(salary_box_right,
                                text='ساعت ماموريت',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label8.place(x=290, y=340, anchor='e')

        

# ليبل هاي ظاهر شونده Salary Box right


        salary_box_show1 = Label(salary_box_right,
                     text='',
                     bg='white',
                     font = ('B nazanin' ,14)
                     )

        salary_box_show1.place(x=110, y=15, anchor='e')


        salary_box_show2 = Label(salary_box_right,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show2.place(x=110, y=60, anchor='e')


        salary_box_show3 = Label(salary_box_right,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show3.place(x=110, y=110, anchor='e')


        salary_box_show4 = Label(salary_box_right,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show4.place(x=110, y=160, anchor='e')

        salary_box_show5 = Label(salary_box_right,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show5.place(x=110, y=240, anchor='e')


        salary_box_show6 = Label(salary_box_right,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show6.place(x=110, y=240, anchor='e')


        salary_box_show7 = Label(salary_box_right,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show7.place(x=110, y=290, anchor='e')


        salary_box_show8 = Label(salary_box_right,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show8.place(x=110, y=340, anchor='e')


        salary_box_show1.config(text=worked_hours)
        salary_box_show2.config(text=daily_hours)
        salary_box_show3.config(text=overtime_hours)
        salary_box_show4.config(text=deficit_hours)
        salary_box_show5.config(text=holiday_hours)
        salary_box_show6.config(text=holiday_hours)
        salary_box_show7.config(text=night_hours)
        salary_box_show8.config(text=mission_hours)



#Labels of  salary_box_mid
        
        salary_box_label1 = Label(salary_box_mid,
                                text='حقوق پايه',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label1.place(x=290, y=15, anchor='e')        
        
        
        salary_box_label2 = Label(salary_box_mid,
                                text='کارانه',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label2.place(x=290, y=60, anchor='e')


        salary_box_label3 = Label(salary_box_mid,
                                text='حق خوار و بار',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label3.place(x=290, y=110, anchor='e')


        salary_box_label4 = Label(salary_box_mid,
                                text='حق اولاد',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label4.place(x=290, y=160, anchor='e')


        salary_box_label5 = Label(salary_box_mid,
                                text='اضافه کاري',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label5.place(x=290, y=210, anchor='e')

        salary_box_label6 = Label(salary_box_mid,
                                text='شب کاري',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label6.place(x=290, y=260, anchor='e')

        salary_box_label7 = Label(salary_box_mid,
                                text='کار در روز تعطيل',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label7.place(x=290, y=310, anchor='e')


        salary_box_label8 = Label(salary_box_mid,
                                text='حق ماموريت',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label8.place(x=290, y=360, anchor='e')


        salary_box_label9 = Label(salary_box_mid,
                                text='جمع کُل',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label9.place(x=290, y=410, anchor='e')



####ليبل هاي ظاهرشونده salary box mid

        salary_box_show1 = Label(salary_box_mid,
                     text='',
                     bg='white',
                     font = ('B nazanin' ,14)
                     )

        salary_box_show1.place(x=110, y=15, anchor='e')


        salary_box_show2 = Label(salary_box_mid,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show2.place(x=110, y=60, anchor='e')


        salary_box_show3 = Label(salary_box_mid,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show3.place(x=110, y=110, anchor='e')


        salary_box_show4 = Label(salary_box_mid,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show4.place(x=110, y=160, anchor='e')

        salary_box_show5 = Label(salary_box_mid,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show5.place(x=110, y=210, anchor='e')


        salary_box_show6 = Label(salary_box_mid,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show6.place(x=110, y=260, anchor='e')


        salary_box_show7 = Label(salary_box_mid,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show7.place(x=110, y=310, anchor='e')


        salary_box_show8 = Label(salary_box_mid,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show8.place(x=110, y=360, anchor='e')


        salary_box_show9 = Label(salary_box_mid,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show9.place(x=110, y=410, anchor='e')

        salary_box_show1.config(text=base_salary)
        salary_box_show2.config(text=bonus)
        salary_box_show3.config(text=food)
        salary_box_show4.config(text=child)
        salary_box_show5.config(text=overtime)
        salary_box_show6.config(text=night)
        salary_box_show7.config(text=holiday)
        salary_box_show8.config(text=mission)
        salary_box_show9.config(text=gross_salary)


#Labels of  salary_box_left

        salary_box_label1 = Label(salary_box_left,
                                text='سهم بيمه کارمند',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label1.place(x=290, y=15, anchor='e')        
        
        
        salary_box_label2 = Label(salary_box_left,
                                text='ماليات',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label2.place(x=290, y=60, anchor='e')


        salary_box_label3 = Label(salary_box_left,
                                text='کسر کار',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label3.place(x=290, y=110, anchor='e')

        salary_box_label4 = Label(salary_box_left,
                                text='جمع کُل',
                                bg='white',
                                font= ('B nazanin', 14))
        salary_box_label4.place(x=290, y=160, anchor='e')


####ليبل هاي ظاهرشونده salary box left

        salary_box_show1 = Label(salary_box_left,
                     text='',
                     bg='white',
                     font = ('B nazanin' ,14)
                     )

        salary_box_show1.place(x=110, y=15, anchor='e')


        salary_box_show2 = Label(salary_box_left,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show2.place(x=110, y=60, anchor='e')


        salary_box_show3 = Label(salary_box_left,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show3.place(x=110, y=110, anchor='e')


        salary_box_show4 = Label(salary_box_left,
                                 text='',
                                 bg='white',
                                 font = ('B nazanin' ,14)
                                 )

        salary_box_show4.place(x=110, y=160, anchor='e')

        salary_box_show1.config(text=insurance)
        salary_box_show2.config(text=tax)
        salary_box_show3.config(text=deficit_amount)
        salary_box_show4.config(text=total_deductions)



######## تابع چک کردن فيش حقوقي ################
        
    def check_payroll():

        month = ent_month.get()
        year = ent_year.get()

        national_id = ent1.get()

        file = open('payroll.txt', 'r', encoding='utf-8')

        for i in file:

            if "'national_id': '" + national_id + "'" in i:

                break

        else:

            file.close()

            messagebox.showerror(
                'خطا',
                'کاربر ثبت نشده است'
                )

            return

        file.close()


        file = open('payroll.txt', 'r', encoding='utf-8')

        for i in file:

            if "'national_id': '" + national_id + "'" in i:

                if "'month': '" + month + "'" in i:

                    break

        else:

            file.close()

            messagebox.showerror(
                'خطا',
                'برای این ماه فیش حقوقی ثبت نشده است'
                )

            return

        file.close()


        file = open('payroll.txt', 'r', encoding='utf-8')

        for i in file:

            if "'national_id': '" + national_id + "'" in i:

                if "'month': '" + month + "'" in i:

                    if "'year': '" + year + "'" in i:

                        file.close()

                        show_payroll_page(national_id, month, year)

                        break

        else:

            file.close()

            messagebox.showerror(
                'خطا',
                'برای این سال فیش حقوقی ثبت نشده است'
                )

        
# تابع دکمه پاک کردن فرم صفحه گزارش


    def clear_report_form():

        ent1.delete(0, END)

        ent_year.set('')
        ent_month.set('')

        ent_year.config(state='disabled')
        ent_month.config(state='disabled')

        lbl6.config(text='')
        lbl7.config(text='')
        lbl8.config(text='')

        btn_form_delete.config(state='disabled')
        btn_show_payroll.config(state='disabled')
        btn_search_report.config(state='disabled')

        ent1.focus()

#تابع چک کردن طول شماره ملي
        
    def check_national_id_length(event=None):

        text = ent1.get()

        if len(text) > 10:
            ent1.delete(10, END)

        if len(ent1.get()) == 10:
            btn_search_report.config(state='normal')
        else:
            btn_search_report.config(state='disabled')        
# Top frame

    frm = LabelFrame(report_win,
                text = 'جستجوي کارمند',
                bg='silver',
                labelanchor = 'n',
                font = ('B nazanin', 14,),
                width=500,
                height=130
                )

    frm.place(x=750, y=100, anchor='n')


    lbl1 = Label(frm,
                 text='لطفا شماره ملي کارمند را اينجا وارد کنيد',
                 bg='silver',
                 font= ('B nazanin', 14)
                 )

    lbl1.place(x=490, y=40, anchor='e')


    ent1 = Entry(frm, width=13, bg='white', font = ('B nazanin', 12))
    ent1.place(x=215, y=40, anchor='e')

    ent1.bind('<KeyRelease>', check_national_id_length)


    btn_search_report = Button (frm,
                  text='جستجو',
                  width=8,
                  height=1,
                  state='disabled',
                  command = search_employee)
    btn_search_report.place(x=80, y=40, anchor='e')


############################################

    frm2_mid = LabelFrame(report_win,
        text = 'اطلاعات کارمند',
        bg='silver',
        labelanchor = 'n',
        font = ('B nazanin', 16,),
        width=500,
        height=220
        )

    frm2_mid.place(x=750, y=250, anchor='n')


    lbl3 = Label(frm2_mid,
                 text='نام و نام خانوادگي',
                 bg='silver',
                 font=('B nazanin', 14)
                 )

    lbl3.place(x=490, y=30, anchor='e')


    lbl4 = Label(frm2_mid,
                 text='عنوان شغلي',
                 bg='silver',
                 font=('B nazanin', 14)
                 )

    lbl4.place(x=490, y=80, anchor='e')


    lbl4 = Label(frm2_mid,
                 text='شماره ملي',
                 bg='silver',
                 font=('B nazanin', 14)
                 )

    lbl4.place(x=490, y=130, anchor='e')

############  ليبل هاي ظاهر شونده #################


    lbl6 = Label(frm2_mid,
                 text='',
                 bg='silver',
                 font = ('B nazanin' ,14)
                 )

    lbl6.place(x=250, y=30, anchor='e')


    lbl7 = Label(frm2_mid,
                 text='',
                 bg='silver',
                 font = ('B nazanin' ,14)
                 )

    lbl7.place(x=250, y=80, anchor='e')


    lbl8 = Label(frm2_mid,
                 text='',
                 bg='silver',
                 font = ('B nazanin' ,14)
                 )

    lbl8.place(x=250, y=130, anchor='e')



    ent2 = Entry(frm2_mid, width=15, bg='white')
    ent2.place(x=850, y=30, anchor='e')


###########################################

# Right frame

    frm_right = Frame(report_win,
        bg='gainsboro',
        width=700,
        height=1080
        )

    frm_right.place(x=1170, y=0)

    btn_employee = Button(frm_right, text='ثبت نام کاربر',
                  width=15,
                  height=2,
                  command = go_employee
                  )
    btn_employee.place(x=100, y=300)

    btn2 = Button(frm_right,
                  text='محاسبه حقوق',
                  width=15,
                  height=2,
                  command = go_payroll
                  )
    btn2.place(x=100, y=360)

    btn3 = Button(frm_right,
                  text='دريافت فيش',
                  width=15,
                  height=2,
                  command = go_report
                  )
    btn3.place(x=100, y=420)

###########################################

# Bottom frame

    frm_bottom = LabelFrame(report_win,
                text = 'جزئيات فيش حقوقي',
                bg='silver',
                labelanchor = 'n',
                font = ('B nazanin', 14,),
                width=500,
                height=130
                )

    frm_bottom.place(x=750, y=530, anchor='n')


    lbl3 = Label(frm_bottom,
                 text = 'لطفا سال و ماه را انتخاب کنيد',
                 bg = 'silver',
                 font = ('B nazanin', 14)
                 )
    lbl3.place(x=490, y=40, anchor='e')

    ent_year = ttk.Combobox(frm_bottom,
                            font=('B nazanin', 8),
                            values=('1405', '1406'),
                            width=12,
                            state='disabled'
                            )
    ent_year.place(x=300, y=40, anchor='e')
    ent_year.bind('<<ComboboxSelected>>', check_year_month)


    ent_month = ttk.Combobox(frm_bottom,
                             font=('B nazanin', 8),
                             values=('فروردين', 'ارديبهشت', 'خرداد', 'تير',
                                     'مرداد', 'شهريور', 'مهر', 'آبان',
                                     'آذر', 'دي', 'بهمن', 'اسفند'),
                             width=12,
                             state='disabled'
                             )
    ent_month.place(x=180, y=40, anchor='e')
    ent_month.bind('<<ComboboxSelected>>', check_year_month)


    btn_show_payroll = Button(frm_bottom,
                              text = 'مشاهده',
                              width = 8,
                              height = 1,
                              state='disabled',
                              command = check_payroll
                              )
    
    btn_show_payroll.place(x=80, y=40, anchor='e')

# دکمه پاک کردن فرم 

    btn_form_delete = Button(report_win,
                             text = 'پاک کردن فرم',
                             width = 15,height=2,
                             state='disabled',
                             command = clear_report_form,
                             )

    btn_form_delete.place(x=500, y=670)
    

main_page()

win.mainloop()
