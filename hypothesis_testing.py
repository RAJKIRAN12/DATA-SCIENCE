import scipy.stats as stats
import pandas as pd

def perform_hypothesis_tests(netflix_movies, disney_movies):
    """
    Perform hypothesis testing:
    - Compare Age restrictions using Chi-Square Test.
    - Compare Rotten Tomatoes Scores using T-Test.
    """
    # Age restrictions: Chi-Square Test
    age_netflix = netflix_movies['Age'].value_counts()
    age_disney = disney_movies['Age'].value_counts()

    age_contingency = pd.concat([age_netflix, age_disney], axis=1, keys=["Netflix", "Disney+"]).fillna(0)
    chi2, p_age, _, _ = stats.chi2_contingency(age_contingency)

    print(f"Chi-Square Test for Age Restrictions: Chi2 = {chi2}, p-value = {p_age}")
    if p_age < 0.05:
        print("Significant difference in Age Restrictions between Netflix and Disney+.")
    else:
        print("No significant difference in Age Restrictions between Netflix and Disney+.")

    # Rotten Tomatoes Scores: T-Test
    netflix_scores = netflix_movies['Rotten Tomatoes'].dropna()
    disney_scores = disney_movies['Rotten Tomatoes'].dropna()

    t_stat, p_score = stats.ttest_ind(netflix_scores, disney_scores, equal_var=False)
    print(f"T-Test for Rotten Tomatoes Scores: T = {t_stat}, p-value = {p_score}")
    if p_score < 0.05:
        print("Significant difference in Rotten Tomatoes Scores between Netflix and Disney+.")
    else:
        print("No significant difference in Rotten Tomatoes Scores between Netflix and Disney+.")

if __name__ == "__main__":
    from data_preprocessing import preprocess_data
    from data_loading import load_dataset
    file_path = r"C:\Users\rajkiran sapkota\Pictures\KALI\TU DORTMUN\MoviesOnStreamingPlatforms.csv"
    movies_df = load_dataset(file_path)
    if movies_df is not None:
        netflix_movies, disney_movies = preprocess_data(movies_df)
        perform_hypothesis_tests(netflix_movies, disney_movies)
