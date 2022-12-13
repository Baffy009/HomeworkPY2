#По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты. Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. До последнего человека в круге. Составьте алгоритм, который проводит эту игру. Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep. Определите номер этого человека и количество монет, которые оказались у него в конце игры. 
# P.S. рекомендации по выполнению 4-го задания. 1. представьте список людей в виде списка индексов: [0,1,2,3,4...]; 2. работайте одновременно со списком монет; 3. не надо писать сложных систем для "Процесс продолжается с места остановки". Достаточно использовать срезы: переместите оставшуюся часть списка вперед 4. после каждого выбывшего пусть работает input: хотите продолжать или выйти из цикла игры?

def money_dealer(ppl,mon, count):                
    for i in range(0, len(ppl)):
        if i < count:
            mon[i] += 1
        else: mon[i] += 2
    print('Игроки получили свои монеты.')    
    return mon

def anounce(ppl,mon):
    print(f'Игроки с номерами: {ppl} \nДеньги на руках:   {mon}')

def man_count(ppl):
    ppl_counter = -1
    while(ppl_counter<1 or ppl_counter>len(ppl)):
        try:
            ppl_counter = int(input('Считаем до: '))
            if(ppl_counter<1 or ppl_counter>len(ppl)):
                    print('Введите другое число')
        except:
            print('Это не число')
    return ppl_counter


people_list = []
money_list = []

for i in range(0, (int(input('Количество участников в игре: ')))):
    people_list.append(i)
    money_list.append(0)

for i in range(0,len(people_list)-1):
    anounce(people_list,money_list)
    
    counter = man_count(people_list)

    money_list = money_dealer(people_list,money_list, counter)
    anounce(people_list,money_list)

    last_player_def = counter
    if(counter == len(people_list)):
        last_player_def = 0

    print(f'Игроку: {people_list[counter-1]} сегодня не везет.\n{money_list[counter-1]} единиц валюты достаются {people_list[last_player_def]} игроку')
    
    if(counter == len(people_list)):
        stack = money_list.pop(counter-1) + money_list.pop(last_player_def)
    else: stack = money_list.pop(last_player_def) + money_list.pop(counter-1)

    money_list.insert(last_player_def, stack)
    people_list.pop(counter-1)

    anounce(people_list,money_list)
    if(len(people_list) > 1):
        quit = input('Хотите продолжать или выйти из цикла игры?\n N - чтобы выйти:  ')
        if(quit=='N' or quit=='n'):
            print('Вы вышли так и не узнав кто победил')
            break
    else: print(f'Победил игрок {people_list} унеся с собой монет в количестве {money_list} шт')
