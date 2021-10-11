#Lst = Array sorted, item = item to find
#This algorithm needs a sorted array
def BinarySearch(lst, item):
    low = 0; #Low number
    high = len(lst)-1; #Maximum number
    while low <= high:
        mid = (high + low); #Check the middle element
        guess = lst[mid];
        if guess == item:
            return mid; #Item founded
        if guess > item: #To high
            high = mid - 1;
        else: #Too low
            low = mid + 1;
    return None;

def findSmallest(arr):
        smallest = arr[0];
        smallest_index = 0;
        for i in range(1, len(arr)):
            if arr[i] < arr[smallest_index]:
                smallest_index = i;
                smallest = arr[i];
        return smallest_index;

def selectionSort(arr):
    new_arr = [];
    for i in range(len(arr)):
        smallest = findSmallest(arr);
        new_arr.append(arr.pop(smallest));
    return new_arr;

def countdown(n):
    print(n);
    if n <= 0:
        return 0;
    else:
        return countdown(n-1);

def factorial(n):
    if n == 1:
        return 1;
    else:
        return n * factorial(n - 1);

def quicksort(arr):
    if len(arr) < 2:
        return arr;
    else:
        pivot = arr[0]; #Tomamos como pivote el primer elemento, este puede ser cualquier elemento del array
        less = [i for i in arr[1:] if i <= pivot];
        greater = [i for i in arr [1:] if i > pivot ];

        return quicksort(less) + [pivot] + quicksort(greater);


if __name__ == '__main__':
    my_list = [1,3,5,7,9];
    print(BinarySearch(my_list, 9));
    print(selectionSort([7,1,5,2,10,4,22,18]));
    print(countdown(10));
    print(factorial(5));
    print(quicksort([9,5,1,7,3,9,2,10,23,75,132,75,23]));