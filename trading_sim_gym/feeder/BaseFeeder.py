from abc import ABCMeta, abstractmethod

class BaseFeeder(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, data, **kwargs):
        self._data = data
        self._index = 0
    
    def getDatas(self):
        return self._data
    
    def reset(self):
        self._index = 0
    
    @abstractmethod
    def next(self):
        raise NotImplementedError
    
    @abstractmethod
    def hasNext(self):
        raise NotImplementedError