from statistics import mean, median, mode


class FirstClass:
    mean = 0
    median = 0
    mode = 0

    def __init__(self, data):
        self.data = data

    @staticmethod
    def calc_mean(data):
        FirstClass.mean = mean(data)

    @classmethod
    def calc_median(cls, data):
        cls.median = median(data)

    def calc_mode(self):
        self.mode = mode(self.data)

    def results(self):
        return self.mean, self.median, self.mode


test = FirstClass([1, 2, 3, 3, 4, 4, 4, 5])

test.calc_mode()
test.calc_mean([1, 2, 3, 4, 5, 6])
FirstClass.calc_median([1, 2, 3, 4, 5, 6])

print(test.results())
