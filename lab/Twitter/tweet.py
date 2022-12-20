import snscrape.modules.twitter as sntwitter
import pandas as pd
import os
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from textblob import TextBlob
import matplotlib.pyplot as plt

query = "(#KUHP) && (KUHP) until:2022-12-20 since:2022-11-01"
tweets = []
limits = 500

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
  if len(tweets) == limits:
    break
  else:
    tweet_properties = {}
    tweet_properties['Date'] = tweet.date
    tweet_properties['User'] = tweet.username
    #cleaning
    tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ", tweet.content).split()).lower()
    tweet_properties['Tweet'] = tweet_bersih
    #stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    tweet_bersih = stemmer.stem(tweet_bersih)
    #stopword removal
    factory1 = StopWordRemoverFactory()
    stopword = factory1.create_stop_word_remover()
    tweet_bersih = stopword.remove(tweet_bersih)
    #translate to english
    analysis = TextBlob(tweet_bersih)
    an = analysis.translate(from_lang="id", to="en")
    #get polarity
    tweet_properties['Polarity'] = an.sentiment.polarity

    #check polarity
    if tweet_properties['Polarity'] > 0.0:
      tweet_properties['Sentiment'] = 'Positive'
    elif tweet_properties['Polarity'] < 0.0:
      tweet_properties['Sentiment'] = 'Negative'
    else:
      tweet_properties['Sentiment'] = 'Neutral'

    tweets.append(tweet_properties)

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Polarity', 'Sentiment'])
print(df)

#if tweet.csv exists, delete it
if os.path.exists('lab/Twitter/tweet.csv'):
  os.remove('lab/Twitter/tweet.csv')
#export to csv
df.to_csv('lab/Twitter/tweet.csv', index=False, encoding='utf-8')

#check if tweet is a retweet
if tweet.retweetCount > 0:
  if tweet_properties not in tweets:
    tweets.append(tweet_properties)
else:
  tweets.append(tweet_properties)

text_pos = [t for t in tweets if t['Sentiment'] == 'Positive']
text_neg = [t for t in tweets if t['Sentiment'] == 'Negative']
text_neu = [t for t in tweets if t['Sentiment'] == 'Neutral']

print("Sentiment Analysis: ")
print("Positive: ", len(text_pos), "({} %)".format(round(len(text_pos)/len(df['Tweet'])*100, 2)))
print("Negative: ", len(text_neg), "({} %)".format(round(len(text_neg)/len(df['Tweet'])*100, 2)))
print("Neutral: ", len(text_neu), "({} %)".format(round(len(text_neu)/len(df['Tweet'])*100, 2)))

#grafiks sentiment analysis
labels = 'Positive', 'Negative', 'Neutral'
sizes = [len(text_pos), len(text_neg), len(text_neu)]
colors = ['green', 'red', 'gold']


plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title('Sentiment Analysis Tweet tentang RKUHP')
plt.axis('equal')
plt.show()