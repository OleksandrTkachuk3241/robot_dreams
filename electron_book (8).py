class Book:
    
    
    def __init__(self):
        self.book = set()
    
    
    def stats(self):
        print(len(self.book))
    
    
    def show(self):
        name = input("Введіть ім'я:\n")
        for word in self.book:
            if word[0] == name:
                print(word)
    
    
    def list(self):
        print(sorted([i[0] for i in self.book]))
    
    
    def add(self):
        name = input("Введіть ім'я:\n")
        number = int(input("Введіть номер:\n"))
        for word in self.book:
            if word[0] == name:
                print("Запис з таким ім'ям вже існує")
                break
        else:
            self.book.add((name, number))
    
    
    def delete(self):
        name = input("Введіть ім'я:\n")
        for word in self.book:
            if word[0] == name:
                self.book.remove(word)
                break


book = Book()


commands = {
    "add": book.add,
    "delete": book.delete,
    "list": book.list,
    "show": book.show,
    "stats": book.stats,
}

while True:
    command = input('Введіть команду:\n').lower()
    commands[command]()

