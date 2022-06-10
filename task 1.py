file = open('log.txt', 'r')
all_sids = []
for line in file:
    if '10.1.192.38' in line:
        sid = ''
        index = line.find('sid=') + 5
        while line[index] != '&':
            sid += line[index]
            index += 1
        all_sids.append(sid[0:-1])

all_sids.sort()
print(*all_sids)