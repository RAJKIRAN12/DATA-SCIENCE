from data_loading import load_dataset
from data_preprocessing import preprocess_data
from descriptive_analysis import perform_descriptive_analysis
from hypothesis_testing import perform_hypothesis_tests

if __name__ == "__main__":
    file_path = r"C:\Users\rajkiran sapkota\Pictures\KALI\TU DORTMUN\MoviesOnStreamingPlatforms.csv"
    
    # Step 1: Load dataset
    movies_df = load_dataset(file_path)
    
    if movies_df is not None:
        # Step 2: Preprocess the data
        netflix_movies, disney_movies = preprocess_data(movies_df)

        # Step 3: Perform descriptive analysis
        perform_descriptive_analysis(netflix_movies, disney_movies)

        # Step 4: Perform hypothesis testing
        perform_hypothesis_tests(netflix_movies, disney_movies)
