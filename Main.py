from Tax import ISS, ICMS
from Budget import Budget
from TaxCalculator import TaxCalculator

calculator = TaxCalculator()
budget = Budget(500)

calculator.Calculate(budget, ISS())
calculator.Calculate(budget, ICMS())