# Задача 38: Создать телефонный справочник возможностью добавления записей и чтения. 
# Пользователь также может ввести фамилию, тогда программа должны вывести на экран все записи 
# с этой фамилий.
# Также пользователь может добавлять новых людей в справочник в режиме экспорт.

# Показывает информацию в файле
def readfile(phonebook):
    print("\nФ.И. | Телефон")
    with open(phonebook.txt, "r", encoding="utf-8") as file:
        print(file.read())
    print("")

# Записывает информацию в файл
def writes_information(phonebook):
    with open(phonebook.txt, "r", encoding="utf-8") as file:
        book_file = file.read()
    num = len(book_file.split("\n"))
    with open(phonebook, "a", encoding="utf-8") as file: 
        name = input("Введите Фамилию и имя: ")
        number_phone = input("Введите номер телефона: ")
        file.write(f"{num} | {name} | {number_phone}\n")
        print(f"Добавлена запись : {name} | {number_phone}\n")

# Изменяет информацию из файла
def changes_information(phonebook):
    print("\nФ.И. | Телефон")
    with open(phonebook.txt, "r", encoding='utf-8') as file:
        phone_book = file.read()
    print(phone_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    phone_book_lines = phone_book.split("\n")
    edit_phone_book_lines = phone_book_lines[index_delete_data]
    elements = edit_phone_book_lines.split(" | ")
    fio = input("Введите Фамилию и имя: ")
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{fio} | {phone}"
    phone_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_phone_book_lines}, изменена на - {edited_line}\n")
    with open(phonebook.txt, "w", encoding='utf-8') as file:
        file.write("\n".join(phone_book_lines))
        
def main():
    my_choice = -1
    file_tel = "phonebook.txt"

    # Создает файл если его нет в папке
    with open(file_tel, "a", encoding="utf-8") as file:
         file.write("")

    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 - Вывести инфо на экран")
        print("2 - Произвести экпорт данных")
        print("3 - Произвести изменение данных")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            readfile(file_tel)
        elif action == 2:
            writes_information(file_tel)
        elif action == 3:
            changes_information(file_tel)
        else:
            my_choice = 0

    print("До свидания")

if __name__ == "__main__":
    main()
