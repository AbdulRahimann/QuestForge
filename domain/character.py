class Character:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self._health = health
        self.__max_health = health
        self.attack_power = attack_power

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
            return
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")

    def heal(self, amount: int) -> None:
        self._health = min(self._health + amount ,self.__max_health)
        return self._health
