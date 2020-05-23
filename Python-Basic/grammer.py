tupletest = (1,2,4,5)
print(len(tupletest))

listtest = [1,9,4,32,12]
if len(listtest) > 1:
    print("listtest len is " + str(len(listtest)))
elif len(listtest) == 5:
    print("listtest len is 5")

for i in listtest:
    print(i)

for index in range(2,12,2):
    print(index)

def say_hello(name = "blue210"):
    print("hi!" + name)

say_hello("seqman")

is_even = lambda x: x % 2 == 0
print(is_even(2))
print(is_even(3))

def make_double(x):
    return x * 2

maptest = list(map(make_double, [1,2,3]))
print(maptest)

maptest = list(map(lambda x: x % 2 == 0, [1,2,3]))
print(maptest)

filter_test = list(filter(lambda x: x % 2 != 0, [0,1,2,3,4,5]))
print(filter_test)

filter_test2 = list(filter(lambda x: x % 3 == 0, [0,1,2,3,4,5,6]))
print(filter_test2)


print(sorted(["bread", "rice", "spaghetti"], key=lambda x: len(x), reverse=True))

print([x*2 for x in [1,2,3,4]])

print(
    [[x,x+1,x+2] for x in [1,2,3]]
)

print(
    [[0 for x in range(3)] for y in range(4)]
)