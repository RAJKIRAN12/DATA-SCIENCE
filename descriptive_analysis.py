import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_descriptive_analysis(netflix_movies, disney_movies):
    # Clean Rotten Tomatoes column
    netflix_movies['Rotten Tomatoes'] = pd.to_numeric(netflix_movies['Rotten Tomatoes'], errors='coerce')
    disney_movies['Rotten Tomatoes'] = pd.to_numeric(disney_movies['Rotten Tomatoes'], errors='coerce')

    # Drop NaN values in Rotten Tomatoes scores for analysis
    netflix_scores = netflix_movies['Rotten Tomatoes'].dropna()
    disney_scores = disney_movies['Rotten Tomatoes'].dropna()

    # Print descriptive statistics
    print("Netflix Rotten Tomatoes Scores:")
    print(netflix_scores.describe())
    print("\nDisney+ Rotten Tomatoes Scores:")
    print(disney_scores.describe())

    # Plot Rotten Tomatoes Scores: KDE plot
    plt.figure(figsize=(10, 6))
    sns.kdeplot(netflix_scores, label='Netflix', fill=True, color='blue', alpha=0.6)
    sns.kdeplot(disney_scores, label='Disney+', fill=True, color='red', alpha=0.6)
    plt.title("Rotten Tomatoes Score Distribution")
    plt.xlabel("Rotten Tomatoes Score")
    plt.ylabel("Density")
    plt.legend()
    plt.show()

    # Bar chart for Age Distribution
    age_distribution = pd.DataFrame({
        "Netflix": netflix_movies["Age"].value_counts(),
        "Disney+": disney_movies["Age"].value_counts()
    }).fillna(0)
    print("\nAge Distribution Comparison:")
    print(age_distribution)

    age_distribution.plot(kind="bar", figsize=(12, 6), title="Age Distribution for Netflix and Disney+")
    plt.ylabel("Number of Movies")
    plt.xlabel("Age Group")
    plt.show()
