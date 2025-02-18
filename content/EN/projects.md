# How to collaborate during the Data Analyst project

Here are some tips for organizing your data science project:

-   **Create a shared folder**: Set up a Google Drive folder where you and your team can store project documents, datasets, and code. This will make it easy for everyone to access and collaborate on the project.

-   **Give access** : Make sure to grant access to the shared folder to all team members. This will allow everyone to view, edit, and contribute to the project materials.

-   **Use Google Colab** : Consider using Google Colab as a collaborative coding environment. Colab allows multiple users to work together on the same notebook simultaneously, making it convenient for code sharing and collaboration.

-   **Build a project timeline** : Create a project timeline or plan based on the steps outlined in the previous message. Break down the project into smaller tasks and assign them to team members. This will help in organizing the work and ensuring that all project milestones are met.

Remember, the goal is to keep the project organization simple and efficient, allowing the focus to be on data analysis rather than project management. If you have any further questions or need assistance with project organization, feel free to reach out. Good luck with your project!

# Final delivery

Regarding the structure of the final rendering, I would like the folder structure to be as follows (this is an example; you can have more notebooks):

```         
project/
│
├── notebooks/
│ ├── 01_exploration.ipynb
│ ├── 02_DataViz.ipynb
│ ├── 03_preProcessing.ipynb
│ └── 04_modelisation.ipynb
│
├── datasets/
│ ├── data.csv
│ └── data_clean.csv
│
├── report/
│ ├── report_word.docx
│ └── report_pdf.pdf
│
└── requirements.txt
```

In this structure, we have a notebooks folder containing the notebooks numbered in order of execution. Data is stored in the datasets folder, and reports in Word and PDF format are in the report folder. Finally, the requirements.txt file contains the list of dependencies needed to run the notebooks, see the example below:

```         
matplotlib
numpy
pandas
scipy
seaborn
scikit-learn
```

This includes libraries used for data analysis and machine learning. You can add other project-specific libraries as you need them. Finally, make sure that the notebooks run without errors and define the relative path of the datasets when loading with pandas, see example below:

``` python
df = pd.read_csv('../datasets/data.csv')
```