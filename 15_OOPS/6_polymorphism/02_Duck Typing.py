# Object type doesn’t matter — method existence matters

class UPI:
    def pay(self):
        print("Paid using UPI")

class Card:
    def pay(self):
        print("Paid using Card")

class Cash:
    def pay(self):
        print("Paid using Cash")


def make_payment(method):
    method.pay()


make_payment(UPI())
make_payment(Card())
make_payment(Cash())


# 🔹 Key Insight
# No inheritance used
# Still polymorphism works
# Python checks behavior, not type

