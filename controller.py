import func 

def directory():
     oper = int(input('1 - Добавить контакт \n2 - Удалить контакт \n3 - Найти котакт \n4 - Показать все контакты \n5 - Выход \n Введите, что вы хотите сделать 1-5: '))
     while oper <= 5:
          if oper == 1:
               func.get_add()
          elif oper == 2:
               func.get_del()
          elif oper == 3:
               func.get_find()
          elif oper == 4:
               func.get_see()
          if oper == 5:
               print('Спасибо, что выбрали наш Продукт')
               break
          oper = int(input('1 - Добавить контакт \n 2 - Удалить контакт \n 3 - Найти котакт \n 4 - Показать все контакты \n 5 - Выход \n Введите, что вы хотите сделать 1-5: '))
            

    
    
      
