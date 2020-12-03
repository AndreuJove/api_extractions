import json

class JsonWriter():
    """

    This class collect all the arguments to save them on a json file

    """
    def __init__(self, path, **kwargs):
        # collect all kwargs (key=value) to save
        self.path = path
        self.kwargs = kwargs
        self.write_json_file()

    def write_json_file(self):
        # Write on a json file the variable given with a known path
        with open(f"{self.path}.json", 'w') as file:
            json.dump(self.kwargs, file)
