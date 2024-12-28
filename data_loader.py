import json5
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.graphs.graph_document import GraphDocument
import json
import csv



def read_json5_files(directory):
    data_array = []

    # Loop through all files in the specified directory
    for filename in os.listdir(directory):
        # if filename.startswith("sdgIndicatorData") and filename.endswith(".json5"):
        if filename.endswith(".json5"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                try:
                    data = json5.load(file)
                    data_array.append(data)
                except Exception as e:
                    print(f"Error reading {filename}: {e}")

    return data_array

def splitter(directory):
    # Specify the directory containing the JSON5 files
 

    # Read the JSON5 files and store the data in an array
    data_array = read_json5_files(directory)

    # Convert the data to strings for the text splitter
    data_strings = [json5.dumps(data) for data in data_array]

    # Initialize the text splitter
    text_splitter = RecursiveCharacterTextSplitter()

    # Split the text data
    all_splits = []
    for data_string in data_strings:
        splits = text_splitter.split_text(data_string)
        all_splits.extend(splits)

    # # Print the splits to verify
    # for split in all_splits:
    #     print(split)
    
    return all_splits






# dir = "./data/reduced_mixed_3/reduced_mixed_3"
dir = './dump_data'
data = splitter(dir)


for i in data:
    print("\n\n\n\n -----------------------------------------------------\n\n data: \n", i)
    

# import pandas as pd

# # Assuming 'data' is the parsed JSON list
# attributes = data[0]['attributes']
# dimensions = data[0]['dimensions']
# records = data[0]['data']

# # Flatten attributes
# attributes_df = pd.DataFrame([
#     {'id': attr['id'], 'code': code['code'], 'description': code['description'], 'sdmx': code['sdmx']}
#     for attr in attributes for code in attr['codes']
# ])

# # Flatten dimensions
# dimensions_df = pd.DataFrame([
#     {'id': dim['id'], 'code': code['code'], 'description': code['description'], 'sdmx': code['sdmx']}
#     for dim in dimensions for code in dim['codes']
# ])

# # Flatten data records
# records_df = pd.DataFrame(records)

# # Display the dataframes
# print("\n\n\n\n\nattributes_df ",attributes_df.head())
# print("\n\n\n\n\dimensions_df",dimensions_df.head())
# print("\n\n\n\n\nrecords_df ",records_df.head())
