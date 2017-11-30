# Database applied Factory method

import sqlite3
from abc import ABCMeta, abstractmethod
from Database.IDatabase import IDatabase


class DatabaseTemplate(metaclass=ABCMeta):
    def __init__(self):
        self.database_name = ""
        self.connection = None
        self.cursor = None

    def build_database(self, name):
        self.set_database_name(name)
        self.set_database_connection(name)
        self.set_database_cursor()

    def set_database_name(self, name):
        self.database_name = name

    def set_database_connection(self):
        self.connection = sqlite3.connect(self.database_name)

    def set_database_cursor(self):
        self.cursor = self.connection.cursor()


class Database(IDatabase, DatabaseTemplate):
    def __init__(self, database_name):
        super().__init__()
        self.build_database(database_name)

    @abstractmethod
    def backup_database(self):
        pass

    @abstractmethod
    def execute_sql(self, sql):
        pass

    @abstractmethod
    def write_to_database(self, data):
        pass

    @abstractmethod
    def display_data(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def reset(self):
        pass
