from operator import getitem
from functools import reduce

class MetricsExtractor:
    # Class for extracting different metrics of the api.

    def __init__(self, json, domain_classification):
        self.json = json
        self.domain_classification = domain_classification
        self.websites = []
        self.total_dict_domains_counter = {}
        self.path_to_http_codes = ['project', 'website', 'operational']
        self.path_to_website = ['project', 'website']
        self.metrics_website = ['bioschemas', 'ssl', 'license', 'https']
        self.values_bioschemas_ssl_liscense_https = [[[0,0] for _ in range(4)] for _ in range(len(self.domain_classification))]
        self.values_codes = self.create_empty_dict_http_codes_by_classification()
        self.operationals = []
        self.uptime_30_days = []
        self.average_access_time = []
        self.redirections = []
        self.iterate_in_json()
        self.counter_domains_from_websites()
        self.format_values_bioschemas_ssl_license_https()

    @staticmethod
    def get_domain(url):
        # Returns the domain from a url given.
        return url.lower().split("://")[-1].split("/")[0].replace("www.", "")

    @staticmethod
    def check_if_value_exists(item, path):
        # Check if the value exist inside a path and return it.
        try:
            return reduce(getitem, path, item)
        except KeyError:
            return None

    def format_values_bioschemas_ssl_license_https(self):
        # Change the format of the list of lists extracted to dictionaries with keys
        dict_groups_classification = {}
        for i, key in enumerate(self.domain_classification.keys()):
            dict_groups_classification.setdefault(key, self.values_bioschemas_ssl_liscense_https[i])
        for key, value in dict_groups_classification.items():
            dict_metrics = {}
            for i, metric in enumerate(value):
                dict_metrics.setdefault(self.metrics_website[i], metric)
            dict_groups_classification[key] = dict_metrics
        self.values_bioschemas_ssl_liscense_https = dict_groups_classification

    def create_empty_dict_http_codes_by_classification(self):
        # Create a dict with the classification domains
        dict_http_codes = {}
        for key in self.domain_classification.keys():
            dict_http_codes.setdefault(key, {})
        return dict_http_codes

    def extract_redirections(self, item):
        # Check if there are redirections and return the list of codes.
        redirects_dict = self.check_if_value_exists(item, ['project', 'website', 'redirects'])
        if redirects_dict:
            return [dict_item['status'] for dict_item in redirects_dict]
        return None

    def iterate_in_json(self):
        # Iterates in the array of tools and send to diferent functions the items to collect them
        for tool in self.json:
            url = tool["homepage"]
            domain = self.get_domain(url)
            self.websites.append(url)
            self.operationals.append(self.check_if_value_exists(tool, ['project','website','operational']))
            self.uptime_30_days.append(self.check_if_value_exists(tool, ['project', 'website', 'last_month_access', 'uptime_days']))
            self.average_access_time.append(self.check_if_value_exists(tool, ['project', 'website', 'last_month_access', 'average_access_time']))
            self.redirections.append(self.extract_redirections(tool))
            self.extract_all_bioschemas_ssl_license_https_from_api(tool, domain)
            self.extract_http_codes_from_api(tool, domain)

    def extract_http_codes_from_api(self, item, domain):
        # Extract the http codes by classification domains.
        found_item = False
        if reduce(getitem, self.path_to_http_codes, item) in self.values_codes["total"]:
            self.values_codes["total"][reduce(getitem, self.path_to_http_codes, item)] += 1
        else:
            self.values_codes["total"][reduce(getitem, self.path_to_http_codes, item)] = 1
        for group, list_domains in self.domain_classification.items():
            if domain in list_domains:
                if reduce(getitem, self.path_to_http_codes, item) in self.values_codes[group]:
                    self.values_codes[group][reduce(getitem, self.path_to_http_codes, item)] += 1
                else:
                    self.values_codes[group][reduce(getitem, self.path_to_http_codes, item)] = 1
                found_item = True
        # If the item is not in any of the domains of the primary classification.
        if not found_item:
            if reduce(getitem, self.path_to_http_codes, item) in self.values_codes["others"]:
                self.values_codes["others"][reduce(getitem, self.path_to_http_codes, item)] += 1
            else:
                self.values_codes["others"][reduce(getitem, self.path_to_http_codes, item)] = 1

    def extract_all_bioschemas_ssl_license_https_from_api(self, item, domain):
        # Extract the domain of the URL of the item of the api:
        found_item = False
        # Create boolean false for adding in others if the item is not_found:
        for i, list_domains in enumerate(self.domain_classification.values()):
            if domain in list_domains:
                # Iterate over the domains of the primary classification if it's found add on the corresponding site of the list of 0
                for j, metric in enumerate(self.metrics_website):
                    if reduce(getitem, self.path_to_website + [metric], item):
                        self.values_bioschemas_ssl_liscense_https[i][j][0] += 1
                        self.values_bioschemas_ssl_liscense_https[-1][j][0] += 1
                    else:
                        self.values_bioschemas_ssl_liscense_https[i][j][1] += 1
                        self.values_bioschemas_ssl_liscense_https[-1][j][1] += 1
                found_item = True
        # If the item is not in any of the domains of the primary classification.
        if not found_item:
            for j, metric in enumerate(self.metrics_website):
                if reduce(getitem, self.path_to_website + [metric], item):
                    self.values_bioschemas_ssl_liscense_https[-2][j][0] += 1
                    self.values_bioschemas_ssl_liscense_https[-1][j][0] += 1
                else:
                    self.values_bioschemas_ssl_liscense_https[-2][j][1] += 1
                    self.values_bioschemas_ssl_liscense_https[-1][j][1] += 1

    def counter_domains_from_websites(self):
        # Counter of domains of the list of unique URL of tools:
        for website in self.websites:
            domain = self.get_domain(website)
            if domain in self.total_dict_domains_counter:
                self.total_dict_domains_counter[domain] += 1
            else:
                self.total_dict_domains_counter[domain] = 1
