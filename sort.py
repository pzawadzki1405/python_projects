#sort min and max

data = [4, 32, 23, 74, 27, 82, 21, 12, 9, 54]

def maximum(numbers):
    max = numbers[0]
    for i in numbers:
        if i>max: max=i
    print('Maximum value of list is ', max)
def minimum(numbers):
    min = numbers[0]
    for i in numbers:
        if i<min: min=i
    print('Minimum value of list is ', min)

def sortowanie(numbers):
    i=0
    pom = 0
    while i < 9:
        if numbers[i+1] > numbers[i]:
            numbers[i+1] = numbers[i]
            numbers[i] = pom
            numbers[i] = pom
        i=i+1
    return numbers


print('Values of the list are')
for i in data:
    print(i)
maximum(data)
minimum(data)
sorted = sortowanie(data)
print('sorted data is ', sorted)
