import discord

TOKEN = 'NzA0MTYzMDY5MTEwMTI0NzE2.XqaQzw.lMbHtc_oiIQn8f_qoKaTo7v6X7c'
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_ready():
    print('Bot ready!')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'test':
        await message.channel.send('テスト完了')
    if message.content == '暇':
        await message.channel.send('暇なら勉強でもしたらどうだい？')
    if message.content == 'ひま':
        await message.channel.send('暇なら勉強でもしたらどうだい？')
    if message.content == '黙れ':
        await message.channel.send('嫌だ')
    if message.content == 'IA、コロナの感染者数が知りたい':
        await message.channel.send('ぼくに聞くより、これ見たほうが正確性があるから\nhttps://www.bing.com/covid/local/japan')
    if client.user in message.mentions:
        reply = f'{message.author.mention} 呼んだ？'
        await message.channel.send(reply)
client.run(TOKEN)