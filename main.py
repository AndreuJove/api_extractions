import json
import time
import os
import requests
import argparse
from utils import*
import api_extractors
import sys


if __name__ == "__main__":

    # Instance of the class ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Bioinformatics tools API extraction")

    # Add the argument of URL of the api to extract the data:
    parser.add_argument('-i', '--url', type=str, default="https://dev-openebench.bsc.es/monitor/rest/edam/aggregate?projection=description&projection=web&name=&label=null",
                        help="URL API for extraction")

    # Add the argument of the number of the most common domains to extract. The default is 36:
    parser.add_argument('-o_n_domains', '--number_of_domains',
                        type=int, default=36, help="Number of domains to extract")

    # Add the argument of output's directory name where the output files will be saved:
    parser.add_argument('-o_directory', '--output_directory', type=str,
                    default="output_data", help="Name of the directory for the outputs files")

    # Add the argument of output's filename of the file of the list of tools with unique URL:
    parser.add_argument('-o_tools_unique_url', '--tools_unique_url', type=str,
                    default="tools_unique_url", help="File name for the tools with unique url")

    # Add the argument of output filename of the list of problematic tools for crawling in the API:
    parser.add_argument('-o_problematic_tools', '--problematic_tools', type=str,
                default="problematic_tools", help="File name for the problematic tools")
    
    # Add the argument of output filename of the extraced metrics: bioschemas, ssl, https and license resulted from the API.
    parser.add_argument('-o_bio_ssl_https', '--bioschemas_ssl_https_license', type=str,
                default="bioschemas_ssl_https_license_by_classification", help="File name of the extracted metrics: bioschemas, ssl, https and license")

    # Add the argument of output filename of the extraced http codes of the API.
    parser.add_argument('-o_https_codes', '--http_codes', type=str,
                default="http_codes_by_classification", help="File name of the https codes received for the different domains")

    # Add the argument of output filename of the primary classification about domains.
    parser.add_argument('-o_classification', '--primary_classification', type=str,
                default="primary_classification_domains", help="Primary classification of the domains in Universities, Tools Collections, Life Sciences, Generic and Institutions")

    # Add the argument of output filename of the primary classification about domains.
    parser.add_argument('-o_count_domains', '--count_domains', type=str,
                default="count_domains_tools_unique_url", help="The final count of the domains of tools with unique URL")

    args = parser.parse_args()

    if not os.path.isdir(args.output_directory):
        os.mkdir(args.output_directory)

    start = time.time()

    # Primary classification of domains, can be change it in the future.
    UNIVERSITY = ['ncbi.nlm.nih.gov', 'ebi.ac.uk',
                  'broadinstitute.org', 'csbio.sjtu.edu.cn', 'dna.leeds.ac.uk']
    INSTITUTIONAL = ['cbs.dtu.dk', 'galaxy.pasteur.fr', 'bioinformatics.psb.ugent.be', 'zhanglab.ccmb.med.umich.edu', 'jci-bioinfo.cn',
                     'sanger.ac.uk', 'protein.bio.unipd.it',  'imgt.org', 'genius.embnet.dkfz-heidelberg.de',
                     'bioinformatics.psb.ugent.be', 'ccb.jhu.edu', 'tools.proteomecenter.org', 'genome.sph.umich.edu']
    LIFESCIENCE = ['bioconductor.org', 'emboss.open-bio.org']
    COLLECTIONS = ['bioinformatics.org', 'ms-utils.org', 'web.expasy.org']
    GENERIC = ['github.com', 'cran.r-project.org', 'doi.org', 'imtech.res.in', 'pypi.python.org',
               'sourceforge.net', 'sites.google.com', 'metacpan.org', 'gitlab.com', 'code.google.com', 'bitbucket.org']

    # Create list of dictionaries to save in json format:
    primary_classifcation_domains = [
        {'university': UNIVERSITY},
        {'institucional': INSTITUTIONAL},
        {'lifeScience': LIFESCIENCE},
        {'collections': COLLECTIONS},
        {'generic': GENERIC},
        {'others': []},
        {'total': []}
    ]


    # Request to the api and convert to a list of dictionaries to operate with python and catch if it is not available.
    try:
        with requests.get(args.url, stream=True) as r:
            data = r.json()
    except:
        print("The URL given is not available in this moment")
        sys.exit()

    # Instance the object to calculate the differents metrics:
    api_extractor_obj = api_extractors.Api_Vicky_Extractor(
        data, primary_classifcation_domains)
    # Run the specific methods:
    api_extractor_obj.iterate_in_json()
    api_extractor_obj.counter_domains_of_list_unique()

    # Create Dataframe of the counter of domains
    df = create_dataframe_from_dict_and_give_length(
        api_extractor_obj.total_dict_domains_counter, "Domain", "Count", args.number_of_domains)
    # Extract as a list the columns of the dataframe and return list of dictionaries to save in json:
    count_of_most_popular_domains = get_lists_of_dictionaries_of_dataframe_columns(
        df)

    # Safe tools lists for scrapy crawler in json format:
    write_json_file(api_extractor_obj.tools_list_unique_url,
                    f'{args.output_directory}/{args.tools_unique_url}.json')

    # Safe problematic tools for scrapy crawler in json format:
    write_json_file(api_extractor_obj.problematic_url,
                    f'{args.output_directory}/{args.problematic_tools}.json')
    # Distribute the values of bioschemas, ssl, https in a comprensive format and save to json file:
    final_value_metrics_bioschemas_ssl_https_to_save = [dict([(list(api_extractor_obj.domain_classification[i].keys())[0], dict(
        [(api_extractor_obj.acces_metrics_path[j], it) for j, it in enumerate(v)]))]) for i, v in enumerate(api_extractor_obj.values_bioschemas_ssl_liscense_https)]
    write_json_file(final_value_metrics_bioschemas_ssl_https_to_save,
                    f'{args.output_directory}/{args.bioschemas_ssl_https_license}.json')

    # Distribute the http codes of in a comprensive format save to json file:
    final_http_codes_to_save = [{list(api_extractor_obj.domain_classification[i].keys())[
        0]: k} for i, k in enumerate(api_extractor_obj.values_codes)]
    write_json_file(final_http_codes_to_save,
                    f'{args.output_directory}/{args.http_codes}.json')

    # Safe list of dictionaries: item is a domain and his count in a jsonfile.
    write_json_file(primary_classifcation_domains,
                    f'{args.output_directory}/{args.primary_classification}.json')

    # Safe list of dictionaries about primary classification of groupation in a jsonfile.
    write_json_file(count_of_most_popular_domains,
                    f'{args.output_directory}/{args.count_domains}.json')

    end = time.time()
    print(f"Time of execution: {end - start}")
