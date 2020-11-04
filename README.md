
## Description of the package:
This Python package extracts different metrics of an API and save this stadistics in JSON files. Also elaborates the Input file of https://github.com/AndreuJove/mastercrawlerTFG.

#### Input:
- URL API to request.

#### Output:
- JSON file showed in the next JSON schema.

```
schema := {
  #name -> JSONSchema string.
  #dateAndTime -> (JSONSchema stringWithFormat: 'date-time').
  #numberOfPets -> JSONSchema number } asJSONSchema.

```

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
        $ python3 main.py input_url "https://dev-openebench.bsc.es/monitor/rest/edam/aggregate?projection=description&projection=web&name=&label=null" -number_domains 36 -output_directory output_data -output_file_name_metrics metrics_api_v
<br />


## Build with:
- [Pandas](https://pandas.pydata.org/docs/) - is an opensource, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

<br />


## Authors

Andreu Jové

<br />


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE.MD](https://github.com/AndreuJove/mastercrawlerTFG/blob/master/LICENSE.md) file for details.