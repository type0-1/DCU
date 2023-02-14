import sys

lines = sys.stdin.readlines()
speeds = []

if len(lines) > 2:
	i = 2
	while i < len(lines):
		ph, pm = lines[i - 1].strip().split()
		ch, cm = lines[i].strip().split()
		miles = (int(cm) - int(pm))
		hours = (int(ch) - int(ph))
		speeds.append(miles // hours)
		i += 1
	print(max(speeds))
else:
	h, m = lines[1].strip().split()
	print(int(m) // int(h))
