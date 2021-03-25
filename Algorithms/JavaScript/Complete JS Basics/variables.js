// Using var vs. let
// Var is outdated and can cause bugs within the scope of a function.

/* - - - */

// Example 1:

console.log('Example 1')

/* - - - */

var number = 10

for(i =0; i < 1; i++){
    number = 11
    console.log('redefined num:' + number)
}

console.log('After loop: '+number)

// Num remains the same, which makes sense. However, if we want a variable to only work in a scope: {}
// Then we would want it to not change afterwards

/* - - - */

let number_let = 11;

console.log('Before change:' + number_let)

for(j = 0; j < 1; j ++){
    let number_let = 12 
    console.log('In the loop:' + number_let)
}

console.log('After Loop:' + number_let)

console.log(' ')

// Note: in likne 27, if we just asigned number_let = 12 without the 
// keyword 'let' then it would update the variables (similar to var)
// However, we want to only update in the scope, so we would just 
// include the 'let' keyword

// Furthermore, they are both treated as different variables since they're in different scopes

// Example 2: Error Causing, uncomment line 45 to see the difference 
console.log('Example 2')

let error = 'this is not going to work' 
// let error = 'it still will not'
console.log(' ')

// Example 3:
console.log('Example 3')

let string = 'Hey There :)'
string = 'This is changed but still, hi'
console.log(string)

/* --- */

// Example 4 
console.log('Example 4')
let changed_string = 'using JS'
let changed_string_two = 'using TS'
let both = changed_string + ' ' + changed_string_two
console.log(both)

// Example 5
console.log('Example 5')

let array_string = 'Hello'
let array_one = array_string[array_string.length-3]
console.log(array_one)

// Example 6: Spaces counting as cells in the string or arrays
console.log('Example 6')
let array_spaced = 'Hey there!'
let array_two = array_spaced[array_spaced.length-7]
console.log(array_two)
let array_length = array_spaced.length
console.log(array_length)