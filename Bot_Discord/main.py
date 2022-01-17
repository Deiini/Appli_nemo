#Import des ressources
import os
import time
from typing import ValuesView
import discord

client = discord.Client()


#Envoi dans le canal défini par client.get_channel que le bot est prêt
@client.event
async def on_ready():
    general_channel = client.get_channel(834118319257681950)
    await general_channel.send(f"Bonjour, Je suis opérationnel !")

#Envoi dans un canal la réponse
@client.event
async def ping(message):
    general_channel = client.get_channel(834118319257681950)
    if message.content =="Ping":
        await message.channel.send("Pong")
        return;


#Commande Spam de génération de lignes
@client.event
async def spam(message):
       if message.content.startswith("!spam"):
            number = int(message.content.split()[0])
            for number in message:
                message.channel.send
            return;

    
#fonction de suppression de message

@client.event
async def delete(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()
            return (await message.channel.send('les lignes sont supprimées'))
    time.sleep(5)
    number = int(message.content.split()[1])
    messages = await message.channel.history(limit=number + 0).flatten()
    for each_message in messages:
        await each_message.delete()
        print('Message bot supprimé')
        return;
           
#on annonce le pseudo de la personne qui tape !pseudo
@client.event
async def bonjour(message):
    #general_channel = client.get.channel(834118319257681950)
    if message.content =="!pseudo":
        message.channel.send("ton pseudo est " + GetCurrentUser)
        return;
  

client.run("ODA2MTgxOTg0Nzk1MzYxMzIz.YBltew.i1Kbckt8MWBVHTWx0GDvQmJRdXg")

