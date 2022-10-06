# Пользователь вводит на экран дату в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

# Подсказка: создайте списки с названием дней и названиями месяцев
# Примечание: для экономии времени, можно ограничить номер дня десятью.
# Примечание: склонениями названий можно принебречь

date="02.11.2013"
date_list=date.split(".")
date_new_list=["","",""]
months = ['Январь','Февраль','Март','Апрель','Май','Июнь', \
          'Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
days = ['первое','второе','третье','четвертое','пятое','шестое'\
          ,'седьмое','восьмое','девятое','десятое','одиннадцатое','двенадцатое']
for num,val in enumerate(months,1):
    if int(date_list[1])==num:
        date_new_list[1] =val.lower()
        break
for num,val in enumerate(days,1):
    if int(date_list[0])==num:
        date_new_list[0] =val
        break
date_new_list[2]=date_list[2]
print(f'{date_new_list[0]} {date_new_list[1]} {date_new_list[2]} года')
