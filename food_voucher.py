from abc import ABC, abstractmethod

class FoodVoucher(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class PizzaVoucher(FoodVoucher):
    def eat(self):
        print("Here is your food, enjoy!")

    def get_name(self):
        return "Pizza Voucher"


class SushiVoucher(FoodVoucher):
    def eat(self):
        print("Here is your food, enjoy!")

    def get_name(self):
        return "Sushi Voucher"
