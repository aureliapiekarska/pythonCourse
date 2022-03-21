def generate_fibonnaciego:
results =[0,1,1]

for i in range (2,n):
    current_result = results[-1] +results[-2]
    results.append(current_result)
    print(current_result)

print(results)
for nr in range(len(results)):
    print(f'Fib od {nr}->{results[nr]}')