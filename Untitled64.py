# Generated from: Untitled64.ipynb
# Converted at: 2026-05-09T16:18:24.818Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# <a href="https://colab.research.google.com/github/salimdo2004/Analyse-et-visualisation-de-donn-es/blob/main/Untitled64.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import linregress

# Style des graphiques
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12,6)

import pandas as pd

df = pd.read_csv(
    "GLB.Ts+dSST (1).csv",
    skiprows=1,
    na_values="***"
)
df.head()

print(df.columns)

print(df.dtypes)

# Dimensions du dataset
print("Nombre de lignes et colonnes :", df.shape)

print(df.info())

# ***Nettoyage des données***


# *Vérification des valeurs manquantes*


duplicates = df.duplicated().sum()

print(df.isnull().sum())

# Pourcentage des valeurs manquantes
missing_percent = (df.isnull().sum() / len(df)) * 100
print("\nPourcentage des valeurs manquantes :")
print(missing_percent)

# *Suppression des doublons*


df.drop_duplicates(inplace=True)

# ***TRAITEMENT DES VALEURS MANQUANTES***


cols = ["Year","J-D","DJF","MAM","JJA","SON"]

for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ***Analyse exploratoire***


# ***Statistiques descriptives***


print(df.describe())

# Conversion de Year en entier
df["Year"] = df["Year"].astype(int)

# ***Création de la colonne décennie***


