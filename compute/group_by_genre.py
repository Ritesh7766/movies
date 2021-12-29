import operator

def group_by_genre(dataset):
    genre = {}
    for map in dataset:
        key = map['Genre'].strip()
        if key in genre.keys():
            genre[key] += 1
        else:
            genre[key] = 1
    genre = dict(sorted(genre.items(), key=operator.itemgetter(1), reverse=True) )
    return genre