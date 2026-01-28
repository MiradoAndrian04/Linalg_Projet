import numpy as np
import pandas as pd

# notes_sim
data = np.random.randint(0, 20, size=(10, 3))
df = pd.DataFrame(data, columns=["Math","Physique","Informatique"])
df.to_csv("data/notes_sim.csv", index=False)
