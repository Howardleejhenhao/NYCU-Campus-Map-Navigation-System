import json

class Path_Data():
    def __init__(self, path):
        self.data = {}
        self.data_path = path
        with open(path, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def path_length(self, start_point, end_point):
        start_point = str(start_point)
        end_point = str(end_point)
        path_length = self.data[start_point][end_point]["dis"]
        # path_route = self.data[start_point][end_point]["route"]
        return path_length

    def path_route(self, start_point, end_point):
        start_point = str(start_point)
        end_point = str(end_point)
        # path_length = self.data[start_point][end_point]["dis"]
        path_route = self.data[start_point][end_point]["route"]
        return path_route