from abc import ABCMeta, abstractmethod
from enum import Enum
import gymnasium as gym
from TradingSimGym.feeder import BaseFeeder


class TradingEnvAction(Enum):
    BUY = 0
    SELL = 1
    HOLD = 2


class BaseEnv(gym.Env, metaclass=ABCMeta):
    def __init__(self, feeder: BaseFeeder):
        super(BaseEnv, self).__init__()

        self._feeder = feeder
