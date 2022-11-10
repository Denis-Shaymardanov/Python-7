import func, log

def directory():
     oper = int(input('1 - Добавить контакт \n2 - Удалить контакт \n3 - Найти контакт \n4 - Показать все контакты \n5 - Выход \n Введите, что вы хотите сделать 1-5: '))
     while oper <= 5:
          if oper == 1:
               func.get_add()
               log.input_write("Добавили новый контакт")
          elif oper == 2:
               func.get_del()
               log.input_write("Удалили контакт")
          elif oper == 3:
               func.get_find()
               log.input_write("Нашли контакт")
          elif oper == 4:
               func.get_see()
               log.input_write("Показали все контакты")
          if oper == 5:
               print('Спасибо, что выбрали наш Продукт')
               log.input_write("Вышли из программы")
               break
          oper = int(input('1 - Добавить контакт \n 2 - Удалить контакт \n 3 - Найти контакт \n 4 - Показать все контакты \n 5 - Выход \n Введите, что вы хотите сделать 1-5: '))     
