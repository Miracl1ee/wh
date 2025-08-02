class Console():
    
    def input_user_name(self):
        print('Введите ваше имя:')
        while True:
            user_name=input()
            if user_name:
                return user_name
            print('Имя не может быть пустым') 
                    
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

                
    def input_search_query(self):
        return input("Введите задание, по которому будет вестись поиск: ").strip()

        