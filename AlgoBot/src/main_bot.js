// requires discord.js
const Discord = require('discord.js')
const {token, prefix} = require('../config.json')

// client
const client = new Discord.Client()

client.on('ready', () => {
    console.log("Connected as " + client.user.tag)
})

client.on('message', message => {
	console.log(message.content);
})

client.on('message', message => 
{
    if(message.content === '!ping'){
        message.channel.send('pongggg')
    }
})

client.on('message', message => {
    if(message.content  === '!beanyyy'){
        message.channel.send('uhhhh')
    }
})

client.on('message', message => {
    if(message.content  === '!Marco' || message.content  === '!marco'){
        message.channel.send('Polo')
    }
})

//logins in as the client for algobot
client.login(token)