df["Decade"] = (df["Year"] // 10) * 10

# Détection simple des anomalies
outliers = df[(df["J-D"] > df["J-D"].mean() + 3*df["J-D"].std()) |
              (df["J-D"] < df["J-D"].mean() - 3*df["J-D"].std())]
print("\nNombre de valeurs aberrantes :", len(outliers))


# ***5. Visualisations***


# Graphique 1 — Série temporelle
# Évolution des températures mondiales


df_1950 = df[df["Year"] >= 1950]

plt.figure()

plt.plot(df_1950["Year"], df_1950["J-D"])

plt.title("Évolution des températures mondiales depuis 1950")
plt.xlabel("Année")
plt.ylabel("Anomalie de température")

plt.show()

# Graphique 2 — Moyenne mobile
# Tendance du réchauffement


df_1950 = df[df["Year"] >= 1950]
df_1950["Moving_Avg"] = df_1950["J-D"].rolling(5).mean()

plt.figure()

plt.plot(df_1950["Year"], df_1950["J-D"], alpha=0.5)
plt.plot(df_1950["Year"], df_1950["Moving_Avg"], linewidth=3)

plt.title("Tendance climatique avec moyenne mobile")
plt.xlabel("Année")
plt.ylabel("Température")
plt.grid(True)
plt.show()

# Graphique 3 — Boxplot par décennie
# Comparaison des décennies


df_1950 = df[df["Year"] >= 1950].copy()

# créer les décennies
df_1950["Decade"] = (df_1950["Year"] // 10) * 10

plt.figure(figsize=(10,5))

sns.boxplot(x="Decade", y="J-D", data=df_1950)

plt.title("Comparaison des anomalies par décennie")
plt.xlabel("Décennie")
plt.ylabel("Anomalie de température")

plt.xticks(rotation=45)

plt.show()

# Graphique 4 — Heatmap de corrélation
# Corrélation entre saisons


season_cols = ["J-D","DJF","MAM","JJA","SON"]

corr = df[season_cols].corr()

plt.figure()

sns.heatmap(corr, annot=True)

plt.title("Corrélation des températures saisonnières")

plt.show()

# Graphique 5 — Histogramme
# Distribution des anomalies climatiques


plt.figure()

sns.histplot(df["J-D"], bins=20)

plt.title("Distribution des anomalies de température")
plt.xlabel("Anomalie")
plt.ylabel("Fréquence")

plt.show()

# Relation année ↔ température


plt.figure(figsize=(10,5))

sns.scatterplot(x="Year", y="J-D", data=df_1950)

plt.title("Relation entre année et température")
plt.xlabel("Année")
plt.ylabel("Anomalie de température")

plt.show()

#  ***Température moyenne par décennie***


decade_mean = df_1950.groupby("Decade")["J-D"].mean()

plt.figure(figsize=(10,5))

decade_mean.plot(kind="bar")

plt.title("Température moyenne par décennie")
plt.xlabel("Décennie")
plt.ylabel("Anomalie moyenne")

plt.xticks(rotation=45)

plt.show()

# ***Top 10 des années les plus chaudes***


top_hot = df.nlargest(10, "J-D")

plt.figure(figsize=(10,5))

sns.barplot(x="Year", y="J-D", data=top_hot)

plt.title("Top 10 des années les plus chaudes")
plt.xlabel("Année")
plt.ylabel("Anomalie de température")

plt.xticks(rotation=45)

plt.show()

# ***Comparaison des saisons***


season_means = df[["DJF","MAM","JJA","SON"]].mean()

plt.figure(figsize=(8,5))

season_means.plot(kind="bar")

plt.title("Comparaison des températures par saison")
plt.xlabel("Saison")
plt.ylabel("Température moyenne")

plt.xticks(rotation=0)

plt.show()

# Courbe avec régression linéaire


plt.figure(figsize=(10,5))

sns.regplot(x="Year", y="J-D", data=df_1950)

plt.title("Tendance du réchauffement climatique")
plt.xlabel("Année")
plt.ylabel("Anomalie de température")

plt.show()

# Évolution cumulative des anomalies


df_1950["Cumulative"] = df_1950["J-D"].cumsum()

plt.figure(figsize=(10,5))

plt.plot(df_1950["Year"], df_1950["Cumulative"])

plt.title("Accumulation des anomalies de température")
plt.xlabel("Année")
plt.ylabel("Anomalie cumulée")

plt.grid(True)

plt.show()

# Heatmap des températures par année et saison


heatmap_data = df_1950[["Year","DJF","MAM","JJA","SON"]]
heatmap_data = heatmap_data.set_index("Year")

plt.figure(figsize=(12,8))

sns.heatmap(heatmap_data, cmap="coolwarm")

plt.title("Heatmap des anomalies saisonnières")

plt.show()

# Variation annuelle des températures


df_1950["Variation"] = df_1950["J-D"].diff()

plt.figure(figsize=(10,5))

plt.plot(df_1950["Year"], df_1950["Variation"])

plt.axhline(0, linestyle="--")

plt.title("Variation annuelle des températures")
plt.xlabel("Année")
plt.ylabel("Différence annuelle")

plt.show()

# Pie chart des années chaudes vs froides


hot_years = (df_1950["J-D"] > 0).sum()
cold_years = (df_1950["J-D"] <= 0).sum()

plt.figure(figsize=(6,6))

plt.pie(
    [hot_years, cold_years],
    labels=["Années chaudes", "Années froides"],
    autopct="%1.1f%%"
)

plt.title("Répartition des années chaudes et froides")

plt.show()

# vérifier les valeurs manquantes
print(df_1950["J-D"].isnull().sum())

# supprimer les lignes avec NaN
df_1950 = df_1950.dropna(subset=["J-D"])

# Machine Learning — Régression Linéaire


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Variables
X = df_1950[["Year"]]
y = df_1950["J-D"]

# séparation train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# modèle
model = LinearRegression()

# entraînement
model.fit(X_train, y_train)

# prédictions
y_pred = model.predict(X_test)

# évaluation
print("MAE :", mean_absolute_error(y_test, y_pred))
print("R2 Score :", r2_score(y_test, y_pred))

# Visualisation des prédictions ML


plt.figure(figsize=(10,5))

plt.scatter(X_test, y_test, label="Valeurs réelles")

plt.plot(X_test, y_pred, linewidth=3, label="Prédictions")

plt.title("Régression linéaire des températures")
plt.xlabel("Année")
plt.ylabel("Température")

plt.legend()

plt.show()

# Random Forest Regressor


from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

print("R2 Score RF :", r2_score(y_test, rf_pred))

# Visualisation Random Forest


plt.figure(figsize=(10,5))

plt.scatter(X_test, y_test)

plt.scatter(X_test, rf_pred)

plt.title("Random Forest Prediction")
plt.xlabel("Année")
plt.ylabel("Température")

plt.show()

# Deep Learning


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler

# normalisation
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y,
    test_size=0.2,
    random_state=42
)

# modèle
dl_model = Sequential()

dl_model.add(Dense(64, activation='relu'))
dl_model.add(Dense(32, activation='relu'))
dl_model.add(Dense(1))

# compilation
dl_model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# entraînement
history = dl_model.fit(
    X_train,
    y_train,
    epochs=100,
    validation_split=0.2,
    verbose=1
)

# Évaluation Deep Learning


loss, mae = dl_model.evaluate(X_test, y_test)

print("MAE :", mae)

# Visualisation entraînement DL


plt.figure(figsize=(10,5))

plt.plot(history.history['loss'], label='Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.title("Évolution de la perte du modèle")
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.legend()

plt.show()

# Prédire les températures futures


future_years = pd.DataFrame({
    "Year": range(2025, 2051)
})

future_pred = model.predict(future_years)

plt.figure(figsize=(12,5))

plt.plot(df_1950["Year"], df_1950["J-D"], label="Historique")

plt.plot(
    future_years["Year"],
    future_pred,
    linewidth=3,
    label="Prévisions"
)

plt.title("Prévision des températures futures")
plt.xlabel("Année")
plt.ylabel("Température")

plt.legend()

plt.show()