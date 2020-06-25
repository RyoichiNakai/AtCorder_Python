
a = int(input())
b = int(input())
print('\n'.join(["%d: Odd" % (a * b) if (a * b) % 2 == 1 else "%d: Even" % (a * b)]))
print("%d: Odd" % (a * b) if (a * b) % 2 == 1 else "%d: Even" % (a * b))
