import requests
import json
import math

base_url = "http://10.10.239.113:8000/api/v1.0"
tasks_url = "http://10.10.239.113:8000/api/v1.0/tasks"
start_url = "http://10.10.239.113:8000/api/v1.0/start"
answer_url = "http://10.10.239.113:8000/api/v1.0/answer"
file = 'full_ascii.txt'
decorator = 'decorator.py'
converter = 'Converter.py'
dz_classmethod = 'new_last-task.py'


def make_ascii(filename, part_ascii):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        file.write(part_ascii)


def get_task(url):
    response = requests.get(url).json()
    print(f"Название задачи: {response['name']} \nЗадание: {response['description']} \nЗначения: {response['variables']} \nФомат ответа: {response.get('answer format')}")
    return {'taskname': response['name'], 'variables': response['variables']}


def send_answer(taskname, answer):
    json_data = json.dumps({'name': taskname, 'values': answer})
    print('--------------------------------------------------------------')
    print(json_data)
    print('--------------------------------------------------------------')
    response = requests.post(answer_url, json=json_data).json()
    print(f"Ответ: {response['answer']} \nСледующая задача: {base_url}{response['next_url']}")
    make_ascii(file, response['saveit'])
    return f"{base_url}{response['next_url']}"


def solve_equation(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return {'x1': '', 'x2': ''}
    elif d > 0:
        x1 = (- b + math.sqrt(d)) / (2 * a)
        x2 = (- b - math.sqrt(d)) / (2 * a)
        return {'x1': x1, 'x2': x2 }
    else:
        x = (- b + math.sqrt(d)) / (2 * a)
        return {'x1': x, 'x2': ''}


def search_fib(n):
    fib1 = fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    return {'F': fib2}
    

def polyndromes_even(n):
    even_list = []
    start_num = int('1' + '0' * (n - 1))
    stop_num = int('1' + '0' * n)
    l_num = [i for i in range(start_num, stop_num, 2)]
    for i in l_num:
        if str(i) == str(i)[::-1]:
            even_list.append(i)
    even_list.sort(reverse=True)
    return {'lst': even_list}


def decorator_json(filename):
     with open(filename, 'r', encoding='utf-8') as file:
        reader = file.read()
        return {'decorator': reader}


def send_weight(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = file.read()
        return {'static': reader}


def send_class(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = file.read()
        return {'class': reader}


start_task = get_task(start_url)
next_url = send_answer(start_task['taskname'], solve_equation(start_task['variables']['a'], start_task['variables']['b'], start_task['variables']['c']))

new_task = get_task(next_url)
next_url = send_answer(new_task['taskname'], search_fib(new_task['variables']['n']))

new_task = get_task(next_url)
next_url = send_answer(new_task['taskname'], polyndromes_even(new_task['variables']['n']))

new_task = get_task(next_url)
next_url = send_answer(new_task['taskname'], decorator_json(decorator))

new_task = get_task(next_url)
next_url = send_answer(new_task['taskname'], send_weight(converter))

new_task = get_task(next_url)
next_url = send_answer(new_task['taskname'], send_class(dz_classmethod))

new_task = get_task(next_url)

x = new_task['variables']['command'] 
exec(x)







