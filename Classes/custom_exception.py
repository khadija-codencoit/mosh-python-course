class InvalidOperationError(Exception):
    pass



class Stram:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already close")
        self.opened = True

class Filestream(Stram):
    def read(self):
        print("Reading data from file")

class Filestream(Stram):
    def read(self):
        print("Reading data from file")