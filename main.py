
"""
import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
dataBase = client["neurolabDB"]

# Collection  Name
collection = dataBase['Products']

# Sample data
d = {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'}

# Insert above records in the collection
rec = collection.insert_one(d)

# Lets Verify all the record at once present in the record with all the fields
all_record = collection.find()

# Printing all records present in the collection
for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")
"""
import sys,os
from flight_fare.logger import logging
from flight_fare.exception import FlightFareException
from flight_fare.entity import config_entity
from config_entity import data_ingestion_config
if __name__=="__main__":
     try:
         training_pipeline_config=config_entity.TrainingPipelineConfig()
         data_ingestion_config=DataIngestionConfig(training_pipeline_config)
         print(data_ingestion_config.to_dict())
     except Exception as e:
          print(e)