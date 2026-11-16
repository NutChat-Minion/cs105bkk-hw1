class MenuItem:
    """A dish on a restaurant's menu. The price is a whole number of baht."""

    def __init__(self, name: str, price: int):
        """Store the name and the price."""
        self.name = name
        self.price = price

    @property
    def price(self) -> int:
        """The price in baht."""
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        """Set the price and check that it is more than 0."""
        if value <= 0:
            raise ValueError(
                f"price must be more than 0 baht, got {value}"
            )
        self._price = value

    def __repr__(self) -> str:
        """Return the developer view."""
        return f"{type(self).__name__}({self.name!r}, {self.price})"

    def __eq__(self, other: object) -> bool:
        """Compare two menu items."""
        if not isinstance(other, MenuItem):
            return NotImplemented

        return self.name == other.name and self.price == other.price

    def cost(self, quantity: int) -> int:
        """What quantity of this dish costs."""
        return self.price * quantity


class PromoItem(MenuItem):
    """A dish on a buy 2, get 1 free promotion."""

    def cost(self, quantity: int) -> int:
        """Every third item is free."""
        free_items = quantity // 3
        paid_items = quantity - free_items

        return super().cost(paid_items)


class Order:
    """One customer's delivery order."""

    delivery_fee = 30
    free_delivery_from = 300

    def __init__(
        self,
        customer: str,
        lines: list[tuple[MenuItem, int]] | None = None
    ):
        """Store customer and make a separate list of lines."""
        self.customer = customer
        self.lines = list(lines) if lines is not None else []

    def add(self, item: MenuItem, quantity: int = 1) -> None:
        """Add an item to the order."""
        if quantity < 1:
            raise ValueError(
                f"quantity must be at least 1, got {quantity}"
            )

        self.lines.append((item, quantity))

    def total(self) -> int:
        """Calculate food cost and delivery fee."""
        food_cost = sum(
            item.cost(quantity)
            for item, quantity in self.lines
        )

        if not self.lines:
            return 0

        if food_cost >= self.free_delivery_from:
            return food_cost

        return food_cost + self.delivery_fee

    def summary(self) -> list[str]:
        """Return one summary line per order line."""
        return [
            f"{quantity} x {item.name}"
            for item, quantity in self.lines
        ]


def cheapest(options: list) -> object | None:
    """Return the option with the smallest total()."""
    if not options:
        return None

    return min(options, key=lambda option: option.total())
