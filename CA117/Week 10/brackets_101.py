def matcher(string):
	string = list(string)
	dic = {")": "(", "}":"{", "]":"["}
	check = []
	if string[0] in dic:
		check.append(string[0])
	for s in string:
		if s in dic.values():
			check.append(s)
		elif s in dic.keys():
			if len(check) > 0 and dic[s] == check[-1]:
				check.pop()
	return len(check) == 0