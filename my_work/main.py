from database import Database
from console import Console
from file_format import FileFormat

def main():
    console = Console()
    db = Database()
    file_manager = FileFormat()
    
    try:
        while True:
            print('Пункт управления:')
            print('1. Добавить строки в csv файл')
            print('2. Добавить строки в xlsx таблицу')
            print('3. Добавить задания в базу данных')
            print('4. Поиск заданий')
            print('5. Выход')
            
            try:
                variant = int(input('Выберите вариант 1-5: '))
            except ValueError:
                print('Ошибка: введите число от 1 до 5')
                continue
                
            if variant not in (1, 2, 3, 4, 5):
                print('Ошибка: выберите вариант от 1 до 5')
                continue
                
            if variant in (1, 2):
                lines = console.input_lines() #вызов функции в консоли получаем lines
                if not lines:
                    print('Нечего записывать')
                    continue
                    
                if variant == 1:
                    file_manager.write_to_csv(lines)
                else:
                    file_manager.write_to_xlsx(lines)
                print('Данные успешно записаны в файл')
                    
            elif variant == 3:  
                # Создаем таблицу если ее нет
                db.create_table()
                
                # Спрашиваем нужно ли очистить базу
                print('Хотите удалить данные из базы данных? (1 - Да, 2 - Нет)')
                while True:
                    try:
                        clear_choice = int(input())
                        if clear_choice == 1:
                            db.delete_all()
                            print('Все данные удалены')
                            break
                        elif clear_choice == 2:
                            break
                        else:
                            print('Введите 1 или 2')
                    except ValueError:
                        print('Ошибка: введите число')
                        
                # Добавляем новые данные
                user_name = console.input_user_name()
                house_work = console.input_homework()
                if house_work:
                    db.add_homework(user_name, house_work)
                    print('Данные успешно добавлены в базу')
                    
            elif variant == 4:
                print('Поиск по точному слову')
                query = console.input_search_query()
                results = db.search_homework(query)
                if not results:
                    print('Совпадений не найдено')
                else:
                    print('Результаты поиска:')
                    for row in results:
                        print("ID: " + str(row[0]) + ", Пользователь: " + str(row[1]))
                        print("Задание: " + str(row[2]))
                        
            elif variant == 5:
                print('Выход из программы')
                break
                
    finally:
        db.close()

main()