import random
import numpy as np
import time
import matplotlib.pyplot as plt


def Merge(Arr, left, mid, right):
    nl = mid - left + 1
    nr = right - mid
    left_arr = []
    right_arr = []
    for i in range(nl):
        left_arr.append(Arr[left + i])

    for j in range(nr):
        right_arr.append(Arr[mid + 1 + j])
    i = 0
    k = left
    j = 0
    while i < nl and j < nr:
        if left_arr[i] <= right_arr[j]:
            Arr[k] = left_arr[i]
            i = i + 1
            k = k + 1
        else:
            Arr[k] = right_arr[j]
            j = j + 1
            k = k + 1
    while i < nl:
        Arr[k] = left_arr[i]
        i = i + 1
        k = k + 1
    while j < nr:
        Arr[k] = right_arr[j]
        j = j + 1
        k = k + 1


def Merge_sort(Arr, first, last):
    if first < last:
        mid = (first + last) / 2
        Merge_sort(Arr, first, int(mid))
        Merge_sort(Arr, int(mid) + 1, last)
        Merge(Arr, first, int(mid), last)


def partition(Arr, first, last):
    pivot = Arr[last]
    i = first - 1
    for j in range(first, last):
        if Arr[j] <= pivot:
            i = i + 1
            Arr[i], Arr[j] = Arr[j], Arr[i]
    Arr[i + 1], Arr[last] = Arr[last], Arr[i + 1]
    return i + 1


def randomized_partition(Arr, first, last):
    i = random.randint(first, last)
    Arr[i], Arr[last] = Arr[last], Arr[i]
    return partition(Arr, first, last)


def randomized_quick_sort(Arr, first, last):
    if first < last:
        pivot = randomized_partition(Arr, first, last)
        randomized_quick_sort(Arr, first, pivot - 1)
        randomized_quick_sort(Arr, pivot + 1, last)


# n : length of array
def selection_sort(Arr, n):
    for i in range(n - 1):
        I_min = i
        for j in range(i + 1, n):
            if Arr[j] < Arr[I_min]:
                I_min = j
        if i != I_min:
            Arr[i], Arr[I_min] = Arr[I_min], Arr[i]


def insertion_sort(Arr, n):
    for i in range(1, n):
        key = Arr[i]
        j = i
        while j > 0 and Arr[j - 1] > key:
            Arr[j] = Arr[j - 1]
            j = j - 1
        Arr[j] = key


def hybrid_sort(Arr, first, last, threshold):  # O(n^2)

    if (last - first + 1) <= threshold:
        selection_sort(Arr, len(Arr))
    else:
        mid = (first + last) / 2
        hybrid_sort(Arr, first, int(mid), threshold)
        hybrid_sort(Arr, int(mid), last, threshold)
        Merge(Arr, first, int(mid), last)


def kth_element(Arr, first, last, k):  # O(n) or O(n^2)
    pivot=partition(Arr,first,last)
    if pivot==k:
        print(Arr[k])
        return Arr[k]
    elif pivot>k:
        kth_element(Arr,first,pivot-1,k)
    else:
        kth_element(Arr,pivot+1,last,k)


if __name__ == '__main__':

    x_axis = []
    y_merge = []
    y_Quick = []
    y_selection = []
    y_insertion = []
    for i in range(5):
        size_arr = input('Enter the size: ')

        Array = np.random.randint(int(size_arr), size=(int(size_arr)))
        Arr_merge = Array.copy()
        Arr_quick = Array.copy()
        Arr_selection = Array.copy()
        Arr_insertion = Array.copy()
        Arr_hybrid = Array.copy()
        Arr_Kth = Array.copy()
        #  print(Arr_merge)
        begin_merge = time.time()
        Merge_sort(Arr_merge, 0, len(Arr_merge) - 1)
        end_merge = time.time()
        time_merge = (end_merge - begin_merge)*1000
        #  print(Arr_merge)
        #  print(Arr_quick)
        begin_quick = time.time()
        randomized_quick_sort(Arr_quick, 0, len(Arr_quick) - 1)
        end_quick = time.time()
        time_quick = (end_quick - begin_quick)*1000
        # print(Arr_quick)
        # print(Arr_selection)
        begin_selection = time.time()
        selection_sort(Arr_selection, len(Arr_selection))
        end_selection = time.time()
        time_selection = (end_selection - begin_selection)*1000
        #  print(Arr_selection)
        #  print(Arr_insertion)
        begin_insertion = time.time()
        insertion_sort(Arr_insertion, len(Arr_insertion))
        end_insertion = time.time()
        time_insertion = (end_insertion - begin_insertion)*1000
        # print(Arr_insertion)
        x_axis.append(size_arr)
        y_merge.append(time_merge)
        y_Quick.append(time_quick)
        y_selection.append(time_selection)
        y_insertion.append(time_insertion)

        # print(Arr_hybrid)
        hybrid_sort(Arr_hybrid, 0, len(Arr_hybrid) - 1, 6)
        #  print(Arr_hybrid)
        # print(Arr_Kth)
        k = input('Enter the kth: ')
        kth = kth_element(Arr_Kth,0,len(Arr_Kth)-1,int(k))
    print(y_merge)
    print(y_Quick)
    print(y_selection)
    print(y_insertion)

    plt.plot(x_axis, y_merge, label="merge")
    plt.plot(x_axis, y_Quick, label="quick")
    plt.plot(x_axis, y_selection, label="selection")
    plt.plot(x_axis, y_insertion, label="insertion")
    plt.legend()
    plt.show()
