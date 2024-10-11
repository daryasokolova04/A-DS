def step_count(k):
    if k == 1:
        return 1
    elif k == 2:
        return 2
    elif k == 3:
        return 4
    else:
        return step_count(k-3) + step_count(k-2) + step_count(k-1)


n = int(input())
print(step_count(n))
