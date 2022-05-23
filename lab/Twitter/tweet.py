import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
from textblob import TextBlob

query = "(#masker) && (#jokowi) until:2022-01-01 since:2020-01-01"
tweets = []
limits = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
  if len(tweets) == limits:
    break
  else:
    tweet_properties = {}
    tweet_properties['Date'] = tweet.date
    tweet_properties['User'] = tweet.username
    tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.content).split())
    tweet_properties['Tweet'] = tweet_bersih

    analysis = TextBlob(tweet_bersih)
    tweet_properties['Polarity'] = analysis.sentiment.polarity

    #check polarity
    if analysis.sentiment.polarity > 0.0:
      tweet_properties['Sentiment'] = 'Positive'
    elif analysis.sentiment.polarity < 0.0:
      tweet_properties['Sentiment'] = 'Negative'
    else:
      tweet_properties['Sentiment'] = 'Neutral'

    tweets.append(tweet_properties)

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Polarity', 'Sentiment'])
print(df)

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