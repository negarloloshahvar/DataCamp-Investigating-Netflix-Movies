import pandas as pd
import matplotlib.pyplot as plt

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

movie_dict = {'years': years, 'durations': durations}

durations_df = pd.DataFrame(movie_dict)

plt.plot(durations_df['years'], durations_df['durations'])
plt.title('Netflix Movie Durations 2011-2020')

netflix_df = pd.read_csv('netflix_data.csv')
print(netflix_df.head())
