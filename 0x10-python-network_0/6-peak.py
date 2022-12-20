#!/usr/bin/python3

def peak(arr, low, high, n):
    # Find index of middle element
    mid = low + (high - low) / 2
    mid = int(mid)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid

    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return peak(arr, low, (mid - 1), n)

    else:
        return peak(arr, (mid + 1), high, n)


def find_peak(list_of_integers):
    n = len(list_of_integers)
    if n == 0:
        return None
    else:
        return list_of_integers[peak(list_of_integers, 0, n - 1, n)]