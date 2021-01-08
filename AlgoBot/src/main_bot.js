// requires discord.js
const { ifError } = require('assert')
const Discord = require('discord.js')
const {token, prefix} = require('../config.json')

// client
const client = new Discord.Client()

client.on('ready', () => {
    console.log("AlgoDS is activated: " + client.user.tag)
})

// help message 
client.on('message', message => {if(message.content === `${prefix}help`){message.channel.send(
    `AlgoDS is a bot made to easily access common implementations of Algorithms, programming languages and more.`
)}})

// random response game

let choose_options_8ball = new Map([
    [1, 'lol no.'],
    [2, 'Do you even have to ask?'],
    [3, 'Ask again...'],
    [4, 'Maybe another day...'],
    [5, `It seems like you're having a bad day... the answer is NO.`],
    [6, `Of course!`]
])


client.on('message', message => {
    if(message.content ===`${prefix}8ball`){
        let random_number = Math.floor(Math.random()*choose_options_8ball.size)
        if(random_number != 0){
            message.channel.send(guess.get(random_number))
        }else{
            message.channel.send(guess.get(3))
        }
    }
})




//logins in as the client for algobot
client.login(token)