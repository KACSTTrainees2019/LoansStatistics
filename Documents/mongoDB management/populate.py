from pymongo import MongoClient
import csv


def populate_data(collection_name="data"):
    data = csv_to_data()
    # Connect to database
    # URI_string = "mongodb://localhost:27017/"
    with MongoClient() as client:
        # Populate data into database
        collection = client["loans_data_base"][collection_name]
        collection.insert(data)


def csv_to_data(csv_file_path="data.csv"):
    # open csv file, with 1st line of file as a field names
    with open(csv_file_path, newline="") as csv_file:
        records_list = []
        # make an object to read the records row by row
        reader = csv.DictReader(csv_file)
        labels = reader.fieldnames
        for row in reader:
            record = {}
            for label in labels:
                record[label] = row[label]
            records_list.append(record)

    return records_list


populate_data()
