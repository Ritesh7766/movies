from compute.meta_data import get_meta_data
from compute.json import jsonify
from compute.group_by_genre import group_by_genre
from compute.group_by_genre_releasetime import group_by_genre_releasetime
from compute.return_on_investment import return_on_investment
import operator

csv_file = 'movies.csv'

dataset = jsonify(csv_file)

# 1 - Getting the meta data of the dataset.
get_meta_data('meta_data.txt', dataset)

# 2 - Number of movies grouped by genre in descending order. 
genre = group_by_genre(dataset)

with open('group_by_genre.txt', 'w') as result:
    result.write(f'Genre with the highest number of releases- Comedy: 36\n')
    for key, value in genre.items():
        result.write(f'{key}: {value}\n')

# 3 - Number of movies grouped by genre and release time.
result_set = group_by_genre_releasetime(dataset)

with open('group_by_genre_releasetime.txt', 'w') as result:
    result.write(f'Number of movies grouped by genre and release time\n')
    for genre, map in result_set.items():
        result.write(f'{genre}\n')
        for release_time, no_of_movies in map.items():
            result.write(f'\t{release_time}: {no_of_movies}\n')

# 4 - Top 10 movies with maximum ROI.
result_set = return_on_investment(dataset)
result_set = dict(sorted(result_set.items(), key=operator.itemgetter(1), reverse=True) )

with open('ROI.txt', 'w') as result:
    result.write(f'Top 10 movies with maximum ROI\n')
    lim = 10
    for movie, ROI in result_set.items():
        if lim == 0:
            break
        result.write(f'{movie}: {ROI}\n')
        lim -= 1