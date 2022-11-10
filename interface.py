from tkinter import *
import func as f
import log

def add_contact():
    cont_inf = []
    cont_inf.append(Entry.get(entry_name))
    cont_inf.append(Entry.get(entry_last_name))
    cont_inf.append(Entry.get(entry_phone))
    cont_inf.append(Entry.get(entry_comment))

    f.add_contact(cont_inf)
    log.write(f'Добавлен контакт {cont_inf[0]} {cont_inf[1]}')

    window.destroy()

def delete_contact():
    number = int(Entry.get(entry_number))
    
    f.delete_contact(contacts, number)
    log.write(f'Удален контакт')

    window.destroy()

def find_contact():
    result = f.find_contact(Entry.get(entry_word))

    for i in range(0, len(result)):
        label = Label(window, text=result[i]).grid(row=2+i, column=0)

def button_add_contact():
    global window
    global entry_name
    global entry_last_name
    global entry_phone
    global entry_comment

    window = Toplevel()
    window.title('Добавить контакт')
    window.geometry('400x240')
    window.resizable(0,0)

    window.columnconfigure(index=0, weight=50)
    window.columnconfigure(index=1, weight=250)

    name_label = Label(window, text='Фамилия')
    last_name_label = Label(window, text='Имя')
    phone_label = Label(window, text='Телефон')
    comment_label = Label(window, text='Комментарий')

    name_label.grid(row=0, column=0, sticky = 'e')
    last_name_label.grid(row=1, column=0, sticky = 'e')
    phone_label.grid(row=2, column=0, sticky = 'e')
    comment_label.grid(row=3, column=0, sticky = 'e')

    entry_name = Entry(window)
    entry_last_name = Entry(window)
    entry_phone = Entry(window)
    entry_comment = Entry(window)

    entry_name.grid(row=0, column=1, sticky = 'w')
    entry_last_name.grid(row=1, column=1, sticky = 'w')
    entry_phone.grid(row=2, column=1, sticky = 'w')
    entry_comment.grid(row=3, column=1, sticky = 'w')

    btn = Button(window, text='Добавить',command = add_contact)
    btn.grid(row=4, columnspan=2)
    window.mainloop()

def button_delete_contact():
    global window
    global entry_number
    global contacts

    window = Toplevel()
    window.title('Удалить контакт')
    window.geometry('400x240')
    window.resizable(0,0)

    contacts = f.get_contacts()
    for i in range(0, len(contacts)):
        label_contact_number = Label(window, text=i+1).grid(row=i, column=0)
        label_contact = Label(window, text=contacts[i]).grid(row=i, column=1)    

    label_number = Label(window, text="Введите номер контакта").grid(row=i+1, column=0, sticky = 'e')
    entry_number = Entry(window)
    entry_number.grid(row=i+1, column=1, sticky = 'w')   
    btn = Button(window, text='Удалить',command = delete_contact)
    btn.grid(column=2, row=i+1,  sticky = 'w')
    window.mainloop()

def button_find_contact():
    global window
    global entry_word

    window = Toplevel()
    window.title('Найти контакт')
    window.geometry('400x240')
    window.resizable(0,0)

    label_word = Label(window, text="Введите слово для поиска").grid(row=0, column=0, sticky = 'e')
    entry_word = Entry(window)
    entry_word.grid(row=0, column=1, sticky = 'w')   
    btn = Button(window, text='Найти',command = find_contact)
    btn.grid(column=2, row=0,  sticky = 'w')
    window.mainloop()

def button_show_all():

    window = Toplevel()
    window.title("Контакты")
    window.geometry('400x240')
    window.resizable(0,0)

    contacts = f.get_contacts()
    for i in range(0, len(contacts)):
        label_contact = Label(window, text=contacts[i]).grid(row=i, column=1)    

    window.mainloop()    
                
def quit(window):
    window.destroy()

def start():
    
    window = Tk()
    window.title("Телефонный справочник")
    window.geometry('800x600')
    
    lbl = Label(window, text="Выберите действие:", font=("Helvetica", 14)).grid(columnspan=2, row=0)
    btn_add = Button(window, text = 'Создать контакт',font=("Helvetica", 12),command =button_add_contact, height=1, width=25).grid(column= 1, row  = 1) 
    btn_del = Button(window, text = 'Удалить контакт',font=("Helvetica", 12),command =button_delete_contact, height=1, width=25).grid(column= 1, row  = 2) 
    btn_find = Button(window, text = 'Найти контакт',font=("Helvetica", 12),command =button_find_contact, height=1, width=25).grid(column= 1, row  = 3)
    btn_see =  Button(window, text = 'Вывести контакты',font=("Helvetica", 12),command = button_show_all, height=1, width=25).grid(column= 1, row  = 4) 
    btn_exit = Button(window, text = 'Выход',font=("Helvetica", 12),command = window.quit, height=1, width=25).grid(column= 1, row  = 6) 
      
    window.mainloop()