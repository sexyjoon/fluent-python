class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    sereies = []

    def averager(new_value):
        sereies.append(new_value)
        total = sum(sereies)
        return total / len(sereies)

    return averager


def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager

if __name__ == '__main__':
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    avg = make_averager2()
    print(avg(10))
    print(avg(11))
    print(avg(12))