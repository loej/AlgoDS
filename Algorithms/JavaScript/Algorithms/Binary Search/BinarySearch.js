// Binary Searchg in JS: Searching Algorithm that finds a target. Assumed: it is sorted
function binary_search(array, target){
    let left_side = 0
    let right_side = array.length-1

    while(left_side <= right_side){
        let middle = Math.floor((right_side + left_side)/2)

        if(array[middle] == target){
            return 'found' 
        }
        if(array[middle] < target){
            left_side = middle + 1
        }
        if(array[middle] > target){
            right_side = middle - 1
        }

    }
    return 'not found'
}

let array = [1,2,3,4,5,6]
let target = 1000
console.log(binary_search(array,target))
