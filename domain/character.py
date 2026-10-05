from abc import ABC, abstractmethod
from domain.inventory import Inventory
from domain.exceptions import DeadCharacterError

class Character(ABC):
    def __init__(self, name: str, health: int, attack_power: int,defense: int = 0):
        self.name = name
        self._health = health
        self.__max_health = health
        self.attack_power = attack_power
        self.inventory = Inventory()
        self.defense = defense

    @property
    def health(self) -> int:
        return self._health

    @property
    def isalive(self) -> bool:
        return self._health > 0

    def take_damage(self, amount: int ) -> None:
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")
        self._health  = max(self._health - amount, 0)

    def attack(self, target: "Character") -> None:
        if not self.isalive:
            raise DeadCharacterError(f"{self.name} is dead and cannot act")
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")

    def heal(self, amount: int) -> int:
        self._health = min(self._health + amount ,self.__max_health)
        return self._health

    @abstractmethod
    def special_ability(self, target: "Character") -> None:
        raise NotImplementedError("every concrete must define its own move")