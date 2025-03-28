f = open("/day2input.txt", "r")
report_list = []
for x in f:
    report = x.split(' ')
    for i in range(len(report)):
        report[i] = int(report[i])
    report_list.append(report)

print(report_list)

def check_report(report):
    for i in range(len(report) - 1):
        if i < len(report) - 2:
            if not ((report[i] <= report[i+1] <= report[i+2]) or (report[i] >= report[i+1] >= report[i+2])):
                return False
        if not (1 <= abs(report[i] - report[i+1]) <= 3):
            return False
    return True

count = 0

for report in report_list:  
    if check_report(report):
        count += 1

print(count)



def check_report(report):
    for i in range(len(report) - 1):
        if i < len(report) - 2:
            if not ((report[i] <= report[i+1] <= report[i+2]) or (report[i] >= report[i+1] >= report[i+2])):
                return False
        if not (1 <= abs(report[i] - report[i+1]) <= 3):
            return False
    return True

def is_safe(report):
    if check_report(report):
        return True
    for i in range(len(report)):
        if check_report(report[:i] + report[i+1:]):
            return True
    return False

count = 0

for report in report_list:
    if is_safe(report):
        count += 1

print(count)