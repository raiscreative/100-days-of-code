def highest_even(li):
    evens = []
    for num in li:
        if num % 2 == 0:
            evens.append(num)
    return max(evens)

print(highest_even([10, 2, 3, 4, 8, 11]))