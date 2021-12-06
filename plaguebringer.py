import discord
import sqlite3
import random
import time
from math import ceil



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



class Pidor(discord.Client):
    def prefix(self):
        with open('p.txt', 'r') as f:
            self.p = ''.join(f.read())
        print('{0} - это мой префикс'.format(self.p))
    def change_prefix(self, new_prefix):
        with open('p.txt', 'w') as f:
            f.write(new_prefix)
        self.prefix()
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
        self.prefix()


    async def on_message(self, msg):
        if msg.author == client.user:
            return
        if msg.content.startswith(f'{self.p}prefix') and msg.author.server_permissions.administrator:
            p = msg.content.split()[1]
            self.change_prefix(p)
            await msg.channel.send('мой префикс теперь '+self.p)
        if msg.content == f'{self.p}ping' and msg.author.name == 'ZeNik77':
            self.change_ping(1)
            await msg.channel.send('текущий пинг: '+'\\'+self.ping)
        if msg.content == 'PLAGUE BARRAGE' and msg.author.name == 'ZeNik77':
            await msg.channel.send(f'{self.ping} PLAGUE NUKE BARRAGE ARMED, PREPARING FOR LAUNCH!!!')
            time.sleep(10)
            for i in range(40):
                await msg.channel.send(f'{self.ping} https://tenor.com/view/floppa-gif-22427240')
        if 'ROCKET BARRAGE' in msg.content and msg.author.name == 'ZeNik77':
            s = ['https://tenor.com/view/ukraine-flags-waving-gif-16757086', 'https://tenor.com/view/%D1%83%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0%D1%83%D0%B2%D1%80%D0%BE%D0%BF%D0%B0-%D1%83%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0-%D0%B5%D0%B2%D1%80%D0%BE%D0%BF%D0%B0-%D1%84%D0%BB%D0%B0%D0%B3-stars-gif-16830672', 'https://tenor.com/view/%D1%81%D0%BB%D0%B0%D0%B2%D0%B0-%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%96-%D0%BF%D1%80%D0%B0%D0%BF%D0%BE%D1%80-%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8-%D0%B6%D0%BE%D0%B2%D1%82%D0%BE-gif-20238850', 'https://tenor.com/view/%D0%BB%D1%8E%D0%B1%D0%BB%D1%8E-%D0%BA%D0%BE%D1%85%D0%B0%D1%8E-%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%83-%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0-%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B0-gif-20239168', 'https://tenor.com/view/ukrayna-ukraine-flag-ukraine-gif-23460766', 'https://tenor.com/view/ukraine-flag-ukraine-flag-flag-ukraine-ukraine-map-gif-14339705', 'https://tenor.com/view/%D0%BB%D1%8E%D0%B1%D0%BB%D1%8E-%D0%BA%D0%BE%D1%85%D0%B0%D1%8E-%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%83-%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0-%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D1%8E-gif-20239179']
            await msg.channel.send(f'{self.ping} СКОРО НАЧНЕТСЯ \nУКРАИНСКАЯ БОМБАРДИРОВКА')
            time.sleep(10)
            for i in range(int(msg.content.split()[2])):
                await msg.channel.send(f'{self.ping} {random.choice(s)}')
        if msg.content == 'ХОХЛЯЦКИЙ ТОРНАДО' and msg.author.name == 'ZeNik77':
            await msg.channel.send(f'{self.ping} ВНИМАНИЕ ВНИМАНИЕ НАБЛЮДАЕТСЯ УХУДШЕНИЕ ПОГОДЫ ЧЕРЕЗ:')
            a = 10
            aa = a
            for i in range(aa):
                await msg.channel.send(a)
                a -= 1
                time.sleep(1)
            for i in range(40):
                await msg.channel.send(f'{self.ping} https://tenor.com/view/deff-mishe4ka-gterra-piw-taverna-deffa-gif-23635777')
        if msg.content.startswith(f'БОТ ПОМОГИ') and msg.author.name == 'ZeNik77':
            await msg.channel.send('ВЫПОЛНЯЮ ОТВЛЕКАЮЩИЙ МАНЕВР....')
            time.sleep(5)
            await msg.channel.purge(limit=95000)
            await msg.channel.send('https://media.discordapp.net/attachments/545332087066984449/556391853927301120/50177967_336332557215711_1147320476410839040_n.gif')
            await msg.channel.send(
                'https://media.discordapp.net/attachments/545332087066984449/556391853927301120/50177967_336332557215711_1147320476410839040_n.gif')
            await msg.channel.send(
                'https://media.discordapp.net/attachments/545332087066984449/556391853927301120/50177967_336332557215711_1147320476410839040_n.gif')
            await msg.channel.send(
                'https://media.discordapp.net/attachments/545332087066984449/556391853927301120/50177967_336332557215711_1147320476410839040_n.gif')
            await msg.channel.send(
                'https://media.discordapp.net/attachments/545332087066984449/556391853927301120/50177967_336332557215711_1147320476410839040_n.gif')
            await msg.channel.send(
                'https://media.discordapp.net/attachments/545332087066984449/556391853927301120/50177967_336332557215711_1147320476410839040_n.gif')
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

        if msg.content.startswith(f'{self.p}clean') and msg.author.name == 'ZeNik77':
            time.sleep(3)
            a = int(msg.content.split()[1])
            await msg.channel.purge(limit=a)
        if msg.content.startswith(f'{self.p}trueclean') and msg.author.name == 'ZeNik77':
            time.sleep(5)
            await msg.channel.purge(limit=40)
        if msg.content.startswith(f'{self.p}truetrueclean') and msg.author.name == 'ZeNik77':
            time.sleep(5)
            await msg.channel.purge(limit=95000)


client = Pidor()
client.change_ping(0)
client.run('')
