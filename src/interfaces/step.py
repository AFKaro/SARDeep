from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class Step(ABC):
    step_name: str = field(default="Undefined")

    @abstractmethod
    def run_step(self):
        pass
