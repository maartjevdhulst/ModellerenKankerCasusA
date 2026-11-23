import pandas as pd
from pathlib import Path

# CSV-bestand inlezen
def read_data(filename):
    # Bepaal het pad naar het CSV-bestand
    file_path = Path(__file__).parent / "data" / filename
    data = pd.read_csv(file_path)

    # Voeg kolomnamen toe aan dataframe
    ts_input = data["Tijd_dagen"].tolist()
    ys_input = data["Tumorvolume_mm3"].tolist()

    return ts_input, ys_input