import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    # Формирование строки с символами, в зависимости от выбранных опций
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Генерация пароля из случайных символов указанной длины
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, filename):
    # Сохранение пароля в указанный файл
    with open(filename, 'a') as file:
        file.write(password + '\n')

def main():
    while True:
        print("1. Сгенерировать пароль")
        print("2. Посмотреть сохраненные пароли")
        print("3. Выход")

        # Получение выбора пользователя
        choice = input("Выберите действие: ")

        if choice == "1":
            length = int(input("Введите длину пароля: "))
            password = generate_password(length)
            print("Сгенерированный пароль: ", password)
            save_password(password, "passwords.txt")
        elif choice == "2":
            with open("passwords.txt", 'r') as file:
                passwords = file.readlines()
                if not passwords:
                    print("Список паролей пуст.")
                else:
                    print("Сохраненные пароли:")
                    for idx, password in enumerate(passwords, start=1):
                        print(f"{idx}. {password.strip()}")
        elif choice == "3":
            # Завершение программы
            break
        else:
            # В случае некорректного выбора пользователя
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    # Запуск основной функции программы
    main()