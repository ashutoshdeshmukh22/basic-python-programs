def hillValey(A):
    if len(A) < 3:
        return
    p1, p2, p3 = A[:3]
    for p in A[3:]:
        if p == p3:
            continue
        if p1 == p2 or (p1 > p2) == (p2 > p3):
            p1, p2, p3 = p2, p3, p
        elif (p3 > p) == (p2 > p3):
            p3 = p
        else:
            return
        if p1 == p2 or p2 == p3:
            return
        if (p1 < p2) != (p2 > p3):
            return
        return "Valley" if p1 > p2 else "Hill"


def check(A): print(A, hillValey(A))


check([1, 2, 3, 5, 4])
check([5, 4, 1, 2, 3])
check([1, 2, 3, 5, 4, 3, 2, 1])
check([9, 5, 4, -1, -2, 3, 7])
check([1, 1, 1, 1, 1])
check([1, 1])
check([1])
check([1, 2, 3, 5, 5])
check([9, -1, 4, -1, -2, 3])
check([3, 2, 2])
check([3, 2, 2, 4])
check([3, 3, 2])
check([1, 1, 2])
check([1, 1, 2, 1])
check([1, 1, 2, 2, 1])
check([1, 1, 1, 2, 2, 1])
check([2, 2, 2, 1, 2, 2])
