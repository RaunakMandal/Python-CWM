from abc import ABC, abstractmethod
# abstract base class


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
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

    @abstractmethod
    def read(self):  # obviously has to implement the method
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory")


stream = NetworkStream()
print(stream.read())
