// Example 1: Maps

let map = new Map()
let name = "joel"
let lastname = "memed"
let school = "Rutgers"
map.set('Name',`${name}`)
map.set('Lastname', lastname)
map.set("School", school)
console.log("Here is your name " + map.get('Name'))
console.log(map)

// Using objects as keys
console.log("\n Using Objects as keys: \n")
let person = {
    name: 'person_one',
    age: 2,
    height: 100
}

map.set("student", person)
console.log(map)

let netid = 123
let name_new = "Hey"
let student = {
    "name": `${name_new}`,
    "netid": `${netid}`
}

let schools = new Map([
    ["Rutgers", student],
    ["NYU", student]
]
)

for( let keys of schools.keys()){
    console.log(keys)
}

for(let amount of schools.values()){
    console.log(amount)
}

for(let entries of schools.entries()){
    console.log(entries)
}