# Comment collaborer pendant le projet Data Analyst

Voici quelques conseils pour organiser votre projet de science des données :

- **Créez un dossier partagé** : configurez un dossier Google Drive dans lequel vous et votre équipe pouvez stocker les documents, les ensembles de données et le code du projet. Cela permettra à tout le monde d’accéder facilement au projet et de collaborer sur celui-ci.

- **Donner l'accès** : Assurez-vous d'accorder l'accès au dossier partagé à tous les membres de l'équipe. Cela permettra à chacun de visualiser, modifier et contribuer aux documents du projet.

- **Utiliser Google Colab** : envisagez d'utiliser Google Colab comme environnement de codage collaboratif. Colab permet à plusieurs utilisateurs de travailler ensemble simultanément sur le même bloc-notes, ce qui facilite le partage de code et la collaboration.

- **Créer un calendrier de projet** : créez un calendrier ou un plan de projet basé sur les étapes décrites dans le message précédent. Décomposez le projet en tâches plus petites et attribuez-les aux membres de l'équipe. Cela aidera à organiser le travail et à garantir que toutes les étapes du projet sont respectées.

N'oubliez pas que l'objectif est de garder l'organisation du projet simple et efficace, en permettant de se concentrer sur l'analyse des données plutôt que sur la gestion de projet.
Si vous avez d'autres questions ou avez besoin d'aide pour l'organisation d'un projet, n'hésitez pas à nous contacter. Bonne chance avec votre projet!




# Livrable final

Concernant la structure du rendu final, je souhaiterai que la structure du dossier soit la suivante (ceci est un exemple vous pouvez avoir plus de notebooks) :

```
projet/
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_DataViz.ipynb
│   ├── 03_preProcessing.ipynb
│   └── 04_modelisation.ipynb
│
├── datasets/
│   ├── data.csv
│   └── data_clean.csv
│
├── rapport/
│   ├── rapport_word.docx
│   └── rapport_pdf.pdf
│
└── requirements.txt
```

Dans cette structure, nous avons un dossier notebooks contenant les notebooks numérotés par ordre d'exécution. Les données sont stockées dans le dossier datasets, et les rapports au format Word et PDF sont dans le dossier rapport. Enfin, le fichier requirements.txt contient la liste des dépendances nécessaires pour exécuter les notebooks, voir l'exemple ci-dessous :
```
matplotlib
numpy
pandas
scipy
seaborn
scikit-learn
```

Cela inclut les bibliothèques couramment utilisées pour l'analyse de données et l'apprentissage automatique. Vous pouvez ajouter d'autres bibliothèques spécifiques au projet au fur et à mesure de vos besoins.Enfin veillez à ce que les notebooks s'exécute sans erreurs et définir le chemin relatif des dataset lors du chargement avec pandas, voir exemple ci-dessous :
```python
df = pd.read_csv('../datasets/data.csv')
```