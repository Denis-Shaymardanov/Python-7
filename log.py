from datetime import datetime

def write(data: str):
    file = 'log.txt'
    with open(file, 'a', encoding='UTF-8') as f:
        now = f"{datetime.now():%Y-%m-%d %H:%M}"
        f.writelines(f'{now} {data} \n')
        
