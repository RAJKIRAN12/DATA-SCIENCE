import pandas as pd

def load_dataset(file_path):
    """
    Load the dataset from the given file path and return it as a DataFrame.
    """
    try:
        movies_df = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        print(f"Dataset contains {movies_df.shape[0]} rows and {movies_df.shape[1]} columns.")
        return movies_df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

if __name__ == "__main__":
    file_path = r"C:\Users\rajkiran sapkota\Pictures\KALI\TU DORTMUN\MoviesOnStreamingPlatforms.csv"
    load_dataset(file_path)
