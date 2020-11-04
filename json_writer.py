import json

class JSON_writer():
    """
    This class collect all the arguments to create a json file
    """
    def __init__(self, path, **kwargs):
        self.path = path
        self.kwargs = kwargs
        self.write_json_file()
    
    #Write on a json file the variable given with a known path
    def write_json_file(self):
        with open(f"{self.path}.json", 'w') as f:
            json.dump(self.kwargs, f)