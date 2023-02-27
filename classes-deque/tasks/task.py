class HistoryDict:
    def __init__(self, data):
        self.data = data
        self.hd = []   #history data

    def set_value(self, key, value):
        self.data[key] = value
        self.hd.append(key)
        if len(self.hd) > 5:
            self.hd.pop(0)

    def get_history(self):
        return self.hd

