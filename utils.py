import json
import pandas as pd

#Creates a dataframe of 2 columns given, from a dict and displays the length of the dataframe. 
def create_dataframe_from_dict_and_give_length(dict_given, col_1, col_2, number_for_length_df):
    return pd.DataFrame(dict_given.items(), columns=[
                    col_1, col_2]).sort_values(by=col_2, ascending=False)[:number_for_length_df] 

#Extract the columns of a dataframe and safe as a list of dictionaries ({<name_column> : <list of values in the column>})
def get_lists_of_dictionaries_of_dataframe_columns(df):
    list_out = []
    for col in df.columns:
        list_out.append({col : df[col].tolist()})
    return list_out

#Open JSON file and return a list of dictionaries:
def open_json(pth):
    with open(pth, "r") as fp:
        jsonInput_data = json.load(fp)
    return jsonInput_data

#Write on a json file a list of dictionaries:
def write_json_file(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)


