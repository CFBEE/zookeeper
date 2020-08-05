initial_atoms = int(input())
final_atoms = int(input())
n = initial_atoms
r = final_atoms
t = int(0)

while n >= r:
    n /= 2
    t += 12
print(t)
