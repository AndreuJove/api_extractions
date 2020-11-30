
## Description of the package:
This Python package extracts different metrics of an API and save this stadistics in JSON files.

#### Input:
- URL API /tool.
- URL API /metrics.

#### Output:
- JSON file with all the stadistics: extracted_metrics.json.


<br />


## Package installation:

- 1) Open terminal.
- 2) Go to the current directory where you want the cloned directory to be added using 'cd'.
- 3) Run the command: <br />
        $ git clone https://github.com/AndreuJove/api_extractions
- 4) Install requirements.txt:<br />
        $ pip3 install -r requirements.txt
- 5) From the root run the following command:<br />
        $ python3 main.py
- 5) The name of the output files and the directory to save them can be changed using the following command line (write it with the default values):<br />
        $ python3 main.py -input_url_tools "https://openebench.bsc.es/monitor/tool" <br />
                        -input_url_metrics "https://openebench.bsc.es/monitor/metrics" <br />
                        -number_domains 36 <br />
                        -output_directory output_data <br />
                        -output_file_name_metrics extracted_metrics <br />
<br />


## Build with:
- [Pandas](https://pandas.pydata.org/docs/) - is an opensource, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
- [Requests](https://pandas.pydata.org/docs/) - is an opensource, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
- [Argparser](https://docs.python.org/3/library/argparse.html) - The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
- [Logging](https://docs.python.org/3/howto/logging.html) - Logging is a means of tracking events that happen when some software runs. The software’s developer adds logging calls to their code to indicate that certain events have occurred.
<br />


## Authors

Andreu Jové

<br />


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE.MD](https://github.com/AndreuJove/mastercrawlerTFG/blob/master/LICENSE.md) file for details.