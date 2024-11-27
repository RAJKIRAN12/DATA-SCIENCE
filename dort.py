import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Ensure the correct path format
for dirname, _, filenames in os.walk(r"C:\Users\rajkiran sapkota\Pictures\KALI\TU DORTMUN\MoviesOnStreamingPlatforms.csv"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Load the dataset
movies_df = pd.read_csv(r"C:\Users\rajkiran sapkota\Pictures\KALI\TU DORTMUN\MoviesOnStreamingPlatforms.csv")

# Show the first few rows
print(movies_df.head())

# Drop unnecessary columns
movies_df = movies_df.drop(['Unnamed: 0', 'ID', 'Type'], axis=1)

# Define palette for the plot
palette_colors = ["#72efdd", "#a2d2ff", "#ff6b6b", "#95d5b2"]
custom_palette = sns.set_palette(sns.color_palette(palette_colors))

# Function to create a donut plot
def donut_plot(splot, data, label, title):
    plt.subplot(splot)
    donut_center_circle = plt.Circle((0, 0), 0.5, color="black", fc="white", linewidth=2)
    plt.pie(
        data, 
        labels=label, 
        colors=palette_colors,
        autopct="%.2f%%",
        shadow=True
    )
    current_fig = plt.gcf()
    current_fig.gca().add_artist(donut_center_circle)
    plt.title(title)

# Filter movies by platform and age group
platform_18_plus_movies = {
    col: movies_df[(movies_df[col] == 1) & (movies_df["Age"] == "18+")]
    for col in ["Netflix", "Hulu", "Prime Video", "Disney+"]
}

# Count movies for each platform
adult_movie_counts = {platform: df.shape[0] for platform, df in platform_18_plus_movies.items()}

# Data for the plot
data = list(adult_movie_counts.values())

# Create the donut plot
plt.figure(figsize=(8, 8))
donut_plot(121, data, ["Netflix", "Hulu", "Prime Video", "Disney+"], "18+ Movies across platforms")
plt.show()
