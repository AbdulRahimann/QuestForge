from domain.exceptions import InventoryEmptyError
class Inventory:
    def __init__(self):
        self._items: list = []


    def add(self, item) -> None:
        self._items.append(item)


    def use(self, index: int, target) -> str:
        if not self._items or index < 0 or index >= len(self._items):
            raise InventoryEmptyError("inventory is empty")
        item = self._items.pop(index)
        return item.apply(target)


    def list_items(self) -> list[str]:
        return [type(i).__name__ for i in self._items]