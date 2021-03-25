// Example 1: Pushing information to an array 
console.log('Example 1:')
let array = ['food', 'is', 'good']
array.push('yes it is ')
console.table(array)
console.log('\n')

//Example 2: Popping information, removes last element of an array
console.log('Example 2:')
array.pop(array[3])
console.table(array)
console.log('\n')

//Example 3: Shifting with Arrays, removes the first element in an array
console.log('Example 3:')
array.shift(array[0])
console.table(array)
console.log('\n')

// Example 4: Unshifting: adding elements to the front of the array
console.log('Example 4:')
array.unshift("Food (again)")
console.table(array)
console.log('\n')

// Example 5: Creating a 2D array of gym equipment
console.log('Example 5:')
let gym_equipment = [
    ['Dumbells', 20],
    ['Racks', 0],
    ['Barbells', 10],
    ['Benches', 4]
]
console.table(gym_equipment)
for(rows = 0; rows < gym_equipment.length; rows++){
    var arr = gym_equipment[rows].length
    for(columns = 0; columns < arr; columns++){
        console.log('[' + rows + ',' + columns + '] =' + gym_equipment[rows][columns])
    }

}