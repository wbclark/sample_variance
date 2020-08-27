from numpy.random import uniform
from numpy import mean
from numpy import std

# yellow attacks, bleed ticks, poison ticks, damage procs, etc... rough, stupid estimate, and probably too low
damage_rolls_per_minute = 140

# length of encounter to simulate
mins_encounter = 5

# simulate damage rolls for a single encounter
def simulate_encounter():
    return [uniform(95, 105) for x in range(mins_encounter * damage_rolls_per_minute)]

# simulate damage rolls for n encounters
def simulate_n_encounters(n):
    return [simulate_encounter() for x in range(n)]

num_encounters = 100

# simulate 100 encounters
encounters = simulate_n_encounters(num_encounters)

# compute mean damage roll for each encounter
means = [mean(encounter) for encounter in encounters]

# compute min/max sample mean, i.e., minimum/maximum average damage roll over the course of all simulated encounters
minimum_avg_damage = min(means)
maximum_avg_damage = max(means)

# compute standard deviation of sample means
standard_deviation = std(means)

# print summary
print("simulated " + str(num_encounters) + " encounters")
print("lowest average damage roll over all encounters was: " + str(minimum_avg_damage))
print("highest average damage roll over all encounters was: " + str(maximum_avg_damage))
print("standard deviation of average damage roll over all encounters was: " + str(standard_deviation))
