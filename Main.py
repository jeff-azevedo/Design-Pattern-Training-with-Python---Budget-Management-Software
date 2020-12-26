from Tax import ISS, ICMS
from Budget import Budget, Item
from Discount import Discount_Calculator
from TaxCalculator import TaxCalculator

# First Class Alura

# calculator = TaxCalculator()
# budget = Budget(500)
#
# calculator.Calculate(budget, ISS())
# calculator.Calculate(budget, ICMS())

budget = Budget()
budget.add_item(Item('ITEM - 1', 100))
budget.add_item(Item('ITEM - 2', 50))
budget.add_item(Item('ITEM - 3', 500))


calculator = Discount_Calculator()
calculated_discount = calculator.Calculate(budget)

print(f'Calculated discount is :{round(calculated_discount, 2)}')
