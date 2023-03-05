import discord
import sqlite3
import random
import time
import string
from bot_token import TOKEN, TOKENS
import asyncio
import threading


'''
            sum = int(msg.content.split()[1])
            sum1 = sum
            k = int(msg.content.split()[2])
            r = random.randint(1, 100)
            if r<=k:
                k=1/(k/100)
                sum=int(sum*k)
                await msg.channel.send(f'выигрыш = {sum}')
            else:
                await msg.channel.send(f'проигрыш')
'''

target = ''
rockets = []

class Pidor(discord.Client):
    async def on_message(self, msg):
        if msg.author == self.user:
            return
        if msg.author.id == 449139068043788288 and 'YOUR MOM' in msg.content:
            await msg.channel.send(f'{self.ping} Loading image of ur mom.....')
            time.sleep(5)
            await msg.channel.send('https://cdn.discordapp.com/attachments/816923139299868682/910326955537207316/image0-1-1-1.png')
            await msg.channel.send('https://cdn.discordapp.com/attachments/816923139299868682/910326970468958308/image0-3-1-1.png')
            await msg.channel.send('https://cdn.discordapp.com/attachments/816923139299868682/910326986218565692/image0-4-1-2.png')
            await msg.channel.send('https://cdn.discordapp.com/attachments/816923139299868682/910326999397040138/image0-5-1.png')
            await msg.channel.send('https://cdn.discordapp.com/attachments/816923139299868682/910327003331325972/image0-6-1-1.png')
                
        if msg.author.id == 449139068043788288 and 'ПОСЛАТЬ НАЗУЙ' in msg.content:
            user = await self.fetch_user('649223035940896788')
            for i in range(100):
                await user.send("ВЫ РАЗГНЕВАЛИ БОГОВ")
                time.sleep(2)
        if msg.author.id == 449139068043788288 and 'розвiдка' in msg.content:
            print('руку')
            for guild in self.guilds:
                for member in guild.members:
                    await msg.channel.send(member)
            await msg.channel.send('мой префикс теперь '+self.p)
        if msg.content == f'-ping' and msg.author.id == 449139068043788288:
            self.change_ping(1)
            await msg.channel.send('текущий пинг: '+'\\'+self.ping)
        if msg.content.startswith('PLAGUE BARRAGE'):
            await msg.channel.send(f'{self.ping} https://tenor.com/view/mother-fat-yo-mama-explode-explosion-gif-22515407')
            time.sleep(10)
            for i in range(40):
                await msg.channel.send(f'{self.ping} https://tenor.com/view/mother-your-your-mother-kurzgesagt-explosion-gif-25748504')
        if 'ROCKET BARRAGE' in msg.content:
            s = ['https://tenor.com/view/ukraine-ukraine-flag-heart-ninisjgufi-gif-25003148', 'https://tenor.com/view/ukrayna-ukraine-flag-ukraine-gif-23460766', 'https://tenor.com/view/%D1%83%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0%D1%83%D0%B2%D1%80%D0%BE%D0%BF%D0%B0-%D1%83%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0-%D0%B5%D0%B2%D1%80%D0%BE%D0%BF%D0%B0-%D1%84%D0%BB%D0%B0%D0%B3-stars-gif-16830672', 'https://tenor.com/view/ukraine-flag-ukraine-flag-flag-ukraine-ukraine-map-gif-14339705', 'https://tenor.com/view/ukraine-flag-heart-ninisjgufi-gif-25056038', 'https://tenor.com/view/ukraine-ninisjgufi-flag-slava-ukraini-hearts-gif-25161687']
            await msg.channel.send(f'{self.ping} СКОРО НАЧНЕТСЯ \nУКРАИНСКАЯ БОМБАРДИРОВКА')
            time.sleep(10)
            for i in range(int(msg.content.split()[2])):
                await msg.channel.send(f'{self.ping} {random.choice(s)}')
        if msg.content == 'БОТ УМРИ' and msg.author.id == 449139068043788288:
            await msg.channel.send(msg.author.mention+' ЦЕЛИ УНИЧТОЖЕНЫ. ВОЗВРАЩАЮСЬ НА ДОМАШНЮЮ СТАНЦИЮ')
            exit(0)
        if msg.content == 'ХОХЛЯЦКИЙ ТОРНАДО':
            await msg.channel.send(f'{self.ping} ВНИМАНИЕ ВНИМАНИЕ НАБЛЮДАЕТСЯ УХУДШЕНИЕ ПОГОДЫ ЧЕРЕЗ:')
            a = 10
            aa = a
            for i in range(aa):
                await msg.channel.send(a)
                a -= 1
                time.sleep(1)
            for i in range(40):
                await msg.channel.send(f'{self.ping} https://tenor.com/view/deff-mishe4ka-gterra-piw-taverna-deffa-gif-23635777')
        if msg.content.startswith('БОТ ПОМОГИ') and msg.author.id == 449139068043788288:
            await msg.channel.send(msg.author.mention+' ВЫПОЛНЯЮ ОТВЛЕКАЮЩИЙ МАНЕВР....')
            time.sleep(5)
            await msg.channel.purge(limit=95000)
            for i in range(5):
                await msg.channel.send('https://tenor.com/view/epilepsi-patates-pattes-denemepattes-gif-13248094')
        if msg.content == 'ВСЕМ ПИЦЦЫ ЗА МОЙ СЧЕТ':
            self.pizza = True
            await msg.channel.send('НАЧИНАЮ РАЗДАЧУ ПИТСЫ')
        if msg.content == 'ХАЧУ ПИТСЫ' and self.pizza == True:
            await msg.channel.send(f'{msg.author.mention} ДЕРЖИ ПИТСУ\nhttps://media.discordapp.net/attachments/786305593765396481/903157505650204712/image0-2.gif')
        elif msg.content == 'ХАЧУ ПИТСЫ' and self.pizza == False:
            await msg.channel.send('нет кого-то кто бы раздавал питсу')
        if msg.content == 'хватит питсу':
            self.pizza = False
            await msg.channel.send('питса кончилась')
        if 'zt!ship' in msg.content:
            await msg.channel.send('НАЧИНАЮ УНИЧТОЖЕНИЕ ШИППЕРА...')
            time.sleep(7)
            for i in range(5):
                await msg.channel.send('https://tenor.com/view/epilepsi-patates-pattes-denemepattes-gif-13248094')
        if msg.content.startswith(f'-clean') and msg.author.id == 449139068043788288:
            time.sleep(3)
            a = int(msg.content.split()[1])
            await msg.channel.purge(limit=a)
        if msg.content.startswith(f'-trueclean') and msg.author.id == 449139068043788288:
            time.sleep(5)
            await msg.channel.purge(limit=40)
        if msg.content.startswith(f'-truetrueclean') and msg.author.id == 449139068043788288:
            time.sleep(5)
            await msg.channel.purge(limit=95000)
        if msg.content.startswith('PLAGUE NUKE BARRAGE') and msg.author.id == 449139068043788288:
            global target
            #target = await self.fetch_user('1081651423009325157')
            for i in range(len(TOKENS)):
                threading.Thread(target=self.run_loop, args=[TOKENS[i]]).start()
                #asyncio.create_task(self.send_rocket(TOKENS[i]))
            await asyncio.sleep(6)
            await msg.channel.send(msg.author.mention+' PLAGUE NUKE BARRAGE ARMED. PREPARING FOR LAUNCH')
        if msg.content.lower() == 'отставить' and msg.author.id == 449139068043788288:
            await asyncio.sleep(3)
            await msg.channel.send(msg.author.mention+' Ракеты успешно вернулись в на базу')


    def run_loop(self, token):
        asyncio.set_event_loop(asyncio.new_event_loop())
        asyncio.get_event_loop().run_until_complete(self.send_rocket(token))

    
    def send_rocket(self, token):
        bot = Rocket(intents=intents)
        global rockets
        rockets.append(bot)
        bot.run(token)

    def change_ping(self, id):
        if id == 0:
            with open('ping.txt', 'r') as f:
                self.ping = ''.join(f.read())
            self.pizza = False
        elif id == 1:
            with open('ping.txt', 'w') as f:
                if self.ping == '':
                    self.ping = '@everyone'
                    f.write('@everyone')
                else:
                    self.ping = ''
        print('текущий пинг:', self.ping)

    async def on_ready(self):
        print(f'logged as {self.user}')
        self.ping = open('ping.txt', 'r').read()
        
