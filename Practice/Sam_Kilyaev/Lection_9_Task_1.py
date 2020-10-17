import time
import threading
from multiprocessing import Process


def find_primes(end, start=3):
    primes_numbers = []
    start_time = time.time()
    for i in range(start, end + 1):
        if i > 1:
            for n in range(2, i):
                if (i % n) == 0:
                    break
            else:
                primes_numbers.append(i)
    print(f"Диапазон от {start} до {end}, время обработки {time.time() - start_time} сек.")
    return primes_numbers


find_primes(30000, 20001)
th = threading.Thread(name='th', target=find_primes, args=(10000, 3))
th2 = threading.Thread(name='th2', target=find_primes, args=(20000, 10001))
th3 = threading.Thread(name='th3', target=find_primes, args=(30000, 20001))

p1 = Process(name='p1', target=find_primes, args=(10000, 3))
p2 = Process(name='p2', target=find_primes, args=(20000, 10001))
p3 = Process(name='p3', target=find_primes, args=(30000, 20001))


if __name__ == '__main__':
    find_primes(10000, 3)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    # Просто запуск
    # Диапазон от 3 до 10000, время обработки 0.4532644748687744 сек.
    # Диапазон от 10001 до 20000, время обработки 1.160167932510376 сек.
    # Диапазон от 20001 до 30000, время обработки 1.8433763980865479 сек.



    ths = [th, th2, th3]
    for i in ths:
        i.start()
        i.join()
    # Без join
    # Отдельные потоки через очередь
    # Диапазон от 3 до 10000, время обработки 1.4850199222564697 сек.
    # Диапазон от 10001 до 20000, время обработки 3.345010995864868 сек.
    # Диапазон от 20001 до 30000, время обработки 4.001810789108276 сек.

    th.start()
    th.join()
    # Первый запуск в отдельном потоке: Диапазон от 3 до 10000, время обработки 0.43637704849243164 сек.
    th2.start()
    th2.join()
    # Первый запуск в отдельном потоке: Диапазон от 10001 до 20000, время обработки 1.1085929870605469 сек.
    # Первый поток + второй поток: Диапазон от 3 до 10000, время обработки 1.093163013458252 сек.
    # Диапазон от 10001 до 20000, время обработки 1.751540184020996 сек.
    th3.start()
    th3.join()
    # Первый запуск в отдельном потоке: Диапазон от 20001 до 30000, время обработки 1.7662663459777832 сек.
    # Третий поток + второй поток: Диапазон от 10001 до 20000, время обработки 2.8737423419952393 сек.
    # Диапазон от 20001 до 30000, время обработки 3.5143141746520996 сек.
    # Третий поток + второй поток + первый поток: Диапазон от 3 до 10000, время обработки 1.4379630088806152 сек.
    # Диапазон от 10001 до 20000, время обработки 3.315340757369995 сек.
    # Диапазон от 20001 до 30000, время обработки 3.924903392791748 сек.

    # С join
    # Отдельные потоки через очередь
    # Диапазон от 3 до 10000, время обработки 0.4536869525909424 сек.
    # Диапазон от 10001 до 20000, время обработки 1.1708734035491943 сек.
    # Диапазон от 20001 до 30000, время обработки 1.783141851425171 сек.

    # Первый запуск в отдельном потоке: Диапазон от 3 до 10000, время обработки 0.43637704849243164 сек.
    # Первый запуск в отдельном потоке: Диапазон от 10001 до 20000, время обработки 1.155395269393921 сек.
    # Первый поток + второй поток: Диапазон от 3 до 10000, время обработки 0.41905736923217773 сек.
    # Диапазон от 10001 до 20000, время обработки 1.1731455326080322 сек.
    # Первый запуск в отдельном потоке: Диапазон от 20001 до 30000, время обработки 1.8445117473602295 сек.
    # Третий поток + второй поток: Диапазон от 10001 до 20000, время обработки 1.2029078006744385 сек.
    # Диапазон от 20001 до 30000, время обработки 1.8432683944702148 сек.
    # Третий поток + второй поток + первый поток: Диапазон от 3 до 10000, время обработки 0.42202234268188477 сек.
    # Диапазон от 10001 до 20000, время обработки 1.1708025932312012 сек.
    # Диапазон от 20001 до 30000, время обработки 1.7974178791046143 сек.
    ps = [p1, p2, p3]
    for i in ps:
        i.start()
        i.join() #Ошибка нельзя использовать так
    for i in ps:
        i.join()
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
    p1.join()
    p2.join()
    p3.join()

# Без join
# Отдельные процессы через очередь
# Диапазон от 3 до 10000, время обработки 0.4532663822174072 сек.
# Диапазон от 10001 до 20000, время обработки 1.2036552429199219 сек.
# Диапазон от 20001 до 30000, время обработки 1.8579685688018799 сек.

# Отдельные процессы подряд
# Диапазон от 3 до 10000, время обработки 0.4916818141937256 сек.
# Диапазон от 10001 до 20000, время обработки 1.2512257099151611 сек.
# Диапазон от 20001 до 30000, время обработки 1.9224333763122559 сек.

# С join после запуска каждого процесса через очередь
# Диапазон от 3 до 10000, время обработки 0.40514683723449707 сек.
# Диапазон от 10001 до 20000, время обработки 1.1105501651763916 сек.
# Диапазон от 20001 до 30000, время обработки 1.7672350406646729 сек.

# С join после запуска всех процессов через очередь
# Диапазон от 3 до 10000, время обработки 0.437638521194458 сек.
# Диапазон от 10001 до 20000, время обработки 1.235382318496704 сек.
# Диапазон от 20001 до 30000, время обработки 1.9074857234954834 сек.

# С join после запуска первого процесса
# Диапазон от 3 до 10000, время обработки 0.43762993812561035 сек.
# Диапазон от 10001 до 20000, время обработки 1.1873795986175537 сек.
# Диапазон от 20001 до 30000, время обработки 1.843843936920166 сек.

# С join после запуска первого процесса и второго
# Диапазон от 3 до 10000, время обработки 0.4061460494995117 сек.
# Диапазон от 10001 до 20000, время обработки 1.1357831954956055 сек.
# Диапазон от 20001 до 30000, время обработки 1.798374891281128 сек.

# С join после запуска каждого процесса
# Диапазон от 3 до 10000, время обработки 0.4063911437988281 сек.
# Диапазон от 10001 до 20000, время обработки 1.1221287250518799 сек.
# Диапазон от 20001 до 30000, время обработки 1.764697790145874 сек.

# С join после запуска всех процессов
# Диапазон от 3 до 10000, время обработки 0.4845249652862549 сек.
# Диапазон от 10001 до 20000, время обработки 1.2811341285705566 сек.
# Диапазон от 20001 до 30000, время обработки 1.9543585777282715 сек.

'Если не использовать join, то время выполнения функции увеличивается и при разных потоках и при разных процессах' \
'После всех тестов для этой функции наилучшим вариантом по времени является использование разных процессов через очередь' \
'с join'