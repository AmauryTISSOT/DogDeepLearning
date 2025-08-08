# DogDeepLearning

Pour installer le projet :

```bash
cd project
pip install -r requirements.txt
```

Pour lancer le serveur :

```bash
python manage.py runserver
```

# Apprentissage d'un modèle from scratch

Dans un premier temps, nous avons procédé à la création d'un modèle à partir de zéro.
Le notebook contenant la procédure de création de ce modèle figure dans le fichier `/notebooks/modele_from_scratch.ipynb`.
Malgré de nombreuses heures d'entraînement, le modèle a présenté une précision relativement faible (moins de 1%).

# Apprentissage d'un modèle par transfert

Dans un second temps, nous avons procédé à l'apprentissage d'un nouveau modèle via un "transfer learning".
Pour ce faire, nous avons choisi d'utiliser le modèle Xception.
La procédure de création de ce modèle figure dans le notebook `/notebooks/dogsxception.ipynb`.
Nous sommes parvenus à obtenir une précision de 86,50 %.
