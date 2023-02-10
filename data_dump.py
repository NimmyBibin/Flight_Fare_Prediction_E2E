import pymongo
import pandas as pd
import json

client=pymongo.MongoClient("mongodb+srv://NimmyBibin:Bibin@cluster0.fadr4rz.mongodb.net/?retryWrites=true&w=majority"
)
DATA_FILE_PATH="/config/workspace/dataset/Data_Train.csv"
DATABASE_NAME="flight"
COLLECTION_NAME="flight_fare"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[1])
    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
