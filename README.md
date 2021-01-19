# recsys_using_surprise
recommender_system practical Exercise at EPITA : DSA-S20 - Model pipeline assignment
by Vivien Bogne

Data Source :
The movies dataset -> https://www.kaggle.com/rounakbanik/the-movies-dataset

Content
1. Read the MovieLens dataset from a file (ratings.csv & movies.csv) instead of loading it directly with using the load_builtin method. For more informations, check the Surprise Dataset module documentation.

2. Create 2 model pipelines :

1st pipeline : Load data, Train test split, model training, prediction, evaluation.

2nd pipeline : Load data, cross validation.

3. Benchmark the User based and item based collaborative filtering models using the cosine and pearson correlation similarity metrics. In this step you need to use the data loaded in the 1st step.

Structure
• /data/ : contains the data used. 

• /notebooks/ : contains the different notebooks. 

• /html/: contains a html extract of each notebook.

• /package_folder/ : the functions, code, i used during the EDA . 

• /requirements.txt/: The different packages you used for the practical work with their corresponding versions.

• README.md
