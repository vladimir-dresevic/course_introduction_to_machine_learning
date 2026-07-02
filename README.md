# Introduction to Machine Learning

This repository contains learning materials and practical examples for the **Introduction to Machine Learning** program.

The course introduces machine learning through practical problems such as **sentiment analysis of user reviews** and **regression-based numerical prediction**. Step by step, the materials move from simple rule-based approaches to trained machine learning models, model evaluation, feature engineering, complete ML pipelines, and end-to-end machine learning projects.

## Course Goal

The goal of this course is to help learners understand how machine learning works in practice.

Instead of starting with abstract theory only, the course uses real examples, datasets, and practical problems to explain how data is prepared, how models are trained, how predictions are evaluated, and how machine learning projects are organized from beginning to end.

By the end of the course, learners should understand the basic workflow behind supervised machine learning and be able to build, evaluate, save, and test both classification and regression models using Python.

## What You Will Learn

During the course, you will learn how to:

- Understand when manual data analysis becomes difficult or impractical
- Explore and prepare datasets for machine learning
- Apply rule-based sentiment analysis
- Understand the basic idea behind machine learning
- Train machine learning models with `scikit-learn`
- Convert text into numerical features using vectorization
- Use Bag-of-Words and TF-IDF representations
- Compare different machine learning algorithms
- Split data into training and test sets
- Evaluate classification models using standard metrics
- Interpret accuracy, precision, recall, and F1-score
- Use and understand the confusion matrix
- Perform exploratory data analysis before modeling
- Clean and transform raw data
- Create new features from existing data
- Build preprocessing and machine learning pipelines
- Train and evaluate regression models
- Interpret regression metrics and prediction errors
- Select the best model for a given problem
- Save and reuse trained machine learning models
- Organize a complete machine learning project in a GitHub repository

## Course Structure

The course is organized into five main modules.

## Module 1: Understanding the Problem — Sentiment Analysis

The first module introduces the main classification problem used in the first part of the course: analyzing sentiment in user reviews.

Topics covered:

- Working with user review datasets
- Understanding unlabeled and labeled data
- Exploring the basic structure of a dataset
- Cleaning and preparing labeled review data
- Introduction to rule-based sentiment analysis
- Testing a rule-based sentiment analysis system

This module helps learners understand why automation becomes useful when datasets become too large for manual work.

## Module 2: When Computers Learn from Data — Machine Learning

The second module introduces machine learning as an alternative to manually defined rules.

Topics covered:

- Introduction to machine learning
- Installing and using `scikit-learn`
- Training the first machine learning model
- Writing code for manual model testing
- Testing a model on new data
- Understanding text vectorization
- Bag-of-Words
- TF-IDF
- Basic characteristics of machine learning algorithms
- Training multiple models for the same problem
- Comparing predictions made by different algorithms

This module shows how text data can be transformed into a format that machine learning algorithms can process.

## Module 3: How Good Are Our Models? — Model Validation

The third module focuses on evaluating machine learning models and understanding their performance.

Topics covered:

- Splitting data into training and test sets
- Calculating evaluation metrics
- Accuracy and its limitations
- Precision
- Recall
- F1-score
- Summary statistics
- Confusion matrix
- Visualizing the confusion matrix
- Calculating class-level results from the confusion matrix
- Comparing multiple machine learning algorithms
- Interpreting evaluation results

This module explains why simply training a model is not enough. A model must also be tested, measured, and interpreted.

## Module 4: Complete Machine Learning Project — From Start to Finish

The fourth module brings the previous classification concepts together into a complete machine learning project.

Topics covered:

- Starting a real machine learning project
- Understanding the project workflow
- Creating a GitHub repository
- Creating a local repository
- Adding a dataset to the project
- Creating and saving a Colab notebook
- Performing exploratory data analysis
- Checking missing values
- Analyzing sentiment values
- Analyzing product prices
- Cleaning and preparing data
- Parsing product price values
- Standardizing sentiment values
- Removing unnecessary columns
- Creating new features
- Analyzing the relationship between features and sentiment
- Splitting data into input and output values
- Training and evaluating machine learning models
- Selecting the best algorithm
- Training the final model
- Saving the trained model to a file
- Loading and testing a previously trained model
- Writing project documentation

This module demonstrates how the typical classification project workflow looks in a real project environment.

## Module 5: When the Model Predicts Numbers — Regression in Practice

The fifth module introduces regression, a type of supervised machine learning used when the model needs to predict numerical values.

Topics covered:

- Understanding the difference between classification and regression
- Introducing a new regression dataset
- Performing exploratory data analysis before regression
- Understanding the role of different columns in the dataset
- Analyzing the target variable
- Checking missing values
- Analyzing numerical and categorical columns
- Working with date, time, and coordinate data
- Creating a data cleaning script
- Standardizing column names and text values
- Converting numerical columns
- Cleaning time-based columns
- Removing rows with invalid or missing target values
- Building a data cleaning pipeline
- Creating features from date and time values
- Calculating distance-based features
- Creating indicators from weather-related data
- Building a feature engineering pipeline
- Preparing columns for a regression model
- Preprocessing numerical, nominal, and ordinal categorical columns
- Training a first regression model using linear regression
- Building a complete ML pipeline
- Saving the trained regression model
- Making numerical predictions
- Evaluating regression models using regression metrics
- Creating a prediction analysis table
- Analyzing the largest model errors
- Comparing multiple regression algorithms
- Interpreting the results of regression model evaluation

This module expands the course beyond classification and shows how machine learning can be used to predict continuous numerical values.

## Technologies Used

The course materials are based on the Python ecosystem for data analysis and machine learning.

Main tools and libraries:

- Python
- Google Colab
- Jupyter notebooks
- pandas
- NumPy
- scikit-learn
- matplotlib
- seaborn
- joblib
- Git
- GitHub


## Who This Repository Is For

This repository is intended for beginners who want to understand machine learning through practical examples.

It is suitable for learners who:

- already know the basics of Python
- want to understand how machine learning models are trained
- want to work with real datasets
- want to learn how text can be used in machine learning
- want to understand classification and regression
- want to learn how model evaluation works
- want to build complete beginner-friendly ML projects

## Learning Approach

The course follows a practical learning approach.

Each new concept is introduced through a concrete problem, explained step by step, and then applied in code. The focus is not only on writing code, but also on understanding why each step is important in the machine learning workflow.

## Final Outcome

After completing the course, learners should be able to:

- explain the basic idea of machine learning
- prepare text and tabular data for machine learning models
- train simple classification models
- train simple regression models
- evaluate classification and regression models
- compare different machine learning algorithms
- build basic preprocessing and modeling pipelines
- organize a machine learning project
- save and reuse trained models
- document a machine learning project in a clear way

## License

This repository is intended for educational purposes.
