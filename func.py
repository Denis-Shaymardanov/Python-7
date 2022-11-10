def add_contact(data):
    with open('people.csv', 'a', encoding = 'UTF-8') as file:
        file.writelines(
            f'{data[0]} {data[1]} {data[2]} {data[3]} \n')
    with open('people.txt', 'a', encoding = 'UTF-8') as file:
        file.writelines(
            f'{data[0]} {data[1]} {data[2]} {data[3]} \n')

def get_contacts():
    with open('people.csv', 'r', encoding = 'UTF-8') as file:
        data = []
        data = file.readlines()

    return data

def delete_contact(data, number):
    n = number-1
    data.pop(n)
 
    with open('people.txt', 'w', encoding = 'UTF-8') as file:
        file.writelines(data)
    with open('people.csv', 'w', encoding = 'UTF-8') as file:
        file.writelines(data)

def find_contact(word):
    result = []
    with open('people.csv', 'r', encoding = 'UTF-8') as file:
        data = []
        data = file.readlines()
        for i in range(len(data)):
            data[i] = ''.join(data[i])
            row = []
            row = data[i]
            if word in row:
                result.append(f'N {i+1} : {row}')

    return result