import tweepy,json
import pandas as pd

consumer_key="oicGgwkLsGzpPykBMtcdCiPtb"
consumer_secret="pIWxPN9ft5eM1pTNdcpas9lQGeYqVIyvPhgnO0evR4u5c1OEXw"
bearer_token="AAAAAAAAAAAAAAAAAAAAAGp6WAEAAAAAgK%2F7yTxlgrdVpc1vHcH5AQkCA5Q%3DUcaeAO6XNU68vvY6CPJtBoecN8hYBs5D6bMgfUCLJEY0BzSMwg"
access_token="1463304369395302401-4A4o7rdFx4oYBfUU5M7czQWQGNNHpR"
access_token_secret="Ft0YuedZ9fzQ7Hq22aAvwk9NO2i0fuwFaEBK7T4GrnVV9"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
client=tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret,wait_on_rate_limit=True)

def collect_tweet(next_token):
    a=(client.search_recent_tweets(query="(#covid OR covid OR #pfizer OR pfizer OR #moderna OR moderna OR astrazeneca OR astra-zeneca OR #astrazeneca OR #johnsonandjohnson OR pandemic OR johnson&johnson OR astra zeneca OR vaccination OR vaccine) -is:retweet -is:reply lang:en",tweet_fields=['created_at'],max_results=100,next_token=next_token,end_time="2021-11-30T00:00:00+00:00",start_time="2021-11-27T00:00:00+00:00"))
    lst=list()
    for tweet in a.data:
        d=dict()
        d['created_at']=tweet.created_at
        d['text']=tweet.text
        d['id']=tweet.id

        lst.append(d)
    return (lst,a.meta['next_token'])

f=collect_tweet(None)
fun=f[0]
df=pd.json_normalize(fun)
while len(df.index)<1000:
    f=collect_tweet(f[1])
    fun+=f[0]
    df=pd.json_normalize(fun)
    df=df.drop_duplicates(subset='text')


print(df.text)
df.to_csv('tweets.csv',index=False)
