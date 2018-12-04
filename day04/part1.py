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

# iterate through all minutes and count times
guards = {}
for m in minute:
    for g in m:
        if g not in guards:
            guards[g] = 0
        guards[g] += m[g]

# which guard was asleep most?
sleepy_guard, _ = max(guards.items(), key=operator.itemgetter(1))

# which minute was most common for said guard?
sleepy_guard_minutes = [0 for _ in range(60)]
for m in range(len(minute)):
    if sleepy_guard in minute[m]:
        sleepy_guard_minutes[m] = minute[m][sleepy_guard]

sleepy_guard_minute = sleepy_guard_minutes.index(max(sleepy_guard_minutes))

print(sleepy_guard, sleepy_guard_minute, sleepy_guard * sleepy_guard_minute)
