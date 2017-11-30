from abc import ABCMeta, abstractmethod

class IValidator:
    __metaclass__ = ABCMeta

    @abstractmethod
    def validate(self, data):
        pass

