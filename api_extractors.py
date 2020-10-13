from operator import getitem
from functools import  reduce
import json

class Api_Vicky_Extractor:
    def __init__(self, json, domain_classification):
        self.json = json
        self.domain_classification = domain_classification
        self.tools_list_unique_url = []
        self.problematic_url = []
        self.total_dict_domains_counter = {}
        self.values_codes = [{} for _ in range(len(self.domain_classification))]
        self.values_bioschemas_ssl_liscense_https = [[[0,0] for _ in range(4)] for _ in range(len(self.domain_classification))]
        self.path_to_http_codes = ['metrics', 'project', 'website', 'operational']
        self.path_to_website = ['metrics', 'project', 'website']
        self.acces_metrics_path = ['bioschemas', 'ssl', 'license', 'https']

    """
    Extract the value inside of a json file given a path to the value
    """
    @staticmethod
    def get_atribute_from_item_with_path(array_path_to_value, item):
        return reduce(getitem, array_path_to_value, item)

    @staticmethod
    def get_domain(url):
        return url.lower().split("://")[-1].split("/")[0].replace("www.", "")
    
    def iterate_in_json(self):
        for tool in self.json:
            url = self.get_atribute_from_item_with_path(["entities", 0, 'tools', 0, "web", "homepage"], tool)
            domain = self.get_domain(url)
            self.get_unique_urls(tool, url)
            self.extrat_http_codes_from_api(tool, url, domain)
            self.extract_all_bioschemas_ssl_license_https_from_api(tool, url, domain)

    def extrat_http_codes_from_api(self, item, url, domain):
        found_item = False
        if reduce(getitem, self.path_to_http_codes, item) in self.values_codes[-1]:
            self.values_codes[-1][reduce(getitem, self.path_to_http_codes, item)] += 1
        else:
            self.values_codes[-1][reduce(getitem, self.path_to_http_codes, item)] = 1
        for i,dom in enumerate(self.domain_classification): 
            if domain in list(dom.values())[0]:
                if reduce(getitem, self.path_to_http_codes, item) in self.values_codes[i]:
                    self.values_codes[i][reduce(getitem, self.path_to_http_codes, item)] += 1
                else:
                    self.values_codes[i][reduce(getitem, self.path_to_http_codes, item)] = 1
                found_item = True
        if not found_item:
                if reduce(getitem, self.path_to_http_codes, item) in self.values_codes[-2]:
                    self.values_codes[-2][reduce(getitem, self.path_to_http_codes, item)] += 1
                else:
                    self.values_codes[-2][reduce(getitem, self.path_to_http_codes, item)] = 1

    def extract_all_bioschemas_ssl_license_https_from_api(self, item, url, domain):
        #Extract the domain of the URL of the item of the api:      
        found_item = False
        #Create boolean false for adding in others if the item is not_found:
        for i,dom in enumerate(self.domain_classification[:-2]): 
            if domain in list(dom.values())[0]:
                #Iterate over the domains of the primary classification if it's found add on the corresponding site of the list of 0
                for j,last_path in enumerate(self.acces_metrics_path):
                    if reduce(getitem, self.path_to_website + [last_path], item):
                        self.values_bioschemas_ssl_liscense_https[i][j][0] += 1
                        self.values_bioschemas_ssl_liscense_https[-1][j][0] += 1
                    else:
                        self.values_bioschemas_ssl_liscense_https[i][j][1] += 1
                        self.values_bioschemas_ssl_liscense_https[-1][j][1] += 1
                found_item = True
        #If the item is not in any of the domains of the primary classification 
        if not found_item:
                for j,last_path in enumerate(self.acces_metrics_path):
                    if reduce(getitem, self.path_to_website + [last_path], item):
                        self.values_bioschemas_ssl_liscense_https[-2][j][0] += 1
                        self.values_bioschemas_ssl_liscense_https[-1][j][0] += 1
                    else:
                        self.values_bioschemas_ssl_liscense_https[-2][j][1] += 1
                        self.values_bioschemas_ssl_liscense_https[-1][j][1] += 1

    #This functions parses the urls of the tools given. Extract the problematic urls for crawling and extract the tools with unique url:
    def get_unique_urls(self, item, url):
        passing = True
        error_tool = False
        idTool = self.get_atribute_from_item_with_path(["entities", 0, 'tools', 0, "@id"], item)
        nameTool = self.get_atribute_from_item_with_path(["entities", 0, 'tools', 0, "name"], item)
        if url.endswith(".zip") or url.endswith(".pdf") or url.endswith(".mp4") or url.endswith(".gz") or url.endswith(".bz2") or url.startswith("ftp://") or len(url) < 7:
            self.problematic_url.append({'first_url_tool' : url, 'name' : nameTool, 'id' : idTool})
            error_tool = True
        if not url.startswith("http"):
            url = "https://www." + url
        if self.tools_list_unique_url and not error_tool:
            for i, k in enumerate(self.tools_list_unique_url):
                if k['first_url_tool'] == url:
                    passing = False
                    if type(k['name']) is str:
                        self.tools_list_unique_url[i]['name'] = [self.tools_list_unique_url[i]['name']]
                        self.tools_list_unique_url[i]['id'] = [self.tools_list_unique_url[i]['id']]
                    self.tools_list_unique_url[i]['name'].append(nameTool)
                    self.tools_list_unique_url[i]['id'].append(idTool)
                    continue
        if passing and not error_tool:
            self.tools_list_unique_url.append({'first_url_tool' : url, 'name' : nameTool, 'id' : idTool})

    #Counter of domains of the list of unique URL tools:
    def counter_domains_of_list_unique(self):
        for t in self.tools_list_unique_url:
            domain = self.get_domain(t['first_url_tool'])
            if domain in self.total_dict_domains_counter:
                self.total_dict_domains_counter[domain] += 1
            else:
                self.total_dict_domains_counter[domain] = 1
        







