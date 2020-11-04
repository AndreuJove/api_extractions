import json

class JSON_writer():

    def __init__(self, path, **kwargs):
        self.path = path
        self.kwargs = kwargs
        self.write_json_file()
    
    def write_json_file(self):
        with open(f"{self.path}.json", 'w') as f:
            json.dump(self.kwargs, f)