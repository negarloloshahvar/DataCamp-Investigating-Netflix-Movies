import pandas as pd

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

movie_dict = {'years': years, 'durations': durations}

durations_df = pd.DataFrame(movie_dict)
print(durations_df)

for index in durations_df.index:
    print('in ' + str(durations_df['years'][index]) + ' duration was ' + str(durations_df['durations'][index]))