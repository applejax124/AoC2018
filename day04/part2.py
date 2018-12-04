import sys
from datetime import datetime as dt
import operator

entries = []

# store entries in a list
for line in sys.stdin:
    line = line.strip()

    line = line.split('] ')
    line[0] = line[0].strip('[')

    d = dt.strptime(line[0], '%Y-%m-%d %H:%M')
    e = line[1]

    entries.append((d,e))

# sort entries by datetime
entries = sorted(entries)

minute = [{} for _ in range(60)]

# create a list of tuples with guard id and minute asleep
guard = 0
for e, entry in enumerate(entries):
    date = entry[0]
    event = entry[1]

    # check event
    if event.startswith('Guard'):
        event = event.split()
        guard = int(event[1].strip('#'))
        
        n = e+1
        next_date, next_event = entries[n]
        while not next_event.startswith('Guard'):
            if next_event == 'falls asleep':
                start = int(next_date.minute)
            elif next_event == 'wakes up':
                stop = int(next_date.minute)
                for i in range(start, stop):
                    if guard not in minute[i]:
                        minute[i][guard] = 0
                    minute[i][guard] += 1
            n += 1
            try: 
                next_date, next_event = entries[n]
            except:
                break

# iterate through all minutes and find max
sleepy_guard_minute_max = 0
sleepy_guard = 0
sleepy_guard_minute = 0
for i, m in enumerate(minute):
    for g in m:
        if m[g] > sleepy_guard_minute_max:
            sleepy_guard_minute_max = m[g]
            sleepy_guard = g
            sleepy_guard_minute = i

print(sleepy_guard, sleepy_guard_minute, sleepy_guard * sleepy_guard_minute)
