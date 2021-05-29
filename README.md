# Vaccélérateur Hour Tally

[Vaccélérateur](https://twitter.com/vaccelerateur) is a Twitter account created by [Guillaume Campagna](https://twitter.com/gcamp) that tweets out available vaccination appointments. I wanted to see at what hours people were more likely to cancel appointments, starting in Montreal (Vaccélérateur06). The bot has Tweeted ~1300 times since the beginning of May. Using the hour of the bot Tweets as a proxy, it seems like cancellation times peak between 2 and 3 PM EST.

<!---![bar graph of total tweets per hour, with a low of 13 tweets sent from 2-3 AM EST, increasing to a peak of 95 tweets sent from 2-3 PM EST](https://github.com/mkshaw/vaccelerateur/blob/master/img/graph.png)--->

<img src="https://github.com/mkshaw/vaccelerateur/blob/master/img/graph.png" alt = "bar graph of total tweets per hour, with a low of 13 tweets sent from 2-3 AM EST, increasing to a peak of 95 tweets sent from 2-3 PM EST" width = 600 height = 476/>

I used the Twitter API via Tweepy to pull the Vaccélérateur Tweets, and [termgraph](https://github.com/mkaz/termgraph) to create a basic graph in terminal.

## Usage

To run the code yourself, first create a [Twitter Developer account](https://developer.twitter.com/en/apply-for-access) and create a project to obtain a public and private API key. For privacy reasons, I stored my keys in a json file within scripts called `keys.json`. The file was formatted as: {"api_key" = ______, "api_secret" = ______}.

To run the script in terminal, use the command `python3 scripts/main.py`. This will scrape up to 1500 Tweets from the Vaccélérateur account and save them in `data/vacc06.dat`. The command to graph the data is `termgraph data/vacc06.dat`.
