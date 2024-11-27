def preprocess_data(movies_df):
    """
    Preprocess the dataset:
    - Drop unnecessary columns.
    - Filter movies for Netflix and Disney+.
    - Handle missing values if any.
    """
    # Drop unnecessary columns
    movies_df = movies_df.drop(['Unnamed: 0', 'ID', 'Type'], axis=1)

    # Filter Netflix and Disney+ movies
    netflix_movies = movies_df[movies_df['Netflix'] == 1].copy()
    disney_movies = movies_df[movies_df['Disney+'] == 1].copy()

    print(f"Netflix Movies: {netflix_movies.shape[0]}")
    print(f"Disney+ Movies: {disney_movies.shape[0]}")
    return netflix_movies, disney_movies

if __name__ == "__main__":
    from data_loading import load_dataset
    file_path = r"C:\Users\rajkiran sapkota\Pictures\KALI\TU DORTMUN\MoviesOnStreamingPlatforms.csv"
    movies_df = load_dataset(file_path)
    if movies_df is not None:
        preprocess_data(movies_df)
