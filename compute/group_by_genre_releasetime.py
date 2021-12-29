def group_by_genre_releasetime(dataset):
    result_set = {}
    for map in dataset:
        genre = map['Genre'].strip()
        if genre in result_set.keys():
            release_time = map['ReleaseTime'].strip()
            if release_time in result_set[genre].keys():
                result_set[genre][release_time] += 1
            else:
                result_set[genre][release_time] = 1
        else:
            result_set[genre] = {}
    return result_set