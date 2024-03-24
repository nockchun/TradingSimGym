from abc import ABCMeta, abstractmethod


class BaseTrader(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def reset(self):
        raise NotImplementedError()

    @abstractmethod
    def trade(self):
        raise NotImplementedError()







