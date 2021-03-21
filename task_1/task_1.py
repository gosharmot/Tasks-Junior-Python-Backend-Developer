a = "111111111111111111111111100000000"
b = list("111111111111111111111111100000000")

def task(a):
    for i, v in enumerate(a):
        if v == '0' or v == 0:
            return i

print(task(a))
print(task(b))