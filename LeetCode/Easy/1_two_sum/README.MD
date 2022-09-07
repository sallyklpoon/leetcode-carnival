# 1. Two Sum
## Brute Force
A Brute Force (BF) solution is to use a double loop, checking, one number after another, to match with the next number that
will sum up to the target.

BF solution would run at O(N^2) and is inefficient.

My BF solution, at worse case, can run up to O(N^2) given that I use a while loop including a list search
for the remainder of the list following the 'current' number being tested against the target.

Although not the best solution, by utilization of a while-loop to check the outcome, 
I am not exhausting all elements in the entire list once a solution has been found.

## Considerations
* Numbers can be (-) or (+)
* There will always be at least two numbers
* Target can be (-) or (+)
* we must keep track of indices, meaning sort may not be helpful