import discord
import asyncio
from bot_token import token_8

class Bot(discord.Client):
    async def on_ready(self):
        channel_id = 1082793741259112541
        channel = await client.fetch_channel(channel_id)
        await channel.send('Здарова это на 8 марта короче и надо пройти дофига недоквест. Всем удачи')
        await asyncio.sleep(0.5)
        await channel.send('https://tenor.com/view/vergil-chair-dmc-yamato-gif-21401933')
        await asyncio.sleep(3)
        await channel.send('Начнем?')
        await channel.send(':pig2:')
        self.flag_answer = 0
        self.answers = ['да', '84', '1', 'osowiec', 'г', 'а', 'спасибо']

    async def on_message(self, msg):
        if msg.author == self.user:
            return

        if msg.content.lower() == self.answers[self.flag_answer] or (msg.author.id == 449139068043788288 and msg.content == 'правильно'):
            self.flag_answer += 1
        elif self.flag_answer == 0 and msg.content.lower() == 'нет':
            await msg.channel.send('вообще-то обидно')
        else:
            await msg.channel.send('неправильный ответ!!!!')
        if self.flag_answer == 1:
            await msg.channel.send('хорошо, начнем. первый вопрос: \nЮля купила корзину яблок на рынке и разделила ее между своими друзьями. Она отдала каждому другу на 3 яблока больше, чем предыдущему. Если последнему другу досталось 21 яблоко, сколько яблок было в корзине, которую купила Юля?')
        elif self.flag_answer == 2:
            await msg.channel.send('''отлично(отлично что я посчитал правильно). следующий вопрос:\nДопустим, в университете есть программа обучения для талантливых школьников, которая позволяет им поступать в университет на первый курс еще до окончания школы. В этой программе участвуют ученики, которые прошли специальный отборочный тест. Однако, кроме теста, для поступления в программу необходимо выполнить еще одно задание: написать научную статью по предмету, на который ученик хочет поступать в университет. Статья должна быть настолько хорошей, что она будет опубликована в одном из научных журналов. Только после этого ученик может быть допущен к программе обучения. Ученик Арсений прошел отборочный тест и написал научную статью. Его статья была опубликована в журнале, и он был допущен к программе обучения. На каком курсе учится Арсений? (ответ числом)''')
        elif self.flag_answer == 3:
            await msg.channel.send('Юля, \n_______ then, and again\nAttack of the dead hundred men')
        
        elif self.flag_answer == 4:
            await msg.channel.send('Следующий вопрос. Сколько маме пришлось пришлось наворачивать кругов во время ожидания Никиты после хакатона?\nа) 1\nб) 2\nв) 3\nг) многго')
        elif self.flag_answer == 5:
            await msg.channel.send('Далее. \nКто самый любимый мальчик?:point_right::point_left:\nа) Никита')
            await asyncio.sleep(2)
            await msg.channel.send('б) Арсений')
        elif self.flag_answer == 6:
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1082800155557908592/image.png?width=353&height=156')
            await msg.channel.send('Где спасибо?')

        else:
            if self.flag_answer != 0:
                await msg.channel.send('Хорошо. Спасибо за прохождение мини-викторины на 8 марта. Всех поздравляю люблю целую и желаю всего самого наилучшего. Так как я решил совсем понаглеть, то мама короче сама переведи себе на карту деньги.\nпароль от телефона: 7716977961377(юля радуйся)\nот сбера: 16977')
                await asyncio.sleep(1)
                await msg.channel.send('https://tenor.com/view/8%D0%BC%D0%B0%D1%80%D1%82%D0%B0-%D1%80%D0%BE%D0%B7%D1%8B-%D1%81%D1%87%D0%B0%D1%81%D1%82%D1%8C%D1%8F-%D0%BB%D1%8E%D0%B1%D0%B2%D0%B8-%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-gif-16516438')


intents = discord.Intents.all()

client = Bot(intents=intents)
client.run(token_8)
