import csv
import os

def read_and_sum_time_for_model_a(root_path='.'):
    total_sum = 0
    files_processed = 0
    model_a_records = 0
    
    print("Odczytywanie plików Dane.csv...\n")
    
    for dirpath, dirnames, filenames in os.walk(root_path):
        if 'Dane.csv' in filenames:
            filepath = os.path.join(dirpath, 'Dane.csv')
            files_processed += 1
            
            try:
                with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    
                    for row in reader:
                        model = row.get('Model', '').strip()
                        
                        if model == 'A':
                            czas_str = row.get(' Czas', '').strip()
                            czas_value = czas_str.rstrip('s').strip()
                            
                            try:
                                czas = int(czas_value)
                                total_sum += czas
                                model_a_records += 1
                                
                                wynik = row.get(' Wynik', '').strip()
                            except ValueError:
                                print(f"Błąd: {filepath}")
            except Exception as e:
                print(f"Błąd: {filepath}: {e}")
            
            print()
    
    print(f"{'='*60}")
    print(f"Przetworzone pliki: {files_processed}")
    print(f"Rekordy z Model=A: {model_a_records}")
    print(f"SUMA CZASÓW DLA MODELU A: {total_sum}s")
    print(f"{'='*60}")
    
    return total_sum

if __name__ == "__main__":
    read_and_sum_time_for_model_a()
