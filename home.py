

import xlsxwriter
def two_variants():
    print('Выберете куда записывать строки. 1 - csv, 2 - xlsx')
    try:
        s=int(input())
    except ValueError:
        return print('Произошла ошибка, попробуйте снова')
    
    print('Введите строки. Для прекращения ввода введите "#"')
    line=[]
    while True:
        lines=input('Введите строку: ')
        if lines.strip()=='#':
            print('Конец ввода')
            break
        line.append(lines)
    if s==2:
        workbook=xlsxwriter.Workbook('new_file.xlsx')
        sheet1=workbook.add_worksheet()
        count=0
        for i in line:
            sheet1.write(count,0 , i)
            count+=1
        workbook.close()
        print('Ввод совершен')  
    if not line:
        return print('Вы не ввели ни одной строки')
    if s==1:
        with open('new_file.csv', 'w', newline='', encoding='utf-8') as file:
            for i in line:
                file.write(i+'\n')
        print('Ввод совершен')



    

    


trywork = two_variants()