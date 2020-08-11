#!/usr/bin/python3.8

class Merge:
    
    def mergesort(self, sortedList):
        # If the value is none 
        if sortedList is None or len(sortedList) < 1:
            return print('Please check your list once more.')
        # First edge case, if the right is > 1
        if len(sortedList) > 1:
            # Integer division => 2.5 => 2 | 5.5 => 5
            middle = len(sortedList)//2
            left = sortedList[:middle]
            right = sortedList[middle:]

            mergesort(left)
            mergesort(right)

            # Setting all the values ot 0

            k = i = p = 0

            # We need to copy the sorted data into a temporary list to sort after the data is inserted
            while k < len(sortedList) and i < len(sortedList):
                if left[k] < right[i]:
                    sortedList[p] = left[k]
                    k += 1
                else:
                    sortedList[p] = right[i]
                    i += 1
                p += 1
                

if __name__=="__main__":
    merging = Merge()
    lst = [1, 2, 4, 5]
    merging.mergesort(lst)
    