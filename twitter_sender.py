# TWITTER POST
import tweepy
api = tweepy.Client(
    consumer_key='',
    consumer_secret='',
    access_token='',
    access_token_secret=''
)
try:
    print('\033[35m ☢️  RADIO ARMAGEDOM TWITTER MESSENGER ☢️  \033[m')
    tweet = input('Digite seu tweet: ')
    api.create_tweet(text=tweet)
    print("☢️  \033[1;32mO seu tweet foi enviado com sucesso!\033[m")
except:
    print('Erro no envio do tweet.')
