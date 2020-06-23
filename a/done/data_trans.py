'''
CIS410 Final project
Made by James Kang
Movie!
Written in Python
'''

import csv
from datetime import datetime, timedelta

countries = []
# each entry
class Entry:
	def __init__(self, date: datetime, location: str, new_cases: int = 0, new_deaths: int = 0, total_cases: int = 0, total_deaths: int = 0):
		self.date = date
		self.location = location
		self.new_cases = new_cases
		self.new_deaths = new_deaths
		self.total_cases = total_cases
		self.total_deaths = total_deaths

# each country
class Country:
	def __init__(self, name: str, entries, total_cases: int = 0, total_deaths: int = 0):
		self.name = name
		self.entries = []
		self.total_cases = total_cases
		self.total_deaths = total_deaths
	def get_numbers(self, date: datetime):
		for d in self.entries:
			if d.date == date:
				return d

def insert(ent: Entry, lis):
	for i in lis:
		if ent.location == i.name:
			i.entries.append(ent)
			#print("same")
			return
	#print("new country")
	#print(ent.location)
	lis.append(Country(ent.location, [ent], 0, 0))

#figured out how to fill the holes
def fix_a(list_b, list_n):
	for i in list_b:
		exist = 0
		for j in list_n:
			if(j.location == i.location):
				exist = 1
		if(exist == 0):
			list_n.append(i)

prev = "hi"
start_d = datetime(2021, 5, 23)
newest_d = datetime(2019, 1, 1)

with open('full_data.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	next(spamreader)
	for row in spamreader:
		hi= ', '.join(row)
		hi = hi.split(",")
		if(int(hi[-2]) != 0):
			my_date = datetime.strptime(hi[0], "%Y-%m-%d")
			if my_date < start_d:
				start_d = my_date
			elif my_date > newest_d:
				newest_d = my_date

			#print(my_date)
			#print(my_date)
			#print('Type: ',type(my_date))
			p = len(hi)
			if(p == 6):
				ent = Entry(my_date, hi[1], hi[2], hi[3], hi[4], hi[5])
			elif(p == 7):
				comb = hi[1] + hi[2]
				ent = Entry(my_date, comb, hi[3], hi[4], hi[5], hi[6])
			elif(p == 8):
				comb = hi[1] + hi[2] + hi[3]
				ent = Entry(my_date, comb, hi[4], hi[5], hi[6], hi[7])
			elif(p == 9):
				comb = hi[1] + hi[2] + hi[3] + hi[4]
				ent = Entry(my_date, comb, hi[5], hi[6], hi[7], hi[8])
			elif(p == 10):
				comb = hi[1] + hi[2] + hi[3] + hi[4] + hi[5]
				ent = Entry(my_date, comb, hi[6], hi[7], hi[8], hi[9])

			insert(ent, countries)

#print(countries[8].name)
#print("start date is")
#print(start_d.date())
#print("eariest date is")
#print(newest_d.date())
days = (newest_d - start_d).days
cur_day = start_d
timed_array = []
for i in range(days):
	today = []
	for j in countries:
		for t in j.entries:
			if t.date == cur_day:
				today.append(t)
				break
	timed_array.append(today)
	cur_day += timedelta(1)

t_days = len(timed_array)
for i in range(1, t_days):
	fix_a(timed_array[i-1], timed_array[i])

	#print("today is ", cur_day.date())
	#print("total incidents are: ", len(today))
#file1 = open("countries.txt","w")
#for i in countries:
#	print(i.name)
#	file1.write(i.name)
#	file1.write("/\n")

#file1.close()

# coordinates of all the countries (manually put in the text file)
cords = []
fname = "countries.txt"
lines = open(fname).read().splitlines()
for i in lines:
	hi = i.split("/")
	cords.append(hi)

#for i in cords:
#	print(i)

