"""
1854. Maximum Population Year
"""


def maximum_population(logs: list) -> int:
    pop_count = dict()
    for pair in logs:
        for year in range(pair[0], pair[1]):
            pop_count[year] = 1 if year not in pop_count else pop_count[year] + 1

    max_pop = 0
    for year, pop in pop_count.items():
        max_pop = pop if pop > max_pop else max_pop

    years = []
    for year in pop_count:
        if pop_count[year] == max_pop:
            years.append(year)

    return min(years)