import matplotlib.pyplot as plt
import turtle

# Collect the data

"""
print("Enter Pokeman data:")
print("Day 1: ", end="")
day1 = int(input())5
print("Day 2: ", end="")
day2 = int(input())
print("Day 3: ", end="")
day3 = int(input())
"""
# New Version - loop and get each dat at a time
data = [] #empty list
#num_days = int(input("How many days?"))
num_days = turtle.numinput("Input","How many days?")
num_days = int(num_days)
for day in range(num_days):
  #print("Day ", day, ":", end="")
  #today = int(input())
  label = "Day #" + str(day) # "Day 1" and so on
  today = turtle.numinput(label, "How many Pokeman?")
  data.append(today) # add it to the end of the list
  
# put the data in a list (Done)
# print min and max
print("Best day:", max(data))
print("Worst day:", min(data))
# TODO: total and average
total = 0
for num in data:
  total += num
  # total is now all the numbers in data, added up
average = total / num_days
print("Total:", total)
print("Average:", average)


# TODO: Graph the real data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("Pokeman Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()

