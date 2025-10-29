import random
import csv
import os

def create_dane_csv_in_directory(dirpath):
    model = random.choice(['A', 'B', 'C'])
    wynik = random.randint(0, 1000)
    czas = random.randint(0, 1000)
    
    filepath = os.path.join(dirpath, 'Dane.csv')
    
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Model', ' Wynik', ' Czas', ' '])
        writer.writerow([model, f' {wynik}', f' {czas}s', ''])

def create_files_recursively(root_path='.'):
    count = 0

    for dirpath, dirnames, filenames in os.walk(root_path):
        if dirpath == root_path:
            continue

        if "__pycache__" in dirpath or ".git" in dirpath:
            continue

        if not dirnames:
            create_dane_csv_in_directory(dirpath)
            count += 1
            print(f"[+] Utworzono Dane.csv w: {dirpath}")

    print(f"\n{'='*60}")
    print(f"Utworzono łącznie {count} plików Dane.csv")


if __name__ == "__main__":
    create_files_recursively()
