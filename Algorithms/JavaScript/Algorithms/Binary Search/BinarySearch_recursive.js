// Binary Search recusively: we don't need a loop, we can simply call the function recusively
function binarysearch_recusrive(array, target, left, right){
        if (left > right){
            return 'The target is not found'
        }

        let middle = Math.floor((left + right)/2)

        if(array[middle] == target){
            return 'The target: ' + array[middle] + ' is found'
        }else if(array[middle] < target){
            return binarysearch_recusrive(array, target, middle + 1, right)
        }
        else{
            return binarysearch_recusrive(array, target, left, middle - 1)
        }
}

let array = [1,2,3,4,5]
let target = 5
let left = 0
let right = array.length-1
console.log(binarysearch_recusrive(array, target, left, right))