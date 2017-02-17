#!/bin/bash

TWITTER_USER="realDonaldTrump"

if [ ! -f ./credentials.sh ]; then
	echo "'./credentials.sh' does not exist. Please make a copy of credentials.sh.template and insert your Twitter API keys."
	exit
else
	source credentials.sh
fi

if [ ! -f ./tweet_dumper.py ]; then # download and patch tweet dumper if it does not already exist
	echo "Downloading tweet_dumper.py"
	wget "https://gist.githubusercontent.com/yanofsky/5436496/raw/a4277a2563a903ad42bf7c41a98243578f49bca7/tweet_dumper.py"
	
	# Insert Twitter API credentials
	sed -i "s/consumer_key = \"/consumer_key = \"$twitter_consumer_key/" tweet_dumper.py
	sed -i "s/consumer_secret = \"/consumer_secret = \"$twitter_consumer_secret/" tweet_dumper.py
	sed -i "s/access_key = \"/access_key = \"$twitter_access_key/" tweet_dumper.py
	sed -i "s/access_secret = \"/access_secret = \"$twitter_access_secret/" tweet_dumper.py
	
	# Dirty hack to modify output format:
	truncate -s `head -n48 tweet_dumper.py | wc -c` tweet_dumper.py
	echo "
	open('corpus.txt', 'w').write('\n'.join(tweet.text.encode('utf-8') for tweet in alltweets))

get_all_tweets('$TWITTER_USER')" >> tweet_dumper.py
	
fi

python2 tweet_dumper.py

curl "https://raw.githubusercontent.com/ryanmcdermott/trump-speeches/master/speeches.txt" >> corpus.txt
