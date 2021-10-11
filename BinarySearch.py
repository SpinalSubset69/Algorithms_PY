def BinarySearch(lst, item):
    low = 0;
    high = len(lst)-1;
    while low <= high:
        mid = (high + low);  # Check the middle element
        guess = lst[mid];
        if guess == item:
            return mid;  # Item founded
        if guess > item:  # To high
            high = mid - 1;
        else:  # Too low
            low = mid + 1;
    return None;

def QuickSort(arr):
    middle = (0 + (len(arr) -1)) / 2;
    if len(arr) < 2:
        return arr;
    else:
        pivot = arr[0];
        less = [i for i in arr[1:] if i <= pivot];
        greater = [i for i in arr[1:] if i > pivot];

        return QuickSort(less) + [pivot] + QuickSort(greater);

if __name__ == "__main__":
    lst = [5,3,7,21,3,5,8,234,7,23,1,5,8,2,4356,8,23,4,1,3,6,612,2,4,6,1,46,8,35,6,9,3,4,12,7];

    new_lst = QuickSort(lst);
    print(QuickSort(lst));

    print(BinarySearch(new_lst, 6));