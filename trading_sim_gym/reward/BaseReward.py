from abc import ABCMeta, abstractmethod


class BaseReward(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def reset(self):
        raise NotImplementedError()

    @abstractmethod
    def reward(self):
        raise NotImplementedError()







