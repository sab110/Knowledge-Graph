import numpy as np
import os
import pyjson5 as json5

from langchain_text_splitters import RecursiveCharacterTextSplitter 

# """
# Read data from datafile and store it in an array for embeddings
# """

def data_reader(folder_path):
    
    # documents = []
    document = []
    combined_text = None 

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        ext = "." + file_path.rsplit(".", 1)[-1].lower()
       
        
        

        if file_path.endswith('.json5'):
            # print("\n\n\n in json: , \t")
    
            with open(file_path, 'r',encoding='utf-8-sig') as file:

                # print("\n\n\n loaging file: ")
    
                data = json5.load(file)
                print("\n\n\n\n data ", data)
                
                document.extend(data)

                combined_text = "\n\n".join(data)
                

        
                print("\n\n\n\n combined text: \t", combined_text)
    print("\n\n\n\n document text: \t", document)


    return combined_text

def data_splitter(folder_path):
    documents = data_reader(folder_path)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    all_splits = (text_splitter.split_text(documents))

    print("\n\n\n\n all_splits : ", all_splits)

    return all_splits

# def embedding_model():

#     embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")

#     return embeddings


# # Retrival : it takes documents and embedding model and create vector db. 
# # Store embeddings in Qdrant DB and return a retriever
# def vector_db(all_splits, embeddings, persist_directory):

#     qdrant = Qdrant.from_texts(
#     all_splits,
#     embeddings,
#     path=persist_directory,
#     collection_name='collection',
#     force_recreate=True
# )

#     return qdrant



if __name__ == "__main__":

    folder_path = "./data/reduced_mixed_3/reduced_mixed_3"

    all_splits = data_splitter(folder_path)
