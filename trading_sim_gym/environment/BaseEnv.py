from abc import ABCMeta, abstractmethod
from enum import Enum
import gymnasium as gym
from trading_sim_gym import feeder, reward, trader


class TradeAction(Enum):
    BUY = 0
    SELL = 1
    HOLD = 2


class BaseEnv(gym.Env, metaclass=ABCMeta):
    def __init__(self, feeder: feeder.BaseFeeder, trader: trader.BaseTrader, reward: reward.BaseReward):
        super(BaseEnv, self).__init__()

        self._feeder = feeder
        self._trader = trader
        self._reward = reward
        self._terminated = False
        self._truncated = False

    @abstractmethod
    def _reset(self):
        raise NotImplementedError()

    @abstractmethod
    def _observation(self):
        raise NotImplementedError()

    @abstractmethod
    def _info(self):
        raise NotImplementedError()

    @abstractmethod
    def _reward(self):
        raise NotImplementedError()

    def reset(self):
        self._feeder.reset()
        self._trader.reset()
        self._reward.reset()
        self._done = False
        self._reset()

        return self._observation()

    def step(self, action: TradeAction):
        observation = self._observation()
        reward = self._reward()
        info = self._info()

        return observation, reward, self._terminated, self._truncated, info

    def render(self, mode: str = "human"):
        ...

    def close(self):
        ...
