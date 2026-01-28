import pandas as pd
import numpy as np
import os

def choose_csv_file(data_folder="data"):
    
    csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]
    
    if not csv_files:
        raise FileNotFoundError(f"Aucun fichier CSV trouvé dans le dossier '{data_folder}'.")

    print("Fichiers CSV disponibles :")
    for i, file in enumerate(csv_files):
        print(f"{i+1}. {file}")

    
    while True:
        try:
            choice = int(input(f"Entrez le numéro du fichier à charger (1-{len(csv_files)}): "))
            if 1 <= choice <= len(csv_files):
                selected_file = os.path.join(data_folder, csv_files[choice-1])
                print(f"Vous avez choisi : {csv_files[choice-1]}")
                return selected_file
            else:
                print("Numéro invalide. Réessayez.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def load_csv(path):
    
    df = pd.read_csv(path)
    return df.values, df.columns.tolist()



if __name__ == "__main__":
    csv_path = choose_csv_file()
    data, columns = load_csv(csv_path)
    print("Colonnes :", columns)
    print("Données (5 premières lignes) :\n", data[:5])
