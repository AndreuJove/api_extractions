import os
import logging
import argparse
import collections
from datetime import datetime
from api_extractors import MetricsExtractor
from json_writer import JSON_writer
from constants import CLASSIFICATION_DOMAINS, DICT_CODES_DESCRIPTION
from utils import create_df_from_dict, extract_columns_df, request_api, create_dataframe_access

def match_entries_tools_metrics_by_unique_homepage(metrics, tools):
    # Get the uniques homepages from tools and match with her @id.
    dict_id_homepage = calculate_unique_homepages(tools)
    # Add homepage in metrics entry for each @id
    return match_id_with_metric_add_homepage(dict_id_homepage, metrics)

def calculate_unique_homepages(tools):
    # Get the uniques websites and match with the first @id to match later with metrics.
    dict_id_homepage = {}
    for entry in tools:
        if entry['web']['homepage'] not in dict_id_homepage.values():
            entry['@id'] = entry['@id'].replace("/tool/", "/metrics/")
            dict_id_homepage[entry['@id']] = entry['web']['homepage']
    return dict_id_homepage

def match_id_with_metric_add_homepage(dict_id_homepage, metrics):
    # Filter entries metrics by @id and add his corresponding homepage.
    list_metrics_with_homepage = []
    for metric_entry in metrics:
        if metric_entry['@id'] in dict_id_homepage:
            metric_entry['homepage'] = dict_id_homepage[metric_entry['@id']]
            list_metrics_with_homepage.append(metric_entry)
    return list_metrics_with_homepage

def change_keys_of_dictionary(dictionary, dict_codes_description):
    # Change dictionary key values.
    for item in dictionary.copy().items():
        dictionary[dict_codes_description[item[0]]] = item[1]
        del dictionary[item[0]]
    return dictionary

def main(args):

    # Set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %y %H:%M:%S',
                        filename=f'{args.log_file_name}.log',
                        filemode='w')
    # Define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # Set a format which is simpler for console use.
    formatter = logging.Formatter('%(levelname)-12s %(filename)-12s %(message)s')

    # Tell the handler to use this format.
    console.setFormatter(formatter)

    # Add the handler to the root logger.
    logging.getLogger().addHandler(console)

    # Create the logger:
    logging.basicConfig(format='%(levelname)s: %(message)s ', level=logging.INFO)

    logging.info("Starting the requests. ESTIMATED TIME: 10s.")

    # Request APIs to extract information
    tools = request_api(args.input_url_tools)
    metrics = request_api(args.input_url_metrics)

    logging.info("Extracting entries from APIs. ESTIMATED TIME: 12s.")

    # Calculated the match.
    metrics_homepage = match_entries_tools_metrics_by_unique_homepage(metrics, tools)

    logging.info(f"Unique websites: {len(metrics_homepage)}")
    # Instance the object to calculate the differents metrics:
    api_extractor_obj = MetricsExtractor(metrics_homepage,
                                        CLASSIFICATION_DOMAINS)
    # Run the specific methods:
    logging.info("Calculating the stadistics. ESTIMATED TIME: 1s.")

    logging.info("Stadistics succesfully extracted.")

    # Create Dataframe of the counter of domains
    df_domains = create_df_from_dict(api_extractor_obj.total_dict_domains_counter,
                                                    "Domain",
                                                    "Count",
                                                    args.number_domains)
    # Extract as a list the columns of the dataframe and return list of dictionaries to save in json:
    count_of_most_popular_domains = extract_columns_df(df_domains)

    # Extract bioschemas, ssl, https, and license from the object by the classification domains.
    bioschemas_ssl_https_to_save = [dict([(list(api_extractor_obj.domain_classification[i].keys())[0], dict([(api_extractor_obj.acces_metrics_path[j], it) for j, it in enumerate(v)]))]) for i, v in enumerate(api_extractor_obj.values_bioschemas_ssl_liscense_https)]

    # Extract the different http codes from.
    final_http_codes_to_save = [{list(api_extractor_obj.domain_classification[i].keys())[0]: k} for i, k in enumerate(api_extractor_obj.values_codes)]

    # Access Tab dataframe:
    df_tab_access = create_dataframe_access(api_extractor_obj)

    # Instance of the JSON writer object
    JSON_writer(f"{args.output_directory}/{args.output_file_name_metrics}",
                                    time_of_execution = str(datetime.now()),
                                    bioschemas_ssl_https_license = bioschemas_ssl_https_to_save,
                                    http_codes_by_classification = final_http_codes_to_save,
                                    domains_classification = CLASSIFICATION_DOMAINS,
                                    domains_count = count_of_most_popular_domains,
                                    df_acces = df_tab_access.to_dict(orient="records"),
                                    dict_http_codes_count = change_keys_of_dictionary(dict(collections.Counter(df_tab_access['HTTP Code'].to_list() + [code for list_codes in df_tab_access['Redirections'].dropna().to_list() for code in list_codes])), DICT_CODES_DESCRIPTION),
                                    dict_uptimes_days = dict(collections.Counter(df_tab_access['Days Up'].dropna().astype(int).to_list())),
                                    total_len_tools = len(tools)
                                )
    logging.info(f"Saved the Stadistics in {args.output_directory}/{args.output_file_name_metrics}.json")

if __name__ == "__main__":
    # Instance of the class ArgumentParser:
    parser = argparse.ArgumentParser(description="Python project to extract and analyse data from a bioinformatics API")

    # Add the argument of URL of the api to extract the data:
    parser.add_argument('-input_url_tools',
                        type=str,
                        metavar="",
                        default="https://openebench.bsc.es/monitor/tool",
                        help="The input API url of tools. DEFAULT: https://openebench.bsc.es/monitor/tool"
                        )

    # Add the argument of URL of the API for metrics:
    parser.add_argument('-input_url_metrics',
                        type=str,
                        metavar="",
                        default="https://openebench.bsc.es/monitor/metrics",
                        help="The input API url of metrics data. DEFAULT: https://openebench.bsc.es/monitor/metrics"
                        )

    # Add the argument of the number of the most found domains to be extracted extract. The default is 36:
    parser.add_argument('-number_domains',
                        type=int,
                        metavar="",
                        default=40,
                        help="Number of domains to extract, the default number is 36 domains."
                        )

    # Add the argument of output's directory name where the output files will be saved:
    parser.add_argument('-output_directory',
                        type=str,
                        metavar="",
                        default="output_data",
                        help="Name of the directory for the outputs files"
                        )

    # Add the argument of output file name.
    parser.add_argument('-output_file_name_metrics',
                        type=str,
                        metavar="",
                        default="extracted_metrics",
                        help="Name of the output file of the system"
                        )

    # Add the argument of output's filename of log.
    parser.add_argument('-log_file_name',
                        type=str,
                        metavar="",
                        default="api_extraction",
                        help="Name of the output log file of the program"
                        )

    args = parser.parse_args()

    # If directory does not exist. Create the directory.
    if not os.path.isdir(args.output_directory):
        os.mkdir(args.output_directory)

    main(args)
    