# trumpogram
The World, according to Donald Trump.

## Output
![Output Map Image](https://raw.githubusercontent.com/DavidBuchanan314/trumpogram/master/output.png)

## About

Inspired by this tweet: https://twitter.com/SwiftOnSecurity/status/832074664193249281

There isn't much to this project, just plugging a few existing tools together.

The identification of place names is performed using the `spacy` python library, so any issues in this area aren't my problem :P.
I used `spacy` to output a list of GPEs and NORPs (Geo-Political Entities, Nationalities Or Religious/Political Groups).
The raw output can be found in `places.csv`. Since this data is somewhat messy and unpredictable, I processed it manually in a spreadsheet, `processed.ods`, before combining it with the geographical data (see below).
Locations with fewer than 3 mentions were ignored entirely. I might fix this at some point, but I don't think it will have much impact on the final map.

## Corpus
The corpus for this project was obtained from multiple sources (I might add more):

 - 2016 Campaign speeches, from [ryanmcdermott/trump-speeches](https://github.com/ryanmcdermott/trump-speeches)
 - @realDonaldTrump's tweets, via [tweet_dumper.py](https://gist.github.com/yanofsky/5436496)

## Mapping

I obtained the map data from [thematicmapping.org](http://thematicmapping.org/downloads/TM_WORLD_BORDERS_SIMPL-0.3.zip)
I generated the final map using the [ScapeToad](http://chorogram.choros.ch/scapetoad/) tool.
