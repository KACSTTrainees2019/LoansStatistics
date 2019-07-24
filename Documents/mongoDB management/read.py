from pymongo import MongoClient


def access_database(collection_name="data"):
    """
  Description:
    Connect to mongoDB database, and retrieves the specified collection
  ________________________________________________________________________
  Return:
    list of dictionaries
    """
    # Connect to database
    URI_string = "mongodb://localhost:27017/"
    with MongoClient(URI_string) as client:
        collection = client["loans_data_base"][collection_name]
        records = collection.find({}, {"_id": 0})
        records_list = []
        for record in records:
            records_list.append(record)

        return records_list


print(access_database())
