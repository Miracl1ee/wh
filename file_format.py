import xlsxwriter
class FileFormat():
    def write_to_xlsx(self, lines):  
        if not lines:
            print('Нечего записывать в файл')
            return 
        workbook = xlsxwriter.Workbook('new_file.xlsx')
        sheet1 = workbook.add_worksheet()
        for count, line in enumerate(lines):
            sheet1.write(count, 0, line)
        workbook.close()
        print('Ввод совершен')
    def write_to_csv(self, lines):  
        if not lines:
            print('Нечего записывать в файл')
            return
        with open('new_file.csv', 'w', newline='', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
        print('Ввод совершен')