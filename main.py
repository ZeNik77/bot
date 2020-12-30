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

        if msg.content.startswith(f'{self.p}balance'):
            a = msg.content.find('[')
            b = msg.content.find(']')
            b = msg.content[a+1:b]
            con = sqlite3.connect("mydatabase.db")
            cur = con.cursor()
            cur.execute('SELECT * FROM balance WHERE name == (?)', (b,))
            rows = cur.fetchall()
            if len(rows) == 0 or rows[0][0]!=b:
                cur.execute('INSERT INTO balance VALUES (?, ?)', (b, 0))
                con.commit()
            cur.execute('SELECT * FROM balance WHERE name == (?)', (b,))
            rows = cur.fetchall()
            await msg.channel.send(f'Баланс чела {rows[0][0]} = {rows[0][1]}')

        if msg.content.startswith(f'{self.p}add') and msg.author.guild_permissions.administrator:
            con = sqlite3.connect("mydatabase.db")
            cur = con.cursor()
            c = msg.content.find('[')
            d = msg.content.find(']')
            a = msg.content[d+1:].replace(' ', '')
            b = msg.content[c+1:d]

            cur.execute('SELECT * FROM balance WHERE name == (?)', (b,))
            rows = cur.fetchall()
            if len(rows) == 0 or rows[0][0]!=b:
                cur.execute('INSERT INTO balance VALUES (?, ?)', (b, 0))
                con.commit()
            cur.execute('SELECT * FROM balance WHERE name == (?)', (b,))
            rows = cur.fetchall()
            current = rows[0][1]
            current = int(float(current))
            cur.execute('UPDATE balance SET balance = (?) WHERE name = (?)', (str(int(current)+int(a)), b))
            con.commit()

        if msg.content.startswith(f'{self.p}minus') and msg.author.guild_permissions.administrator:
            con = sqlite3.connect("mydatabase.db")
            cur = con.cursor()
            c = msg.content.find('[')
            d = msg.content.find(']')
            a = msg.content[d+1:].replace(' ', '')
            b = msg.content[c+1:d]
            cur.execute('SELECT * FROM balance WHERE name == (?)', (b,))
            rows = cur.fetchall()
            if len(rows) == 0 or rows[0][0]!=b:
                cur.execute('INSERT INTO balance VALUES (?, ?)', (b, 0))
                con.commit()
            cur.execute('SELECT * FROM balance WHERE name == (?)', (b,))
            rows = cur.fetchall()
            current = rows[0][1]
            current = int(float(current))
            cur.execute('UPDATE balance SET balance = (?) WHERE name = (?)', (str(int(current)-int(a)), b))
            con.commit()
        #msg.channel.id == 791585670149570571 and

        if msg.channel.id == 791585670149570571 and msg.content.startswith(f'{self.p}bet'):
            try:
                con = sqlite3.connect("mydatabase.db")
                cur = con.cursor()
                author = msg.author.name
                cur.execute('SELECT * FROM balance WHERE name == (?)', (author,))
                rows = cur.fetchall()
                if len(rows) == 0 or rows[0][0]!=author:
                    cur.execute('INSERT INTO balance VALUES (?, ?)', (author, 0))
                    con.commit()
                    await msg.channel.send('Ошибка: недостатачно средств')
                    return
                a = int(msg.content.split()[1])
                k = int(msg.content.split()[2])
                if k-5>=1 and k>=60:
                    k-=5
                if k>80:
                    await msg.channel.send('Ошибка: процент должен быть не больше 80')
                    return
                elif k<1:
                    await msg.channel.send('Ошибка: процент должен быть не меньше 1')
                    return
                cur.execute('SELECT * FROM balance WHERE name == (?)', (author,))
                rows = cur.fetchall()
                bal = int(rows[0][1])
                if bal<a:
                    await msg.channel.send('Ошибка: недостаточно средств')
                    return
                else:
                    r = random.randint(1, 100)
                    if r<=k:
                        k = k/100
                        a*=k
                        a=int(a)
                        await msg.channel.send('Победа!')
                        if bal+a == bal:
                            a+=1
                        cur.execute('UPDATE balance SET balance = (?) WHERE name = (?)', (bal+a, author))
                    else:
                        a=int(a)
                        await msg.channel.send('Поражение!')
                        cur.execute('UPDATE balance SET balance = (?) WHERE name = (?)', (bal-a, author))
                    con.commit()
            except Exception as e:
                print(e)
                await msg.channel.send('Ошибка')

        if msg.content.startswith(f'{self.p}trueclean') and msg.author.name == 'ZeNik77':
            time.sleep(5)
            await msg.channel.purge(limit=100)
        if msg.content.startswith(f'{self.p}clean') and msg.author.name == 'ZeNik77':
            await msg.channel.send('ВЫ МЕНЯ РАЗОЗЛИЛИ')
            time.sleep(5)
            await msg.channel.purge(limit=100)
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
        #msg.channel.id == 791343111020085298

        if msg.channel.id == 791343111020085298 and msg.content.startswith('💎'):
            a = msg.content.count('💎')
            k = 10
            o = a//k*2
            author = msg.author.name
            await msg.channel.send(str(o)+' рублей, '+str(a)+' алмазов')
            con = sqlite3.connect("mydatabase.db")
            cur = con.cursor()
            cur.execute('SELECT * FROM balance WHERE name == (?)', (author,))
            rows = cur.fetchall()
            if len(rows) == 0 or rows[0][0] != author:
                cur.execute('INSERT INTO balance VALUES (?, ?)', (author, 0))
                con.commit()
            cur.execute('SELECT * FROM balance WHERE name == (?)', (author,))
            rows = cur.fetchall()
            current = int(rows[0][1])
            cur.execute('UPDATE balance SET balance = (?) WHERE name = (?)', (str(current+o), author))
            con.commit()
        if msg.channel.id == 791358855031423006 and msg.content.startswith('🍉'):
            a = msg.content.count('🍉')
            k = 3
            o = a//3
            author = msg.author.name
            await msg.channel.send(str(o)+' рублей, '+str(a)+' арбузов')
            con = sqlite3.connect("mydatabase.db")
            cur = con.cursor()
            cur.execute('SELECT * FROM balance WHERE name == (?)', (author,))
            rows = cur.fetchall()
            if len(rows) == 0 or rows[0][0] != author:
                cur.execute('INSERT INTO balance VALUES (?, ?)', (author, 0))
                con.commit()
            cur.execute('SELECT * FROM balance WHERE name == (?)', (author,))
            rows = cur.fetchall()
            current = int(rows[0][1])
            cur.execute('UPDATE balance SET balance = (?) WHERE name = (?)', (str(current+o), author))
            con.commit()


client = Pidor()
client.run('NzkxOTk5NzQwMDk4MjQ4NzE0.X-XVPA.5HBTHaQVVEeK8V4yHpxNVnYZQ5I')