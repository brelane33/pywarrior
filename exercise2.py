
'''Sums all elements of a list'''
def newsum(*thelist):
    total = 0
    for i in thelist:
        total += i
    return total

''' Splat operator takes list and turns each element into a single argument'''
print(newsum(10, 20, 30, 40))

