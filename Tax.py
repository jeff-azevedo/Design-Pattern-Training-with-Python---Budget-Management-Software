from abc import ABCMeta, abstractmethod


class ConditionalTaxTemplate(object, metaclass=ABCMeta):

    def Calculate(self, budget):
        if self.should_use_max_tax(budget):
            return self.max_tax(budget)
        else:
            return self.min_tax(budget)

    @abstractmethod
    def should_use_max_tax(self, budget):
        pass

    @abstractmethod
    def max_tax(self, budget):
        pass

    @abstractmethod
    def min_tax(self, budget):
        pass


class ISS(object):
    def Calculate(self, budget):
        return budget.value * 0.1


class ICMS(object):
    def Calculate(self, budget):
        return budget.value * 0.06


class ICPP(ConditionalTaxTemplate):
    def should_use_max_tax(self, budget):
        return budget.value > 500

    def max_tax(self, budget):
        return budget.value * 0.07

    def min_tax(self, budget):
        return budget.value * 0.05


class IKCV(ConditionalTaxTemplate):
    def should_use_max_tax(self, budget):
        return budget.value > 500 and self.__has_item_100_more_valued(budget)

    def max_tax(self, budget):
        return budget.value * 0.1

    def min_tax(self, budget):
        return budget.value * 0.06

    def __has_item_100_more_valued(self, budget):
        for item in budget.get_items():
            if item.value > 100:
                return True
            else:
                return False
