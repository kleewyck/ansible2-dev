import feedparser
NewsFeed = feedparser.parse("https://water.weather.gov/ahps2/rss/obs/shli2.rss")
entry = NewsFeed.entries[1]

print (entry.keys())
