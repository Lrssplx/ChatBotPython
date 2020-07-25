from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Bot test')

conversa = ['oi, boa noite', 'boa noite', 'como vai?', 'estou bem','qual o seu hobby?', 'jogar lol',
'a quanto tempo voce joga lol?', 'jogo a 14 anos' ]
conversa2 = ['qual a sua idade?', 'eu tenho 20 anos', 'qual a sua cor preferida?', 'minha cor preferida é roxo']

trainer = ListTrainer(bot)
trainer.train(conversa)
trainer.train(conversa2)

while True:
    quest = input('Ana e Larissa:')
    response = bot.get_response(quest)
    print('Pety:', response)
    
