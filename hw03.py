import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def print_dir(path, indent=""):
    path = Path(path)
    if not path.is_dir():
        print(Fore.RED + "Помилка: Невірний шлях або це не директорія.")
        return
    print(Fore.CYAN + f"📂 {path.resolve()}")
    for item in sorted(path.iterdir()):
        color = Fore.BLUE if item.is_dir else Fore.GREEN
        print(indent + color + ("📁" if item.is_dir() else "📄") + f" {item.name}")
        if item.is_dir():
            print_dir(item, indent + "   ")

if __name__ == "__main__":
    dir_path = sys.argv[1] if len(sys.argv) > 1 else "."
    print_dir(dir_path)