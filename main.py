#  1 - m
t = (1, 2, 3, 4, 5)
yigindi = sum(t)
print('jami sonlarni yigindisi: ', yigindi)


# 2 - m
numbers = tuple(map(int, input('Son kiriting: ').split()))
print(max(numbers))


# 3 - m
t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)
birlashtirish = tuple(t1 + t2)
print(birlashtirish)


# 4 - m
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
juft_s = tuple(x for x in numbers if x % 2 == 0)
print(juft_s)


# 5 - m
t = (1, 2, 3, 4, 5, 6)
teskari = (t[::-1])
print(teskari)
