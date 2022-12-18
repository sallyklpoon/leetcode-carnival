"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a
warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Brute Force:
Iterate through each number and find the count of each date's warmer days

Stack:
We are looking for greatest next number,
Use stack to store the index of temperatures that are looking for next greatest
When we arrive at a new temperature and pop off the stack because the new temp is > the top of stack,
We check the next top of stack to see if the new temp is greater
Using the current index of new temp, we can find the days by subtracting the index by the stack index.

Finally, anything remaining in stack is 0.
"""


def daily_temperatures_bf(temperatures):
    for i in range(len(temperatures)):
        count, found_high = 0, False
        j = i + 1
        while not found_high and j < len(temperatures):
            count += 1
            if temperatures[j] > temperatures[i]:
                found_high = True
            j += 1
        temperatures[i] = count if found_high else 0
    return temperatures


def daily_temperatures(temperatures):
    """
    Stack solution.

    :param temperatures: a list of integers
    :return: a list of integers
    """
    s = [0]
    i = 1
    while i < len(temperatures):
        temp = temperatures[i]
        while s and temp > temperatures[s[-1]]:
            j = s.pop()
            temperatures[j] = i - j
        s.append(i)
        i += 1

    if s:
        for k in s:
            temperatures[k] = 0
    return temperatures
