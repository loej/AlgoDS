// Basic Control flow is almost exact to Java and C
//Example 1: Switch statements
console.log('Example 1:')
let letter = 'a'
switch(letter){
    case 'a':
        console.log('bet')
        break
    case 'b':
        console.log('wrong choice')
        break
}

// Example 2: Setting a default statement (since a switchstatement may not cover all possible scenarios)
console.log('\nExample 2:')
let word = ' '
switch(word){
    case 'best':
        console.log('ok')
        break;
    case 'not best':
        console.log('meh')
        break
    default:
        console.log('it works')
        break
}

// Example 3: Having multiple cases in statements
// let number = 10
console.log('\nExample 3:')
let number = 5
switch(number){
    case 1:
    case 2:
    case 3:
    case 10:
        console.log('You won!')
        break   
    default: 
        console.log('It did not work')
        break
}