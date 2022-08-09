""""
    mb = max(bottingPower)
    sum_pp = sum(processingPower)
    power = mb + (sum_pp * k)
"""

def verifyMaxCluster(bootingPower, processingPower, maxPower):
    left = 0
    right = 1
    calculate_power = 0
    cluster_count = 0
    qtde_cluster = 0
    while (left < len(bootingPower)) and (right < len(bootingPower)):
        calculate_power = calculatePower(bootingPower[left:right], processingPower[left:right])
        if calculate_power > maxPower:
            left += 1
            qtde_cluster = max(qtde_cluster, cluster_count)
            cluster_count -= 1 
            if left == right:
                right += 1
                cluster_count = 0
        else:
            right += 1
            cluster_count += 1
    return max(qtde_cluster, cluster_count)


def calculatePower(bootingPower, processingPower):
    max_bp = max(bootingPower)
    sum_pp = sum(processingPower)
    k = len(bootingPower)
    return max_bp + (sum_pp * k)


if __name__ == "__main__":
    processingPower = [4, 1, 4, 5 ,3]
    bootingPower = [8, 8, 10, 9, 12]
    maxPower = 33
    print(verifyMaxCluster(bootingPower, processingPower, maxPower))