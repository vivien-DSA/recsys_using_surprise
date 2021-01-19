# recommender_system practical Exercise at EPITA : EDA

by Vivien Bogne

### Data Source :

The movies dataset -> https://www.kaggle.com/rounakbanik/the-movies-dataset

### Content

1. Read the MovieLens dataset from a file (ratings.csv & movies.csv) instead of loading it directly with using the load_builtin method. For more informations, check the Surprise Dataset module documentation.

2. Create 2 model pipelines :

1st pipeline : Load data, Train test split, model training, prediction, evaluation.

2nd pipeline : Load data, cross validation.

3. Benchmark the User based and item based collaborative filtering models using the cosine and pearson correlation similarity metrics. In this step you need to use the data loaded in the 1st step.

### Structure 
The directory is as follows
- data directory : should contain the data that will be used for the practical work
- notebook directory : should contain all the practical work notebooks
- requirements.txt file : should contain the packages used in the practical work
- README.md : for additional informations

![Directory hierarchy](https://github.com/bachtn/recommender_system_practical_work_students/blob/master/doc/directory_hierarchy.png?raw=true)
