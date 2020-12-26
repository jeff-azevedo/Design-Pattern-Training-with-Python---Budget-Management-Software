class TaxCalculator(object):

    def Calculate(self, budget, tax):

        calculated_tax = tax.Calculate(budget)

        print(calculated_tax)
