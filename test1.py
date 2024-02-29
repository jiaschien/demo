import sys

test = []
test_1 = [1]

print(sys.getsizeof(test))
print(sys.getsizeof(test_1) - sys.getsizeof(test))


