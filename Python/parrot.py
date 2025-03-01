from abc import ABC, abstractmethod
from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class IParrot(ABC):
    _base_speed: float = 12.0

    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def cry(self):
        pass

class EuropeanParrot(IParrot):
    def speed(self):
        return self._base_speed

    def cry(self):
        return "Sqoork!"

class AfricanParrot(IParrot):

    def cry(self):
        return "Sqaark!"

    def speed(self):
        pass


class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        match self._type:
            case ParrotType.EUROPEAN:
                parrot = EuropeanParrot()
                return parrot.speed()
            case ParrotType.AFRICAN:
                return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)
            case ParrotType.NORWEGIAN_BLUE:
                return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def cry(self):
        match self._type:
            case ParrotType.EUROPEAN:
                parrot = EuropeanParrot()
                return parrot.cry()
            case ParrotType.AFRICAN:
                parrot = AfricanParrot()
                return parrot.cry()
            case ParrotType.NORWEGIAN_BLUE:
                return "Bzzzzzz" if self._voltage > 0 else "..."

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def _load_factor(self):
        return 9.0

    def _base_speed(self):
        return 12.0
