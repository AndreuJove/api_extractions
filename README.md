
## Description of the package:
This Python package extracts different metrics of an API and save this stadistics in JSON files. Also elaborates the Input file of https://github.com/AndreuJove/mastercrawlerTFG.

#### Input:
- URL API to request.

#### Output:
- JSON file that contains the count of the most common domains of the unique URLs in these amount of bioinformatics tools.
- JSON file of the primary classification about the precedence of these domains: Universities, Institutions, Life Science, Generic and Tools Collections.
- JSON file of problematic extensions of the URLs for crawling. Example: .pdf, .gz, etc.
- JSON file of the tools with unique URLs. This file is the input for https://github.com/AndreuJove/mastercrawlerTFG.
- JSON file that contains the following metrics: bioschemas, ssl, https and licenses grouped by the primary classification mentioned before.
- JSON file that contains the HTTP codes received from the tools grouped by the primary classification mentioned before.
<br />


## Package installation:

- 1) Open terminal.
- 2) Go to the current directory where you want the cloned directory to be added using 'cd'.
- 3) Run the command: 
        $ git clone https://github.com/AndreuJove/api_extractions
- 4) Install requirements.txt:
        $ pip3 install -r requirements.txt
- 5) From the root run the following command:
        $ python3 main.py
- 5) The name of the output files and the directory to save them can be changed using the following command line (write it with the default values):
        $ python3 main.py -o_n_domains 36 -o_directory output_data -o_tools_unique_url tools_unique_url -o_problematic_tools problematic_tools -o_bio_ssl_https bioschemas_ssl_https_license_by_classification -o_https_codes http_codes_by_classification -o_classification primary_classification_domains
        -o_count_domains count_domains_tools_unique_url
<br />


## Build with:
- [Pandas](https://pandas.pydata.org/docs/) - is an opensource, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

<br />


## Authors

Andreu Jové

<br />


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE.MD](https://github.com/AndreuJove/mastercrawlerTFG/blob/master/LICENSE.md) file for details.