import cv2
import data_trans as d
from datetime import datetime, timedelta

# given the number of infected people reutrn how big our radius of the circle should be
def radi(inf: int):
	if inf == 1:
		return 1
	elif inf < 10:
		return 2
	elif inf < 100:
		return 3
	elif inf < 1000:
		return 7
	elif inf < 5000:
		return 10
	elif inf < 10000:
		return 15
	elif inf < 25000:
		return 20
	elif inf < 50000:
		return 40
	elif inf < 75000:
		return 50
	elif inf < 100000:
		return 75
	else:
		return 100

# given the integer value since the begining of the data. Find all the entries in that date and plot it onto a png file
def create_circles(days_since):
	image = cv2.imread('lit.png')
	overlay = image.copy()
	this_d = d.start_d + timedelta(days_since)
	today = this_d.day
	this_m = this_d.month
	this_y = this_d.year
	filename = "image"
	if days_since < 10:
		filename += "0"
	filename += str(days_since)
	#print(filename)
	# Red color in BGR 
	color = (0, 0, 255)

	# Line thickness of 2 px 
	thickness = -1
	world_ind = len(d.timed_array[days_since])
	if(world_ind == 0):
		return
	for i in d.timed_array[days_since]:
		if(i.location == "World"):
			world_total = i.total_cases

	u = 0
	for i in d.timed_array[days_since]:
		u += 1
		for j in d.cords:
			if(j[0] == i.location):
				c = j
		# Coordinates of country
		coordinates = c[1]
		coordinates = coordinates[1:]
		coordinates = coordinates[:-1]
		coordinates = coordinates.split(",")
		center_coordinates = (int(coordinates[0]), int(coordinates[1]))
		#print(center_coordinates)
		# Radius of circle 
		radius = radi(int(i.total_cases))
		# Draw the circle 
		hi = cv2.circle(image, center_coordinates, radius, color, thickness) 

		# Transparency factor.
		alpha = 0.4
		image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

	text = 'Todays Date is '
	text += str(this_m)
	text += "/"
	text += str(today)
	text += "/"
	text += str(this_y)

	text += " It has been "
	text += str(days_since)
	text += " since the discovery of COVID-19"

	s_text = "Total cases: "
	s_text += str(world_total)

	t_text = "Total infected countries: "
	t_text += str(u)

	font = cv2.FONT_HERSHEY_SIMPLEX
	org = (20, 30)
	fontScale = 1
	t_color = (0, 0, 0)
	thicc = 3
	org2 = (20, 70)
	org3 = (800, 70)

	# Using cv2.putText() method 
	image_new = cv2.putText(image_new, text, org, font,  
                   fontScale, t_color, thicc, cv2.LINE_AA)
	image_new = cv2.putText(image_new, s_text, org2, font,  
                   fontScale, t_color, thicc, cv2.LINE_AA)
	image_new = cv2.putText(image_new, t_text, org3, font,  
                   fontScale, t_color, thicc, cv2.LINE_AA)

	cv2.imwrite('%s.png' % (filename), image_new) 

	#cv2.imshow(filename, image_new)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

#hehe = 0
#for i in d.timed_array:
#	print(hehe)
#	hehe +=1
hi = 0
for i in range(d.days):
	create_circles(i)





