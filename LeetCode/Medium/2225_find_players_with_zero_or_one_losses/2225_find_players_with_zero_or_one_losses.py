"""
We need to know all the player numbers
Iterate 1 to create the dict to check player number and count losses
Iterate again to get list of ppl who didn't lose and those who lost one match
sort both lists and return
"""

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = {}
        no_lose, single_lose = [], []

        for m in matches:
            count[m[0]] = count.get(m[0], 0)
            count[m[1]] = count.get(m[1], 0) + 1
        for player, lose in count.items():
            if not lose:
                no_lose.append(player)
            if lose == 1:
                single_lose.append(player)
        return [sorted(no_lose), sorted(single_lose)]
