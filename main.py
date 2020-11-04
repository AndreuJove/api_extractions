import os
import sys
import logging
import argparse
from datetime import datetime
import requests
from api_extractors import Api_V_Extractor
from json_writer import JSON_writer
from constants import CLASSIFICATION_DOMAINS
from utils import create_df_from_dict, extract_columns_df


if __name__ == "__main__":

    # Instance of the class ArgumentParser:
    parser = argparse.ArgumentParser(description="Python project to extract and analyse data from a bioinformatics API")

    # Add the argument of URL of the api to extract the data:
    parser.add_argument('-input_url',
                        type=str,
                        default="https://dev-openebench.bsc.es/monitor/rest/edam/aggregate?projection=description&projection=web&name=&label=null",
                        help="The input API url for the extraction of data. The default value is: https://dev-openebench.bsc.es/monitor/rest/edam/aggregate?projection=description&projection=web&name=&label=null"
                        )

    # Add the argument of the number of the most common domains to extract. The default is 36:
    parser.add_argument('-number_domains',
                        type=int,
                        default=36,
                        help="Number of domains to extract, the default number is 36 domains."
                        )

    # Add the argument of output's directory name where the output files will be saved:
    parser.add_argument('-output_directory',
                        type=str,
                        default="output_data",
                        help="Name of the directory for the outputs files"
                        )

    # Add the argument of output's directory name where the output files will be saved:
    parser.add_argument('-output_file_name_metrics',
                        type=str,
                        default="metrics_api_v",
                        help="Name of the output file of the system"
                        )

    args = parser.parse_args()

    if not os.path.isdir(args.output_directory):
        os.mkdir(args.output_directory)

    #Create the logger:
    logging.basicConfig(format='%(levelname)s: %(message)s (%(asctime)s)', level=logging.INFO)

    #Request to the api and convert to a list of dictionaries to operate with python and catch if it is not available.
    try:
        logging.info("Starting the request. This might take few seconds")
        with requests.get(args.input_url, stream=True) as r:
            data = r.json()
    except:
        logging.error("The URL is given is not available in this moment. Try again in a few minutes again")
        sys.exit()

    # Instance the object to calculate the differents metrics:
    api_extractor_obj = Api_V_Extractor(data,
                                        CLASSIFICATION_DOMAINS)
    # Run the specific methods:
    logging.info("Starting the calculus of metrics from the API. This might take some seconds")
    api_extractor_obj.iterate_in_json()
    api_extractor_obj.counter_domains_of_list_unique()

    logging.info("Extraction of the stadistics done succesfully")
    # Create Dataframe of the counter of domains
    df = create_df_from_dict(api_extractor_obj.total_dict_domains_counter,
                                                    "Domain",
                                                    "Count",
                                                    args.number_domains)

    # Extract as a list the columns of the dataframe and return list of dictionaries to save in json:
    count_of_most_popular_domains = extract_columns_df(df)

    # Extract bioschemas, ssl, https, and license from the object by the classification domains.
    bioschemas_ssl_https_to_save = [dict([(list(api_extractor_obj.domain_classification[i].keys())[0], dict([(api_extractor_obj.acces_metrics_path[j], it) for j, it in enumerate(v)]))]) for i, v in enumerate(api_extractor_obj.values_bioschemas_ssl_liscense_https)]

    #Extract the different http codes from.
    final_http_codes_to_save = [{list(api_extractor_obj.domain_classification[i].keys())[0]: k} for i, k in enumerate(api_extractor_obj.values_codes)]

    #Instance of the JSON writer object
    json_writer_obj = JSON_writer(f"{args.output_directory}/{args.output_file_name_metrics}",
                                    time_of_execution = str(datetime.now()),
                                    bioschemas_ssl_https_license = bioschemas_ssl_https_to_save,
                                    http_codes_by_classification = final_http_codes_to_save,
                                    domains_classification = CLASSIFICATION_DOMAINS,
                                    domains_count = count_of_most_popular_domains,
                                    problematic_urls = api_extractor_obj.problematic_url,
                                    tools_list_unique = api_extractor_obj.tools_list_unique_url
                                )
    logging.info(f"Saved the stats in {args.output_directory}/{args.output_file_name_metrics}.json")