import pandas as pd

# Ouvrez les fichiers Excel
df_etudiant = pd.read_excel("C:/Users/princesse/Downloads/etudiant.xlsx")
df_filiere = pd.read_excel("C:/Users/princesse/Downloads/filiere.xlsx")

# Vérifiez que les ID_ET sont identiques
df_fusion = df_etudiant.merge(df_filiere, how="inner", on=["ID_ET"])

# Enregistrez le fichier fusionné
df_fusion.to_excel("C:/Users/brody/Downloads/etudiant_filiere.xlsx")