flag_rockets = False
rocket_channel = ''
class Rocket(discord.Client):
    async def on_ready(self):
        #self.user = await self.fetch_user('1081651423009325157')
        print('ракета на месте')
        #self.user = await self.get_user('1081651423009325157')
        #self.user = await self.user.create_dm()

    async def on_message(self, msg):
        global flag_rockets
        global rocket_channel
        with open('ping.txt', 'r') as f:
            p = f.read()
        #await message.channel.send('здарова')
        if msg.content == 'LAUNCH' and msg.author.id == 449139068043788288:
            #await target.send(random.choice(['БУМ', 'БАМ', 'БАХ', 'БАБАХ']))
            #await self.close()
            flag_rockets = True
            rocket_channel = msg.channel
            await rocket_channel.send(p+' '+random.choice(['БУМ', 'БАМ', 'БАХ', 'БАБАХ']))
        if (msg.content == 'отставить' or msg.content == 'ОТСТАВИТЬ') and msg.author.id == 449139068043788288:
            print("отставляем")
            flag_rockets = False
            await self.close()
            return
        if flag_rockets:
            await rocket_channel.send(p+' '+random.choice(['БУМ', 'БАМ', 'БАХ', 'БАБАХ']))


intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = Pidor(intents=intents)
client.run(TOKEN)
