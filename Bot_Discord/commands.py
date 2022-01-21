import discord

client = discord.Client()

#Envoi dans un canal la réponse
@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")

#Envoi d'un message sur le canal test_commande après une arrivée sur le serveur.
@client.event
async def on_member_join(member):
    general_channel = client.get_channel(834118319257681950)
    await general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")

@client.event
async def on_message(message):
    general_channel = client.get_channel()
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

# @client.event
# async def on_message(message):
#     general_channel = client.get.channel()
#     if message.content("!pseudo"):
#         await general_channel.send(f"Ton pseudo est  {member.display_name} !")