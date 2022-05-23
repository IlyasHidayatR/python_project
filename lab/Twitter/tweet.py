import snscrape.modules.twitter as sntwitter
import pandas as pd
from textblob import TextBlob

query = "(#masker) (#jokowi) until:2022-01-01 since:2017-01-01"
tweets = []
limits = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
  if len(tweets) == limits:
    break
  else:
    tweets.append([tweet.date, tweet.username, tweet.content])


df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
df['Polarity'] = df['Tweet'].apply(lambda x: TextBlob(x).sentiment.polarity)

#check polarity
if df['Polarity'].mean() > 0.0:
  df['Sentiment'] = 'Positive'
elif df['Polarity'].mean() < 0.0:
  df['Sentiment'] = 'Negative'
else:
  df['Sentiment'] = 'Neutral'
#print all
print(df)