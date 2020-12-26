class ISS(object):
    def Calculate(self, budget):
        return budget.value * 0.1


class ICMS(object):
    def Calculate(self, budget):
        return budget.value * 0.06
