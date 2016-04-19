from random import randint

unsorted = [randint(1, 10) for i in xrange(randint(1, 10))]

def quicksort(arr):

    if len(arr) > 1:
        p = arr[-1]

        i = 0
        for j in xrange(len(arr) - 1):
            if arr[j] < p:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[-1] = p, arr[i]

        left = quicksort(arr[:i])
        right = quicksort(arr[i+1:])

        return left + [p] + right
    else:
        return arr

print unsorted

print quicksort(unsorted)
