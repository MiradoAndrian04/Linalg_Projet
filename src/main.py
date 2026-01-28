from data_loader import choose_csv_file, load_csv
from algorithme import pca
from linalg_utils import center_data
from utils.visualisation import generate_all_plots

def main():
    csv_path = choose_csv_file()
    X, columns = load_csv(csv_path)
    Xc, mean = center_data(X)
    Z, eigenvalues, components = pca(Xc, k=min(Xc.shape[1], 2))

    print("Valeurs propres :", eigenvalues)
    print("Composantes principales :", components)
    
    
    generate_all_plots(Xc, Z, eigenvalues, columns, save_path="results/figures/")

if __name__ == "__main__":
    main()
