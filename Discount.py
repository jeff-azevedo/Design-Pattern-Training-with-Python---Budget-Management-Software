class Discount_Calculator(object):

    def Calculate(self, budget):
        discount = DiscountFiveItems(
            Discount500Value(
                NoDiscount()
            )
        ).Calculate(budget)

        return discount


class DiscountFiveItems(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def Calculate(self, budget):
        if budget.total_items > 5:
            return budget.value * 0.1
        else:
            return self.__next_discount.Calculate(budget)


class Discount500Value:

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def Calculate(self, budget):
        if budget.value > 500:
            return budget.value * 0.07
        else:
            return self.__next_discount.Calculate(budget)


class NoDiscount(object):
    def Calculate(self, budget):
        return 0
