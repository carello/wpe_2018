
class ThresholdEqual(int):
    def __new__(cls, value, threshold=2):
        o = super().__new__(cls, value)
        o.threshold = threshold
        return o

    def __eq__(self, other):
        if abs(self - other) <= self.threshold:
            return True
        else:
            return False

te1 = ThresholdEqual(10)
te2 = ThresholdEqual(6)
print(te1 == te2)

te1 = ThresholdEqual(10)
te2 = ThresholdEqual(9)
print(te1 == te2)

print(te1 + te2)
print(te1 * te2)


te1 = ThresholdEqual(10, 100)
te2 = ThresholdEqual(1)
print(te1 == te2)
