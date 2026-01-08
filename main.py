from menu import run_menu
from data_loader import load_apartments

def main():
    filename = 'apartments.csv'
    try:
        apartments = load_apartments(filename)
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return
    run_menu(apartments, filename)

if __name__ == "__main__":
    main()