#!/usr/bin/env python3

# class CashRegister:
#   pass
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.transactions = []
        self.discount = discount
        self.items = []

    def add_item(self, item, price, quantity=1):
        for _ in range(quantity):
            self.items.append({"item": item, "price": price})
            self.total += price

    def apply_discount(self, discount):
        if discount > 0 and discount <= 100:
            discount_amount = (discount / 100) * self.total
            self.total -= discount_amount
        else:
            return "Invalid discount percentage"
