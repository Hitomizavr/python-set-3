numbers = [int(s) for s in input().split()];
setNums = set();
for num in numbers:
    if num in setNums:
        print('YES');
    else:
        print('NO');
        setNums.add(num);