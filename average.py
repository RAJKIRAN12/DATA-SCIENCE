import pandas as pd

# File path to the dataset
file_path = r"C:\Users\rajkiran sapkota\Pictures\KALI\TU DORTMUN\MoviesOnStreamingPlatforms.csv"
def calculate_and_compare_averages(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Clean Rotten Tomatoes column (convert to numeric, handle missing values)
    data['Rotten Tomatoes'] = pd.to_numeric(data['Rotten Tomatoes'], errors='coerce')

    # Filter movies based on platform
    netflix_movies = data[data['Netflix'] == 1]  # Movies available on Netflix
    disney_movies = data[data['Disney+'] == 1]  # Movies available on Disney+

    # Calculate average Rotten Tomatoes score for each platform
    netflix_avg_score = netflix_movies['Rotten Tomatoes'].mean()
    disney_avg_score = disney_movies['Rotten Tomatoes'].mean()

    # Output results
    print(f"Average Rotten Tomatoes Score for Netflix Movies: {netflix_avg_score:.2f}")
    print(f"Average Rotten Tomatoes Score for Disney+ Movies: {disney_avg_score:.2f}")

    # Compare the platforms
    if netflix_avg_score > disney_avg_score:
        print("Netflix has better-rated movies on average.")
    elif netflix_avg_score < disney_avg_score:
        print("Disney+ has better-rated movies on average.")
    else:
        print("Both platforms have equally rated movies on average.")
