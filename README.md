# Analyse-et-visualisation-de-donn-es


# Introduction
# Analyse et visualisation des tendances climatiques mondiales depuis 1950

## Contexte
Le changement climatique représente l’un des plus grands défis environnementaux actuels. 
L’augmentation des températures mondiales impacte les écosystèmes, les ressources naturelles et les activités humaines.

## Problématique
Comment les températures mondiales ont-elles évolué depuis 1950 et quelles tendances peut-on observer à travers les données climatiques ?

## Objectifs
- Nettoyer et analyser les données climatiques
- Visualiser les tendances des températures
- Identifier les périodes les plus chaudes
- Étudier les corrélations saisonnières
- Réaliser des prédictions avec le Machine Learning


# 2. Chargement des bibliothèques
## Importation des bibliothèques Python
Cette partie permet d’importer les outils nécessaires pour :
- l’analyse des données,
- la visualisation,
- le Machine Learning,
- le Deep Learning.
# 3. Chargement du dataset
## Chargement des données

Le dataset utilisé contient les anomalies de température mondiale par année et par saison.
Les données proviennent d’observations climatiques historiques.
# 4. Exploration des données
## Exploration des données

Cette étape permet :
- d’observer la structure du dataset,
- d’identifier les types de variables,
- de détecter les valeurs manquantes,
- d’analyser les dimensions du jeu de données.

# 5. Nettoyage des données
## Nettoyage des données

Les opérations suivantes ont été réalisées :
- suppression des doublons,
- conversion des colonnes numériques,
- traitement des valeurs manquantes,
- création de nouvelles variables comme la décennie.

# 6. Analyse exploratoire
## Analyse exploratoire des données

Cette section présente plusieurs statistiques descriptives :
- moyenne,
- écart-type,
- valeurs minimales et maximales,
- détection des anomalies.
7. Visualisations

Avant chaque graphique ajoute une courte explication.

Exemple :

## Évolution des températures mondiales depuis 1950

Ce graphique montre l’évolution des anomalies de température mondiale au fil du temps.
On observe une augmentation progressive des températures.

# 8. Machine Learning
## Modélisation Machine Learning

Une régression linéaire a été utilisée afin d’étudier la relation entre le temps et les anomalies climatiques.

Les performances du modèle sont évaluées avec :
- le MAE,
- le score R².
9. Deep Learning
  
## Modèle Deep Learning

Un réseau de neurones simple a été entraîné pour prédire les anomalies de température.

Le modèle utilise :
- plusieurs couches Dense,
- l’optimiseur Adam,
- la fonction de perte MSE.
10. Prévisions futures
## Prévision des températures futures

Cette partie présente les prévisions climatiques jusqu’en 2050 à l’aide du modèle de régression linéaire.
# 11. Conclusion finale (IMPORTANT)

Ajoute cette partie à la fin du notebook :

# Conclusion

Cette étude a permis d’analyser les tendances climatiques mondiales depuis 1950 à travers différentes techniques d’analyse et de visualisation de données.

Les résultats montrent une augmentation significative des anomalies de température au fil des décennies, confirmant la tendance générale du réchauffement climatique.

Les visualisations réalisées ont permis :
- d’identifier les années les plus chaudes,
- d’observer les variations saisonnières,
- d’analyser les tendances globales.

Les modèles de Machine Learning et de Deep Learning ont montré qu’il existe une relation importante entre le temps et l’évolution des températures.

## Limites
- Dataset limité à certaines variables climatiques
- Modèles simples
- Absence de données géographiques détaillées

## Perspectives
- Utilisation de modèles plus avancés
- Analyse par continent ou pays
- Intégration d’autres variables climatiques
- Développement d’un dashboard interactif
