// Linear Search, checking each element in an array one by one 

function linear_search(array, target){
    for(let iterator = 0; iterator < array.length; iterator++){
        if(array[iterator] == target){
            return 'found'
        }
        return 'not found'
    }
}

let array = [-1,010101,-100,100]
let target = 20

console.log(linear_search(array, target))

