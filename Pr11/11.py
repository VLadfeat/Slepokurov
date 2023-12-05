import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

win = tk.Tk()
win.title('Слепокуров Владислав Сергеевич')
win.geometry('1500x1500')

tab_control = ttk.Notebook(win)# Виджет с несколькими вкладками
tb1 = ttk.Frame(tab_control)
tb2 = ttk.Frame(tab_control)
tb3 = ttk.Frame(tab_control)

tab_control.add(tb1, text='1 вкладка')# Создание вкладок
tab_control.add(tb2, text='2 вкладка')
tab_control.add(tb3, text='3 вкладка')

tab_control.pack(expand=True, fill='both')# Расширение на всю длину

# Калькулятор
def calculate():
    n1 = float(entry1.get())# Ввод 1-го числа
    n2 = float(entry2.get())# Ввод 2-го числа
    operation = operation_var.get()
    if operation == '+':
        resultat = n1 + n2
    elif operation == '-':
        resultat = n1 - n2
    elif operation == '*':
        resultat = n1 * n2
    elif operation == '/':
        resultat = n1 / n2
    result_label.config(text='Ответ: ' + str(resultat))

# Создание вкладки с калькулятором
entry1 = tk.Entry(tb1)# Принятие 1-го числа
entry1.pack()
entry2 = tk.Entry(tb1)# Принятие 2-го числа
entry2.pack()
operation_var = tk.StringVar(tb1)# Отслеживание операций
operation_var.set('+')
operation_menu = tk.OptionMenu(tb1, operation_var, '+', '-', '*', '/')# Меню с операциями
operation_menu.pack()
calculate_button = tk.Button(tb1, text='Тыкни', command=calculate)
calculate_button.pack()
result_label = tk.Label(tb1, text='Ответ: ')
result_label.pack()

# Выбор чекбоксов
def show_checkbox():
    if checkbox1_var.get() == 1:
        messagebox.showinfo('Выбор', 'Вы выбрали первый вариант')
    if checkbox2_var.get() == 1:
        messagebox.showinfo('Выбор', 'Вы выбрали второй вариант ')
    if checkbox3_var.get() == 1:
        messagebox.showinfo('Выбор', 'Вы выбрали третий вариант ')

# Чекбоксы
checkbox1_var = tk.IntVar()
checkbox2_var = tk.IntVar()
checkbox3_var = tk.IntVar()
checkbox1 = tk.Checkbutton(tb2, text='Первый вариант', variable=checkbox1_var)# Флажок выбора 1
checkbox1.pack()
checkbox2 = tk.Checkbutton(tb2, text='Второй вариант', variable=checkbox2_var)# Флажок выбора 2
checkbox2.pack()
checkbox3 = tk.Checkbutton(tb2, text='Третий вариант', variable=checkbox3_var)# Флажок выбора 3
checkbox3.pack()
show_button = tk.Button(tb2, text='Клик', command=show_checkbox)# Показывает, что выбрано
show_button.pack()

# Текст
def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text = file.read()
        text_box.delete(1, 'end')# Удаляет все, с начала до конца
        text_box.insert('end', text)# Вставляет текст из файла


# Вкладка с текстом
menu_bar = tk.Menu(win)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
menu_bar.add_cascade(label="Файл", menu=file_menu)
win.config(menu=menu_bar)

text_box = tk.Text(tb3)
text_box.pack()
win.mainloop()