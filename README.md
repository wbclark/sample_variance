The purpose of this script is to demonstrate a basic point about how sample variance is much smaller than individual event variance when many events are sampled.

Here is a basic example:

```
$ python3 main.py 
simulated 100 encounters
lowest average damage roll over all encounters was: 99.72331184375678
highest average damage roll over all encounters was: 100.26679823342167
standard deviation of average damage roll over all encounters was: 0.11698971369890841
```

In the script, we simulated 100 encounters of 5 minutes each and 140 damage rolls ("events") per minute of the encounter.

Each individual damage roll was sampled from a uniform distribution with a range of 95 to 105.

For each encounter simulated, the mean of all damage rolls for that encounter was computed. The minimum average damage roll for the 100 encounters was 99.72331184375678,
while the maximum average damage roll was 100.26679823342167. So even though individual damage rolls had a range of 10 damage (+-5% of the 100 damage average), over the
course of a moderate number of rolls, the actual variance in AVERAGE damage per roll was about 0.5 damage (about 20 times smaller than the variance in any individual roll).

The standard deviation of average damage roll over all encounters was 0.11698971369890841, meaning very loosely that "most" encounters had an average damage roll in the range of
99.88 to 100.12

The conclusion: a +-5% damage range on individual rolls translates to roughly 0.014% variance in performance due to roll variance over the course of a 5 minute encounter, which
is for all practically purposes negligible. The ONLY impact this slight variance in individual damage rolls introduces is lowering the mental fatigue from seeing the same numbersrepeatedly.
