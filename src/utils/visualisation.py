import matplotlib.pyplot as plt
import os
import numpy as np

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def scatter_original_vs_projected(Xc, Z, columns, save_path=None, colors=("green","cyan")):
    plt.figure(figsize=(8,6))
    plt.scatter(Xc[:,0], Xc[:,1], color=colors[0], label='Original')
    plt.scatter(Z[:,0], [0]*len(Z), color=colors[1], label='Projeté')
    for i, val in enumerate(Z[:,0]):
        plt.text(Z[i,0]+0.05, 0, f"{int(val)}", fontsize=8)
    plt.xlabel(columns[0])
    plt.ylabel(columns[1] if len(columns)>1 else "Composante 2")
    plt.title("Projection PCA")
    plt.legend()
    plt.grid(True)
    if save_path:
        ensure_dir(save_path)
        plt.savefig(os.path.join(save_path, "scatter_projection.png"))
    plt.show()

#Barre de variance
def bar_variance(eigenvalues, save_path=None, color="green"):
    plt.figure(figsize=(6,4))
    plt.bar(range(len(eigenvalues)), eigenvalues, color=color)
    plt.xticks(range(len(eigenvalues)), [f"PC{i+1}" for i in range(len(eigenvalues))])
    plt.ylabel("Variance")
    plt.title("Variance expliquée par composante")
    plt.grid(True)
    if save_path:
        ensure_dir(save_path)
        plt.savefig(os.path.join(save_path, "bar_variance.png"))
    plt.show()

# Ligne cumulée
def line_cumulative_variance(eigenvalues, save_path=None, color="red"):
    cumulative_variance = eigenvalues.cumsum() / eigenvalues.sum()
    plt.figure(figsize=(6,4))
    plt.plot(range(1, len(eigenvalues)+1), cumulative_variance, marker='o', linestyle='--', color=color)
    plt.xlabel("Nombre de composantes")
    plt.ylabel("Variance cumulée")
    plt.title("Variance cumulée")
    plt.ylim(0,1.05)
    plt.grid(True)
    if save_path:
        ensure_dir(save_path)
        plt.savefig(os.path.join(save_path, "line_cumulative.png"))
    plt.show()

# Scatter coloré
def color_by_value(Xc, column_index=0, save_path=None, colors=("green","blue")):
    
    color_list = [colors[0] if x[column_index] > 12 else colors[1] for x in Xc]
    plt.figure(figsize=(8,6))
    plt.scatter(Xc[:,0], Xc[:,1], c=color_list, alpha=0.7, s=80)
    for i, val in enumerate(Xc[:,column_index]):
        plt.text(Xc[i,0]+0.1, Xc[i,1]+0.1, f"{int(val)}", fontsize=8)
    plt.xlabel("Colonne 1")
    plt.ylabel("Colonne 2")
    plt.title("Points colorés selon la valeur")
    plt.grid(True)
    if save_path:
        ensure_dir(save_path)
        plt.savefig(os.path.join(save_path, "color_by_value.png"))
    plt.show()

# Générer tous les graphes
def generate_all_plots(Xc, Z, eigenvalues, columns, save_path="results/figures/"):
    scatter_original_vs_projected(Xc, Z, columns, save_path, colors=("green","red"))
    bar_variance(eigenvalues, save_path, color="green")
    line_cumulative_variance(eigenvalues, save_path, color="red")
    color_by_value(Xc, column_index=0, save_path=save_path, colors=("green","red"))
