# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def alg_compression (text):
    char = 0
    count = 1
    resultat = ''
    text+= ' '
    for i in range (1,len(text)):
        if char == text[i]:
            count += 1
        else: 
            resultat += str(count) + text [i-1] 
            char = text [i]
            count = 1
    return resultat

def recovery_RLE (text):
    numbers = ''
    resultat = ''
    for i in range (len (text)):
        if '0' <= text [i] <= '9':
            numbers += text [i]
        else:
            resultat += text [i] * int (numbers)
            numbers = '' 
    return resultat

import codecs
print ('1 - Сжатие данных')
print ('2 - Восстановление данных')
menu = int (input ('Выберите вариант выполнения - '))
if menu == 1:
    with codecs.open ('4_data_compression.txt','r', encoding = 'utf-8') as file:
        text = str (file.readline())
    text = alg_compression (text)
    with codecs.open ('4_data_compression_result.txt','w', encoding = 'utf-8') as file:
        file.write (text)
elif menu == 2:
    with codecs.open ('4_data_recovery.txt','r', encoding = 'utf-8') as file:
        text = str (file.readline())
    text = recovery_RLE (text)
    with codecs.open ('4_data_recovery_result.txt','w', encoding = 'utf-8') as file:
        file.write (text)