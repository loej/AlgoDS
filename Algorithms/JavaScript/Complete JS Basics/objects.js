//Example 1, making objects
console.log('Example 1:')

let Joel = {
    'name': 'joel',
    'legs': 4
};

let Cat = {
    'name': 100,
    'paws': 4
};
// Dot notation
let instance  = Cat.name
console.log(instance)
// bracket notation
let other_instance = Joel['legs']
console.log(other_instance)
console.log(other_instance + 10)

//Example 2: Updating properties of an object
console.log('\nExample 2:')
let Party = {
    'People': 100,
    'Cakes': 1,
    'Not Invited': 2
};
console.log('Cakes:' + Party.Cakes)
Party.Cakes = 100
console.log('Cakes:' + Party.Cakes)
