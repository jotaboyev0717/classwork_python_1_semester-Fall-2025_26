def longest_downward_trend(prices):
    if len(prices) < 2:
        return 0  # not enough data for a trend

    longest = 0
    current = 1  # start counting from first element

    for i in range(1, len(prices)):
        if prices[i] < prices[i - 1]:  # still decreasing
            current += 1
        else:
            longest = max(longest, current)
            current = 1  # reset when the trend breaks

    longest = max(longest, current)  # check last trend

    return longest if longest > 1 else 0
