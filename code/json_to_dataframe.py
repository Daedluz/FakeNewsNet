import pandas as pd
from os import listdir, walk
from os.path import isfile, isdir, join
import json
# from pandas.io.json import json_normalize

def json_to_csv (mypath, csv_name):

    file_list = []
    for root, dirs, files in walk(mypath):
        for f in files:
            fullpath = join(root, f)
            file_list.append(fullpath)
            # print(fullpath)

    tmp = []
    for i in range(len(file_list)):
        if ("retweets" not in file_list[i]):
            tmp.append(file_list[i])
    file_list = tmp

    with open(file_list[0]) as json_data:
        data = json.load(json_data)

    df = pd.json_normalize(data)
    df["text"][0] = df["text"][0].replace('\u2019','\'')
    df["text"][0] = df["text"][0].replace('\n',' ')

    for i in range (1, len(file_list)):
        print(i, end=' ')
        with open(file_list[i]) as json_data:
            data = json.load(json_data)

        temp_df = pd.json_normalize(data)

        # if (i == 32):
        #     print(temp_df["text"].count('\n\n')) 

        temp_df["text"][0] = temp_df["text"][0].replace('\u2019','\'')
        temp_df["text"][0] = temp_df["text"][0].replace('\n',' ')

        # if (i == 32):
        #     print(temp_df["text"].count('\n\n'))

        df = df.append(temp_df, ignore_index=True)

    # Drop Summary(all empty) and some other un-used columns 
    df = df.drop(columns=df.columns[11:])
    df.to_csv(csv_name)

# json_to_csv("./fakenewsnet_dataset/politifact/fake", "politifact_fake.csv")

# json_to_csv("./fakenewsnet_dataset/politifact/real", "politifact_real.csv")

json_to_csv("./fakenewsnet_dataset/gossipcop/fake", "gossip_fake.csv")

json_to_csv("./fakenewsnet_dataset/gossipcop/real", "gossip_real.csv")