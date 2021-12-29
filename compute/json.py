import csv

def jsonify(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        # Dataset is returned in JSON format.
        dataset = []
        for row in reader:
            dataset.append(row)
    return dataset