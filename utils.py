import sys
import json
import pandas as pd
import requests

def create_df_from_dict(dict_given, col_1, col_2, number_for_length_df):
    # Creates a dataframe of 2 columns given, from a dict and displays the length of the dataframe. 
    return pd.DataFrame(dict_given.items(), columns=[
                    col_1, col_2]).sort_values(by=col_2, ascending=False)[:number_for_length_df] 

def extract_columns_df(df):
    # Extract the columns of a dataframe and safe as a list of dictionaries ({<name_column> : <list of values in the column>})
    list_out = []
    for col in df.columns:
        list_out.append({col : df[col].tolist()})
    return list_out

def open_json(pth):
    # Open JSON file and return with encoding:
    with open(pth, "r") as file:
        return json.load(file)

def write_json_file(data, path):
    # Write on a json file with given path:
    with open(path, 'w') as file:
        json.dump(data, file)

def request_api(url):
    # Make a request to an API to recieve format JSON
    headers = {'Accept' : 'application/json',
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)"
                }
    try:
        with requests.get(url, stream=True, headers = headers, timeout=15) as r:
            return r.json()
    except Exception as e:
        print(f"ERROR: the website {url} to request is not available at this moment.")
        print(f"INFO: Exception raised: {str(e)}.")
        sys.exit()

def create_dataframe_access(obj):
    # Create dataframe from different list
    return pd.DataFrame(list(zip(obj.websites, 
                                obj.operationals, 
                                obj.uptime_30_days, 
                                obj.average_access_time, 
                                obj.redirections
                                )), 
                                columns =['Website', 
                                         'HTTP Code', 
                                            "Days Up", 
                                            "Access time", 
                                            "Redirections"
                                        ]
                        ) 
