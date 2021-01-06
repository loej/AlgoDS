#!/usr/bin/python3.8

class Merge:

    def mergesort(self, listToMerge):

        if listToMerge is None or len(listToMerge) < 1:
            return None
        
        if len(listToMerge) > 1:
            middle = len(listToMerge) // 2
            left = listToMerge[:middle]
            right = listToMerge[middle:]

            # recursive call to narrow down the middle 
            mergesort(left)
            mergesort(right)

            # i and u iterate the first two vars, u iterates listToMerge
            i = j = u = 0

            while i < len(left) and j < len(right):
                if left[i] < right[i]:
                    listToMerge[u] = left[i]
                    i += 1 
                else:
                    listToMerge[u] = right[j]
                    j += 1
                u += 1
            #  The remaining values 
            while i < len(left):
                listToMerge[u] = left[i]
                i += 1
                u += 1
            
            while j < len(right):
                listToMerge[u] = right[j]
                j += 1
                u += 1

if __name__=="__main__":
    callMerge = Merge()
    listToMerge = [90,1111,0,2,8]
    callMerge.mergesort(listToMerge)
    print(listToMerge)