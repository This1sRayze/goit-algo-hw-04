from pathlib import Path

def total_salary(path):
    path = Path(path)  
    if not path.exists():
        raise FileNotFoundError(f"Файл не знайдено: {path}")
    with path.open('r', encoding='utf-8') as file:
        salaries = []
        for line in file:
            try:
                _, salary = line.strip().split(',')  
                salaries.append(int(salary))  
            except ValueError:
                print(f"Помилка у рядку: {line.strip()}")  
    total = sum(salaries)
    average = total / len(salaries) if salaries else 0  
    return total, average

total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


def get_cats_info(path):
    path = Path(path)  
    if not path.exists():
        raise FileNotFoundError(f"Файл не знайдено: {path}")
    with path.open('r', encoding='utf-8') as file:
        cats = []
        for line in file:
            try:
                id, name, age = line.strip().split(',')  
                cats.append({"id": id, "name": name, "age": int(age)})
            except ValueError:
                print(f"Помилка у рядку: {line.strip()}")  
    return cats        

cats_info = get_cats_info("identifier.txt")
print(cats_info)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    return "Contact not found."

def phone_username(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")

def all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))    
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(all())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()