import pandas as pd
import matplotlib.pyplot as plt

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

movie_dict = {'years': years, 'durations': durations}

durations_df = pd.DataFrame(movie_dict)

plt.plot(durations_df['years'], durations_df['durations'])
plt.title('Netflix Movie Durations 2011-2020')

netflix_df = pd.read_csv('netflix_data.csv')

# Subset the netflix_df DataFrame such that only rows where the type is a "Movie" are preserved.
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']
netflix_df_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]

fig = plt.figure(figsize= (12, 8))
plt.scatter(netflix_df_movies_col_subset['release_year'], netflix_df_movies_col_subset['duration'])
plt.title('Movie Duration by Year of Release')
plt.show()