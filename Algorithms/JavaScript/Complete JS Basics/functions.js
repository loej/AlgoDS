// Writing funcitons

//Example 1: A simple function
console.log('Example 1:')
function adding_two_numbers(){
    console.log('jk\n')
}
adding_two_numbers()

//Example 2: Same as above but we're adding conditionals now
console.log('\nExample 2:')
function print_name(name){
    console.log(name)
}

function print_error(){
    console.log('error')
}

input_name = 'Joel'
if(input_name != null){
    print_name(input_name)
}else{
    print_error()
}

// Example 3: passing values to the fucntion 
console.log('\nExample 3:')
let array = [1,2,3,4,5]

function reverse_array(array){

    for(let iterator = 0; iterator < array.length; iterator++){
        console.log(array[iterator])
    }
    console.log('Reversed Array:')
    for(let iterator = array.length-1; iterator >= 0; iterator--){
        console.log(array[iterator])
    }
}

reverse_array(array)

// Example 4: Global Variables and functions 
console.log('\nExample 4:')

let global = 100
function print_global(){
    // Stays reassigned
    global = 200
    console.log(global)
}
print_global()

var global_var = 400
function print_var(){
    oops = 2
    console.log(oops)
}

print_var()

// Example 5: Local Scope with functions 
console.log('\nExample 5:')

function testing_locality(){
    let test = 10
    console.log(test)
}

testing_locality
// The following leads to an error:
// console.log(test)

// Example 6: Using both
console.log('\nExample 6:')

let my_global = 'kek'

function test_both(){
    let my_global = 'bruh'
    console.log('bruh')
}
// local in function
test_both();
// Global 
console.log(my_global)

// Example 7: returning a value 
function life(value){
    return value / 10
}
// prints value returned 
let func_answer = life(10)
console.log(func_answer)

// Example 8: Undefined returning values
console.log('\nExample 8:')

function add_two(num){
    num = num +2
}
let returned = add_two(10)
console.log(returned)
// the funciton doesn't return anything it does not return anything to the function

// Example 9: Implementing a queue FIFO
function queue(array, item){
    array.push(item)
    var item_out = array.shift(item)
    return item_out
}

array = [1,2,3,4,5]
console.log(array)
console.log(queue(array,6))
console.table(array)


