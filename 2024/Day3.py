f = open("day3input.txt", "r")
memory = ""
for x in f:
    memory += x


def extract_mul_results(memory):
    total = 0
    i = 0
    while i < len(memory):
        if memory[i:i+4] == "mul(":
            j = i + 4
            res = "mul("
            while j < len(memory) and (memory[j].isdigit() or memory[j] == ',' or memory[j] == ')'):
                res += memory[j]
                if memory[j] == ')':  
                    break
                j += 1  
            if res.count(',') == 1 and res.endswith(')'):  
                parts = res[4:-1].split(',')
                if parts[0].isdigit() and parts[1].isdigit():
                    total += int(parts[0]) * int(parts[1])
            i = j  
        i += 1
    return total

print(extract_mul_results(memory))




def extract_mul_results(memory):
    total = 0
    i = 0
    enabled = True  # Multiplications start enabled

    while i < len(memory):
        if memory[i:i+5] == "don't":
            enabled = False
            i += 5
        elif memory[i:i+3] == "do(":
            enabled = True
            i += 3
        elif memory[i:i+4] == "mul(" and enabled:
            j = i + 4
            res = ""
            while j < len(memory) and (memory[j].isdigit() or memory[j] == ',' or memory[j] == ')'):
                res += memory[j]
                if memory[j] == ')':
                    break
                j += 1
            if res.count(',') == 1 and res.endswith(')'):
                x, y = res[:-1].split(',')
                if x.isdigit() and y.isdigit():
                    total += int(x) * int(y)
            i = j
        i += 1

    return total

print(extract_mul_results(memory))
