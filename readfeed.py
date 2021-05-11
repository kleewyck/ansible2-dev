import feedparser
NewsFeed = feedparser.parse("https://water.weather.gov/ahps2/rss/obs/shli2.rss")
dir(NewsFeed)
entry = NewsFeed.entries[0]

print (entry.keys())
