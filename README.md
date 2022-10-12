# Surfs_Up

## Overview

Using Python, Pandas, and SQLAlchemy, we were able to filter data from a SQLite database to retrive all the temperatures from the months of June and December. We then converted those temperatures to a list, created a DataFrame, and generated a summary of the statistics.

## Results

After calculating the statistics of all the temperatures in June, we displayed them in a table as follows:

![JuneStatistics.png](/Resources/JuneStatistics.png)

And here are the statistics for the temperatures in December:

![DecemberStatistics.png](/Resources/DecemberStatistics.png)

By comparing the two tables, we are able to come up with three key differences:

- The minimum temperature in December is 8 degrees cooler than in June

- The temperatures in June were generally higher than that of December, but not by much.

- June's standard deviation was less than that of December's, meaning the temperature fluctuated less in June than in December.

## Summary

Overall, the weather in June and December are remarkably similar, although there is more variance in the temperatures in December. It is slightly more likely that the Surf and Ice Cream shop would be more successful closer to the Summer months than the Winter months. However, it seems like it could remain open year round!

We could provide even more information with two additional queries: 

1. A query that could show the difference in precipitation between June and December to determine the effects of inclement weather.

2. If we had data on locations among the various islands, we could run a query that would determine weather locations based on location to see if certain parts of an island faired better weather.
