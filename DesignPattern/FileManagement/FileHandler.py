from abc import ABCMeta, abstractmethod
from FileManagement.IFileHandler import *
from Validator.IValidator import *
import pickle
import os
import sys

class Director:
    __builder = None


    def set_builder(self, builder):
        self.__builder = builder


    def construct(self):
        file_handler =FileHandler()
        file_saver = self.__builder.get_file_saver()
        file_handler.set_file_saver(file_saver)

        file_loader = self.__builder.get_file_loader()
        file_handler.set_file_loader(file_loader)

        return file_handler

class Factory(metaclass=ABCMeta):

    @abstractmethod
    def get_file_saver(self):
        pass

    @abstractmethod
    def get_file_loader(self):
        pass


class FileSaver:
    @staticmethod
    def save(file, data):
        the_file = open(file, 'w')
        string = ""
        for l in data:
            new_data = [l[0], l[1], l[2], l[3], l[4], l[5], l[6]]
            for i in range(len(new_data)):
                string += str(new_data[i])
                # prevent a space at the end of a line
                if i != len(new_data) - 1:
                    string += ','

            string += "\n"
        the_file.write(string)
        the_file.close()

class FileLoader:
    @staticmethod
    def load(self, file):
        print("Loading file...")
        contents = []
        try:
            the_file = open(file, 'r')
        except FileNotFoundError:
            print("file does not exist.")
        else:
            for line in the_file:
                line = tuple(line.replace('\n', "").split(','))
                contents.append(line)

            the_file.close()
            validate = Validator.Validator()
            contents = validate.validate(contents)
            return contents


class FileHandler(IFileHandler, Factory):
    def __init__(self):
        self.__fileSaver = None
        self.__fileLoader = None

    def set_file_saver(self, filesaver):
        self.__fileSaver = filesaver

    def set_file_loader(self, fileloader):
        self.__fileLoader = fileloader

    def get_file_saver(self):
        return FileSaver()

    def get_file_loader(self):
        return FileLoader()

    def load_file(self, file):
        content = self.__fileLoader.load(file)
        return content

    def write_file(self, file, data):
        self.__fileSaver.save(file, data)

    def pack_pickle(self, graphs):
        # Raises exception if the default file does not exits and creates it should this exception be raised
        try:
            realfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\pickle.dat"
            if not os.path.exists(realfilepath):
                raise IOError
        except IOError:
            os.makedirs(os.path.dirname(realfilepath))
            pass
        # The pickle process
        pickleout = open(realfilepath, "wb")
        pickle.dump(graphs, pickleout)
        pickleout.close()

    # Brendan Holt
    # Used to unpickle graphs in the pickle file and return them to the interpreters graph list
    def unpack_pickle(self, filepath):
        # Raises exception if for some reason the default file has been deleted
        try:
            if os.path.exists(filepath) is False:
                raise IOError
        except IOError:
            print('File does not exits')
            return
        # The unpickle process
        picklein = open(filepath, "rb")
        graphs = pickle.load(picklein)
        picklein.close()
        # Return the graphs to the interpreter
        return graphs

    # Brendan Holt
    # Used to pickle the entire database to default pickle file
    def pickle_all(self, data):
        # Raises exception if for some reason the default file has been deleted
        try:
            realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
            if os.path.exists(realfiledirectory) is False:
                raise IOError
        except IOError:
            os.makedirs(os.path.dirname(realfiledirectory))
            return
        # The pickle process
        pickleout = open(realfiledirectory + "\\db_backup.dat", "wb")
        pickle.dump(data, pickleout)
        pickleout.close()