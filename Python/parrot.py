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
    def __init__(self, number_of_coconuts: int):
        self._number_of_coconuts = number_of_coconuts

    def cry(self):
        return "Sqaark!"

    def speed(self):
        return max(0, self._base_speed - self._load_factor() * self._number_of_coconuts)

    def _load_factor(self):
        return 9.0

class NorwegianBlueParrot(IParrot):
    def __init__(self, voltage: int, nailed: bool):
        self._voltage = voltage
        self._nailed = nailed

    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."

    def speed(self):
        return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed])



class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    @staticmethod
    def _create(type_of_parrot, number_of_coconuts, voltage, nailed) -> IParrot:
        match type_of_parrot:
            case ParrotType.EUROPEAN:
                return EuropeanParrot()
            case ParrotType.AFRICAN:
                return AfricanParrot(number_of_coconuts)
            case ParrotType.NORWEGIAN_BLUE:
                return NorwegianBlueParrot(voltage, nailed)
            case _:
                raise ValueError("Invalid parrot type")


    def speed(self):
        parrot = self._create(self._type, self._number_of_coconuts, self._voltage, self._nailed)
        return parrot.speed()

    def cry(self):
        match self._type:
            case ParrotType.EUROPEAN:
                parrot = EuropeanParrot()
                return parrot.cry()
            case ParrotType.AFRICAN:
                parrot = AfricanParrot(self._number_of_coconuts)
                return parrot.cry()
            case ParrotType.NORWEGIAN_BLUE:
                parrot = NorwegianBlueParrot(self._voltage, self._nailed)
                return parrot.cry()