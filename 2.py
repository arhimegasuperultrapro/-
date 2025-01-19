def nums(num_lst:list):
    common = None
    for num in num_lst:
        own = [[x, num // x] for x in range(2, int(num**0.5)+1) if num % x == 0]
        new_own = []
        for x in own:
            for i in x:
                new_own.append(i)
        new_own.append(num)
        new_own = set(new_own)
        if common == None:
            common = new_own
        else:
            common = common & new_own

    return list(common)

print(nums([42, 12, 18]))
print(nums([14, 42]))
print(nums([14, 42, 7]))
print(nums([3, 6, 9, 18, 333]))



