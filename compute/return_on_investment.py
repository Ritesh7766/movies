def computeROI(boxOfficeCollection, budget):
    # Converting to crores.
    boxOfficeCollection = float(boxOfficeCollection.strip()) * 10000000
    budget = float(budget.strip()) * 10000000
    return (boxOfficeCollection - budget) / budget

def return_on_investment(dataset):
    result_set = {}
    for map in dataset:
        key = map['MovieName'].strip()
        result_set[key] = computeROI(map['BoxOfficeCollection'], map['Budget'])
    return result_set