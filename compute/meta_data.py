def get_meta_data(out_file, dataset):
    with open('meta_data.txt', 'w') as out_file:
        # Headers
        headers = list(dataset[0].keys() )    
        # Number of rows
        no_of_records = len(dataset)
        # Number of columns
        no_of_columns = len(headers)

        # Writing meta data in the out file.
        out_file.write(f'Headers: {headers}\n')
        out_file.write(f'Number of records: {no_of_records}\n')
        out_file.write(f'Number of columns: {no_of_columns}\n')