// Example 1: Declaring and reversing an array
console.log("Example 1: \n")

let example_one = ['food', 'music', 'train']
for(iterator  = 0; iterator < 3; iterator ++){
    console.log(example_one[iterator])
}
console.log('\n')
console.log('reversed:')

//reversing 
let reversed = []
for(iterator = example_one.length-1; iterator >= 0; iterator--){
    reversed[iterator] = example_one[iterator]
    console.log(reversed[iterator])
}

console.log('Example 2: \n')
// Example 2: Finding duplicate elements in an array
let duplicate_array = [1,2,3,4,5,5,6]
let counter = 0

for(pointer = 0; pointer <= duplicate_array.length-1; pointer++){
    for(front = pointer + 1; front <= duplicate_array.length-1; front++){
        if(duplicate_array[pointer] == duplicate_array[front]){
            console.log('found duplicate!')
            counter++
        }
    }
}
console.log(counter)

// Example 3: Printing and manipulating a 2D array
console.log('Example 3: \n')
let array_2D = [
    [1,1,1,0],
    [1,1,0,1]
]

//displays table
console.table(array_2D)

//rows = 4 => 3
// columns = 4 => 3
// lenght = 4-3
for(let rows = 0; rows < array_2D.length; rows++){
    // size of the inner array [the columns ]
    var inner = array_2D[rows].length
    for(let columns = 0; columns < inner; columns++){
        console.log('[' + rows + ',' + columns + '] = ' + array_2D[rows][columns])
    }
}

// Example 4: Finding duplicates in a 2D array
console.log('Example 4: \n')
let duplicated = [
    [1,1,3,4,5],
    [2,2,3,6,0]
]
console.table(duplicated)
let array_counter = 0
// rows
for(let pointer = 0; pointer < duplicated.length; pointer++){
    var inside  = duplicated[pointer].length
    for(let front_cols = 0; front_cols < inside; front_cols++){
        var num = duplicated[pointer][front_cols]
        for(let find_dup = front_cols + 1; find_dup < inside; find_dup++){
            if(num ==  duplicated[find_dup]){
                console.log('Found duplicate! \n' + duplicated[front_cols] + ',' + duplicated[find_dup])
                counter++
            }
        }
    }
}
console.log('Amount of duplicates:\t' +  counter)