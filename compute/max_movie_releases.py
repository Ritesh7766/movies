def max_movie_releases(dataset):
    result_set = {}
    for map in dataset:
        key = map['ReleaseDate'].strip().split('-')[1]
        if key in result_set.keys():
            result_set[key] += 1
        else:
            result_set[key] = 1
    return result_set
