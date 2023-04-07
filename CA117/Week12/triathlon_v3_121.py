class Triathlete(object):

	def __init__(self, name, tid):
		self.name = name
		self.tid = tid
		self.time = {}

	def add_time(self, discipline, time):
		self.time[discipline] = time

	def get_time(self, discipline):
		return self.time[discipline]

	def race_time(self):
		total = sum([time for time in self.time.values()])
		return total

	def __eq__(self, other):
		return self.race_time() == other.race_time()

	def __lt__(self, other):
		return self.race_time() < other.race_time()

	def __str__(self):
		output = []
		output.append(f'Name: {self.name}')
		output.append(f'ID: {self.tid}')
		output.append(f'Race time: {self.race_time()}')
		return "\n".join(output)

class Triathlon(object):

	def __init__(self):
		self.map = {}

	def add(self, other):
		self.map[other.tid] = (other.name, other.tid, other.race_time())

	def best(self):
		best = min(self.map.values())
		output = []
		output.append(f'Name: {best[0]}')
		output.append(f'ID: {best[1]}')
		output.append(f'Race time: {best[2]}')
		return "\n".join(output)

	def worst(self):
		worse = max(self.map.values())
		output = []
		output.append(f'Name: {worse[0]}')
		output.append(f'ID: {worse[1]}')
		output.append(f'Race time: {worse[2]}')
		return "\n".join(output)		

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()