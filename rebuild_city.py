"""
We have to rebuild the city with build with the same height, for that we have to minimize the number of demolition of floors.

A build can't be constructed new floors but he can be demoted. 

Example: 

[3, 7 , 5]

if the height of the building is 3 so [3, 3, 3]: (3-3) + (7-3) + (5- 3) = 6
if the height of the build is 2 so [2, 2, 2]: (3 - 2) + (7-2) + (5-2) = 9
if the height of the build is 5 so [0, 5, 5]: 3 + (7 - 5) + (5-5) = 5
"""


def calculateDemolition(builds):
    if not builds:
        return 0
    menores = 0
    size = len(builds)
    maiores = sum(builds[1:size])
    builds.sort()
    demolition = float('inf')
    for i in range(0, size): 
        if i > 0:
            menores += builds[i - 1]
            maiores -= builds[i]
        indice_build = i + 1
        currently_demolition = maiores + menores - (builds[i] * (size - indice_build))
        if demolition > currently_demolition:
            demolition = currently_demolition
    return demolition

builds = [3]

# builds = [3, 7, 5]

# builds = [2, 1, 3, 5, 7, 8, 10]

print(f'result = {calculateDemolition(builds)}')
