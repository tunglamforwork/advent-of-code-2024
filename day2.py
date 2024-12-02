def safe_zone(n):
    return [-3, -2, -1, 1, 2, 3]


def is_valid(report):
    trend = 0
    prev_trend = 0
    """Check if a report is valid based on the difference rule."""
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff not in safe_zone(report[i]):
            return False
        if diff > 0:
            trend = 1
        else:
            trend = -1

        if trend != prev_trend and prev_trend != 0:
            return False

        prev_trend = trend

    return True


with open("input.txt") as file:
    ans = 0
    for line in file:
        valid = False
        report = list(map(int, line.strip().split(" ")))
        # Check if inherently safe
        if is_valid(report):
            ans += 1
        else:
            # Check if removing one level makes it valid
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1 :]
                if is_valid(modified_report):
                    ans += 1
                    break

    print(ans)
