from abc import ABCMeta, abstractmethod

class IGraph:
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_build_graph(self, data_arr):
        pass
