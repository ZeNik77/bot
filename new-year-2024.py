import discord
import asyncio
from bot_token import token_8

class Bot(discord.Client):
    async def on_ready(self):
        
        channel_id = 1082793741259112541
        test_id = 1190800614779801640
        channel = await client.fetch_channel(channel_id)
        await channel.send('@everyone Всем привет, я снова тут с ботом урааа(немного квест немного итоги года, смотрим)')
        await asyncio.sleep(0.5)
        await channel.send('https://media.discordapp.net/attachments/741945274901200897/1041057132482674719/attachment-1.gif?ex=65a2d682&is=65906182&hm=701f4a2cfe1137f6146355e7b5824427fe73862090283e437b651b635871ce13&')
        await asyncio.sleep(2)
        await channel.send('Начнем?')
        await channel.send(':pig2:')
        self.cat = []
        for i in range(1, 15):
            self.cat.append(f'xd/{i}.jpg')
        self.flag_answer = 0
    async def on_message(self, msg):
        if msg.author == self.user:
            return
        if self.flag_answer == 0 and msg.content != '29 января':
            await msg.channel.send('Начнем. угадайте дату)) (начало года)')
            await asyncio.sleep(1)
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1190784828237434900/1703975612486.jpg?ex=65a30fca&is=65909aca&hm=2191333356772de284fb2f6a72f612ce958a28acd667e6cd72085adff16ab34f&=&format=webp&width=350&height=467')
        elif self.flag_answer == 0 and msg.content == '29 января':
            self.flag_answer += 1
            await msg.channel.send('Какой же кот крутой. Кстати насчет кота))')
            # self.cat = [] # ДЕБАААААГ
            for el in self.cat:
                await msg.channel.send(file=discord.File(el))
                await asyncio.sleep(3)
            await msg.channel.send('Кстати это все самое милое за год, в хронологическом порядке \:)')
            await asyncio.sleep(2)
            await msg.channel.send('МИЛО??')
        elif self.flag_answer == 1 and msg.content.lower() == 'да':
            self.flag_answer += 1
            await msg.channel.send('ООО ЕЩЕ ЕСТЬ')
            await asyncio.sleep(1)
            await msg.channel.send('https://cdn.discordapp.com/attachments/890839770891190282/1162866766968537169/VID_20231004_060117.mp4?ex=65a30292&is=65908d92&hm=8fc5c61a92399825cee38f2931731537d5cf843f737f6dcc9e846cf3897879fc&')
            await msg.channel.send('(теперь и далее пишите "продолжить")')
        elif self.flag_answer == 2 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('https://cdn.discordapp.com/attachments/780868711485669397/1190786039716007956/1703975907354.jpg?ex=65a310eb&is=65909beb&hm=669ec0da6ea9977afb1d51e6e4c7661c0102efd6b2df89cd0b6a063bde197cc9&')
            await msg.channel.send('А куда это мы летим? Ааа, да, в этом году мы в Москве были))')
        elif self.flag_answer == 3 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('...')
            await asyncio.sleep(4)
            await msg.channel.send('https://cdn.discordapp.com/attachments/780868711485669397/1190794419994107994/caf1754bf3b8eec995931dfb14444054.png?ex=65a318b9&is=6590a3b9&hm=15ebb0b304f7e4196c751fad564ad7b5a26dd7597a104bec00975e16968bfcc7&')
            await msg.channel.send('Б О Б И К')
        elif self.flag_answer == 4 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('https://cdn.discordapp.com/attachments/780868711485669397/1190808687766409266/VID-20230830-WA0000.mp4?ex=65a32603&is=6590b103&hm=77d4e6ba6b3a63dc866c50bb5390e9fb7037d8ce8e783e7fb59e6d4bd040fe84&')
            await msg.channel.send('Также вы были на футбольчике!!')
        elif self.flag_answer == 5 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('ТАК, ПЕРЕРЫВ')
            await asyncio.sleep(3)
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1190798791129960498/1.png?ex=65a31ccb&is=6590a7cb&hm=6b82be5b0af2a2707798e230f93d2ca7b54733a43f6ae6f3bc54bb6c598971ba&=&format=webp&quality=lossless&width=284&height=102')
            await msg.channel.send('ЮЮЮЛЯЯЯ')
            await(msg.channel.send('для продолжения скажи никитке ответ'))
        elif self.flag_answer == 6 and msg.author.id == 449139068043788288 and msg.content == 'ВСЕ ВЕРНО':
            self.flag_answer += 1
            await msg.channel.send('Братан харош, давай, давай, вперед. Контент в кайф, можно еще? Вообще красавчик! Можно вот этого вот почаще?')
            await asyncio.sleep(1)
            await msg.channel.send('А теперь небольшая статистика. За год Никита просил маму пополнить проездную 14 раз.\n6 раз сказал спасибо и 4 раза пожалуйста. ДУМАЙТЕ')
        elif self.flag_answer == 7 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('Вот еще))')
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1190789188229025912/IMG_20231231_005056.jpg?ex=65a313da&is=65909eda&hm=3fcee4dee482607f5b2cf907b27d128f8de65f5934f727511966c8ce0d5d58f8&=&format=webp&width=683&height=294')
        elif self.flag_answer == 8 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('"ОЙ"')
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1190789908667834549/IMG_20231231_005350.jpg?ex=65a31486&is=65909f86&hm=f78f1550fe6bbff59af240cb37bab1699e62722b255ab2b7273aca7223d02416&=&format=webp&width=832&height=272')
        elif self.flag_answer == 9 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('А теперь немного мемов по тому, что происходило в год')
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1190786378317963396/1703975991460.jpg?ex=65a3113c&is=65909c3c&hm=85248fce19faeb8c82fb11da543173c793239248eb87360e106d506f5e2692f1&=&format=webp&width=377&height=467')
        elif self.flag_answer == 10 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1190786501332701194/1703976021140.jpg?ex=65a31159&is=65909c59&hm=8f0772d10aedd6cd7805a99d81356cdfe8e0c368c18c48fdbd6c35c4d76a69d8&=&format=webp&width=467&height=467')
        elif self.flag_answer == 11 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1190787175076343928/1703976181813.jpg?ex=65a311fa&is=65909cfa&hm=b42b2a2cdc3bcafd25aa256c334f86db9508b64f7fa9580d60303a333a89df7f&=&format=webp&width=655&height=467')
        elif self.flag_answer == 12 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1190787556611203123/1703976273504.jpg?ex=65a31255&is=65909d55&hm=c6bdea7bda6539a2a03f9352bbb3e093c2a0542f53a33e0a9c6bf9493091a7d7&=&format=webp&width=929&height=467')
        elif self.flag_answer == 13 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('Ну а теперь, чем же год был для меня особенным. Уверен, вы тоже сможете что-то подобное для себя найти\nРекомендую тоже подумать, это увлекательно, на самом деле')
            await asyncio.sleep(1)
            await msg.channel.send('В этом году я стал этим самым \:)')
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1190786899443470356/1703976115271.jpg?ex=65a311b8&is=65909cb8&hm=47f3e815fdb55048627c3ef9a124aef2c24ba4af4b4bb0ccb2e128c196fa3071&=&format=webp&width=350&height=467')
        elif self.flag_answer == 14 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('В этом году я впервые полностью прочитал (нормальные по размеру) произведения. ураа')
        elif self.flag_answer == 15 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('В этом году я открыл для себя такую группу, как Gojira. Что-то с чем-то(а первую их песню я добавил 13  января 2023)')
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1190787418056560670/1703976239400.jpg?ex=65a31234&is=65909d34&hm=f10d8c7c6453a0b6f1bb36dce5a62946bf91f31f8a3b3d12f976bc31fb6423cf&=&format=webp&width=290&height=467')
        elif self.flag_answer == 16 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('В этом году я начал жестко ботать разных Эриков и ему подобных, РАБОТАЕМ')
            await msg.channel.send('https://media.discordapp.net/attachments/780868711485669397/1190790732483678268/1703977028078.jpg?ex=65a3154a&is=6590a04a&hm=96b452daf8a6a7f4da144fd37e063bd0a7adfafdb33d84a85e6c500437ffb206&=&format=webp&width=350&height=467')
        elif self.flag_answer == 17 and msg.content.lower() == 'продолжить':
            self.flag_answer += 1
            await msg.channel.send('Спасибо вам за этот год \:D')
            exit(0)
        else:
            await msg.channel.send('Ошибка')
intents = discord.Intents.all()

client = Bot(intents=intents)
client.run(token_8)