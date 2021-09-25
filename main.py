
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

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
        else: #To low
            low = mid + 1;
    return None;
if __name__ == '__main__':
    my_list = [1,3,5,7,9];
    print(BinarySearch(my_list, 1));