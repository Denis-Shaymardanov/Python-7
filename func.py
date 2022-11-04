import view

def get_add():
    list = ['Фамилию: ','Имя: ','номер телефона: ','коментарий']
    data = view.get_input(list)
    with open('people.csv', 'a', encoding = 'UTF-8') as file:
        file.writelines(
            f'{data[0]} {data[1]} {data[2]} {data[3]} \n')
    with open('people.txt', 'a', encoding = 'UTF-8') as file:
        file.writelines(
            f'{data[0]} {data[1]} {data[2]} {data[3]} \n')

def get_see():
    with open('people.csv', 'r', encoding = 'UTF-8') as file:
        list = []
        list = ''.join(file.readlines())
        print(list)

def get_find():
    with open('people.csv', 'r', encoding = 'UTF-8') as file:
        data = []
        data = file.readlines()
        text = input('Введите слово для поиска: \n')
        for i in range(len(data)):
            data[i] = ''.join(data[i])
            row = []
            row = data[i]
            if text in row:
                print(f'N {i+1} : {row}')
        
def get_del():
    with open('people.csv', 'r', encoding = 'UTF-8') as file:
        data = []
        data = file.readlines()
        print('-'*100)
        for i in range(len(data)):
            print(f'№ {i+1} |{data[i]}')
    number = int(input('Введите номер контакта для удаления: '))
    n = number-1
    data.pop(n)
    print('Вы удалили контакт')
    for i in range(len(data)):
            print(f'№ {i+1} |{data[i]}')
    with open('people.txt', 'w', encoding = 'UTF-8') as file:
        file.writelines(data)
    with open('people.csv', 'w', encoding = 'UTF-8') as file:
        file.writelines(data)