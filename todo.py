import psycopg2 
import xlsxwriter

class Database():
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="homework",
            user="postgres",
            password="79210000",
            host="127.0.0.1",
            port="5432")
        print("Подключение успешно установлено")
    def create_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE if not exists homework (id SERIAL PRIMARY KEY, user_name text, house_work text)""")
            self.connection.commit() 
    def add_homework(self, user_name, house_work):
        with self.connection.cursor() as cursor:
            for work in house_work:
                cursor.execute("insert into homework (user_name,house_work) values (%s,%s)",(user_name, work))
                self.connection.commit()
                print('Ввод совершен')
   
    def close(self):
        self.connection.close()
class Console():
    def input_user_name(self):
        print('Введите ваше имя:')
        while True:
            user_name=input()
            if user_name:
                return user_name
            print('Имя не может быть пустым')
    def three_variants(self):
        print('Выберете куда записывать строки. 1 - csv, 2 - xlsx, 3 - база данных')
    
        while True:
            try:
                file_format = int(input("Введите 1, 2 ил 3: "))
                if file_format in (1, 2, 3):
                    return file_format 
                print("Пожалуйста, введите 1, 2 или 3")
            except ValueError:
                print('Произошла ошибка. Введите число')
    def input_homework(self):
        print('Введите строки. Для прекращения ввода введите "#"')
        tasks=[]
        while True:
            task=input('Введите задание: ')
            if task.strip()=='#':
                print('Конец ввода')
                break
            if not task:
                continue
            tasks.append(task)
        if not tasks:
            return None 
        return tasks
    def input_lines(self):
        print('Введите строки. Для прекращения ввода введите "#"')
        lines=[]
        while True:
            line=input('Введите строку: ')
            if line.strip()=='#':
                print('Конец ввода')
                break
            lines.append(line)
        if not lines:
            return None 
        return lines

        
        
class FileFormat():
    def write_to_xlsx(self, lines):  # Принимаем lines как параметр
        if not lines:
            print('Нечего записывать в файл')
            return 
        workbook = xlsxwriter.Workbook('new_file.xlsx')
        sheet1 = workbook.add_worksheet()
        for count, line in enumerate(lines):
            sheet1.write(count, 0, line)
        workbook.close()
        print('Ввод совершен')
    
    def write_to_csv(self, lines):  # Принимаем lines как параметр
        if not lines:
            print('Нечего записывать в файл')
            return
        with open('new_file.csv', 'w', newline='', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
        print('Ввод совершен')
def main():
    console = Console()
    db = Database()
    file_manager=FileFormat()
    try:
        file_format = console.three_variants()

        if file_format in (1, 2):
            tasks = console.input_homework()
            lines=console.input_lines()
            if not tasks:
                print('Нечего записывать')
                return

            if file_format == 1:
                file_manager.write_to_csv(lines)
            else:
                file_manager.write_to_xlsx(lines)
        elif file_format == 3:
            user_name = console.input_user_name()
            tasks = console.input_homework()
            if tasks:
                db.add_homework(user_name, tasks)
    finally:
        db.close()
if __name__ == "__main__":
    main()