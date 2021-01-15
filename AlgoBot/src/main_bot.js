/* Imports */
const Discord = require('discord.js')
const {token, prefix, status_command} = require('../config.json')
const {Client, MessageEmbed, MessageAttachment} = require('discord.js')
const { stat } = require('fs')

const client = new Discord.Client()

// UserID
const godot_userid = "732169707519475712"
const algoDS_userid = "799061284447846400"

const playing_with = new Map([
    [0,"Algorithms"],
    [1, "Numbers"],
    [2, "Sesh"],
    [3, "Abdul Bari"],
    [4, "code"],
    [5, "Python"],
    [6, "Java"],
    [7,"C++"],
    [8, "JavaScript"]
])

let status = playing_with.get(Math.floor(Math.random()*playing_with.size))

/* For now, all of our funcitons will stay here lol*/

//Activated 
client.on('ready', () => {
    console.log("AlgoDS is activated: " + client.user.tag)
    client.user.setStatus('online')
    client.user.setActivity(`with ${status} | ${status_command}`,{type: "PLAYING"})
})


// 8ball
const choose_options_8ball = new Map([
    [0, `There's a 50/50 chance.`],
    [1, 'lol no.'],
    [2, 'Do you even have to ask?'],
    [3, 'Ask again...'],
    [4, 'Maybe another day...'],
    [5, `It seems like you're having a bad day... the answer is NO.`],
    [6, `Of course!`],
    [7, `If you ask again the odds will be in your favor`],
    [8, `Nah lol. Never happening.`],
    [9, `Nani??? Ask again`],
    [10, `I called them and they said yes.`],
    [11, `That's for sure happening.`]
])

// Message Embed
const about_embed = new Discord.MessageEmbed()
    .setTitle(`AlgoDS`)
    .setColor(0xff0000)
    .setURL(`https://github.com/loej`)
    .setAuthor(`About`)
    .setDescription(
    `AlgoDS is library of useful algorithms. Written in JavaScript, the bot returns code snippets from the following languages:
    ☕ **Java**
    🐍 **Python**
    📚 **C++**
    💻 **JS/TS**
    `)
    .addField(`**Who wrote this?**`,`This bot was written by Joel Martinez, <@${godot_userid}>, an undergrad studying CS at Rutgers University.`)
    .addField(`**It's open source!**`, `You can checkout or contribute to the project [here](https://github.com/loej/AlgoDS)!`)
    .setThumbnail(`https://avatars0.githubusercontent.com/u/48299349?s=400&u=305df58df9c3e16bddb672736122c3f2f01f2601&v=4`)
    .setTimestamp()

    // display avatar
client.on('message', (message) => {
    const args = message.content.slice(prefix.length).trim().split(/ +/)
    const command = args.shift().toLowerCase()
    const tagged_user = message.mentions.users.first()
    
    if(!message.content.startsWith(prefix)||message.author.bot) return;

    if(message.content.startsWith(prefix) && command == `avatar` && args.length){
        const avatar_embed = new Discord.MessageEmbed()
            .setAuthor(`${tagged_user.username}'s avatar`)
            .setImage(tagged_user.displayAvatarURL({format: "png", dynamic: true}))
            .setTimestamp()
        return message.channel.send(avatar_embed)
    }else if(!args.length || !message.author.bot){
        return message.channel.send(`${message.author}, please check your command again.`)
    }
    
})


// 8ball command
client.on('message', (message) => {
    const args = message.content.slice(prefix.length).trim().split(' ')
    const command = args.shift().toLowerCase()

    if(message.content.startsWith(`${prefix}`) && command === `8ball` && args == false){
        message.channel.send(`You **need** to ask a question!`)
    }else if(message.content.startsWith(`${prefix}`) && command === `8ball`){
        let random_quote = choose_options_8ball.get(Math.floor(Math.random()* choose_options_8ball.size))
        message.channel.send(`**Answer: **` + random_quote)
    }
})

// Reacts to specific names, mainly inside jokes
client.on('message', (message) => {
    // Benry 
    if(message.content.match(/beany/i) || message.content.match(/benry/i)){
        message.react('🥩')
    }
    // Joel 
    if(message.content.match(/joel/i) || message.content.match(/boel/i)){
        message.react('💞')
    }
    // Edrick
      if(message.content.match(/Edrick/i) || message.content.match(/yagami/i)){
        message.react('👓')
    }
    // Bames
    if(message.content.match(/bames/i) || message.content.match(/james/i)){
        message.react('🇪🇨')
    }
    // Andres
    if(message.content.match(/andres/i) || message.content.match(/bandres/i)){
        message.react('😂')
    }
    
    if(message.content.match(/AlgoDS/i)){
        message.react('🔎')
    }

})

// Using commands
client.on('message', (message) => {
    // Splitting the commands 
    const args = message.content.slice(prefix.length).trim().split(/ +/)
    const command = args.shift().toLowerCase()
    // !about: Sends embed message of information from the bot
    if(message.content == `${prefix}about`){
        message.channel.send(about_embed)
    }
    // !server: Sends embed message of information of user:
    if(message.content == `${prefix}server`){
        const server_embed = new MessageEmbed()
        .setAuthor(`Where am I?`)
        .setColor(0xff0000)
        .setDescription(`You're in **${message.guild.name}** \n Total Members: **${message.guild.memberCount}**`)
        .setTimestamp()
        message.channel.send(server_embed)
    }
    // !testing <args>: A testing command 
    if(command == `testing` && message.author == godot_userid){
        if(!args.length){
            return message.channel.send(`You need arguments here, ${message.author}!`)
        }
        const find_username = message.mentions.users.first()
        message.channel.send(`Command Name: ${command} \nArguments: ${args}\n`)
        if(!find_username){
            return message.channel.send(`You're not testing usernames`)
        }
        message.channel.send(`You are tagging ${find_username}`)
    }
})

/* logins in as the client for algobot*/
client.login(token)