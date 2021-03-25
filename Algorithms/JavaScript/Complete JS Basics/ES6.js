// Example 1. of ES6

// Temple literals
const prefix = 'Mr.'
// uses the ` instead of '
let new_name = `${prefix}President`
// console.log(new_name)
// Prints names with all Prefixes
let arr_name = ["President", "Teacher", "Policeman"]

for(let i =0; i < arr_name.length; i ++){
    console.log(`[${prefix + arr_name[i]}]`)
}

// Example 2 . More temple literals 
let password = "abc"
let username = "Discord_Username"
console.log(`Here is your information: 
        ${password}
        ${username}`)

// Example 3. Object decomposition 
// import { field_one, field_two } from 'blahh'
// const {field_one, field_two} = require('blahh')

// Renaming to different variables 
// const {"field_one": new_field} = require('bruh')

// A bit more about let vs. var
// in this example, the scope is the same, it is not being scoped in to the if statement 
let print = 10

if(print = 10){
    print = print + print + 1
    console.log(`In scope: ${print}`)
}

console.log(`out of scope: ${print}`)