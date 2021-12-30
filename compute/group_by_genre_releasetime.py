def group_by_genre_releasetime(dataset):
    result_set = {}
    for map in dataset:
        genre = map['Genre'].strip()
        release_time = map['ReleaseTime'].strip()
        if not genre in result_set.keys():
            result_set[genre] = {}
        if not release_time in result_set[genre].keys():
            result_set[genre][release_time] = 0
        result_set[genre][release_time] += 1
    return result_set