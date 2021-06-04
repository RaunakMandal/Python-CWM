class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.open = False

    def open(self):
        if self.open:
            raise InvalidOperationError("Stream in already open")
        self.open = True

    def close(self):
        if not self.open:
            raise InvalidOperationError("Stream in already closed")
        self.open = False


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")
