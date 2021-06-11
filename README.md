# Covid19tracker

James Kang

Introduction
I have decided to track the spread of COVID-19 across the world. Data was given by WHO (World Health Organization) (https://ourworldindata.org/coronavirus-source-data), the data I used pulled from the website titled “Full dataset”. I believe that my program is able to run even if the data updates in the future. Only problem is that WHO’s data is not consistent (originally, they had the start date set from 2/11 but they added since the start of the year). Also the data had some holes which were tricky to figure out.

This project wasn’t made to put fear into our community, but to rather show people how easily air born illnesses could spread. 

Breakdown of files
countries.txt: where the coordinates were locational with respect to the png file (was all done manually). 

full_data.csv: all publicly available data from WHO

data_trans.py: python file to turn the data into variables and lists.

redcircle.py: python file that turns the data into red circles

Methods
Transparent red circles were used to indicate a country being infected. The size of the circle indicated how many cases there were (actively or not active)
1: 1
10: 2
100: 3
1000: 7
5000: 10
10000: 15
25000: 20
50000: 40
75000: 50
100000: 75
>100000: 100
Left side is the number of cases in a given country. Right is the indicates the radius of the circle (pixels) (the larger the number of cases the larger the circle) these ratios were determined by trial and error and chosen because they look the nicest proportionally.

Running the program
To run the program that make the images simply run “python3 redcircle.py” 

Ffmpeg was used to make the movie. The exact command I used was:
ffmpeg -f image2 -i image%02d.png -filter:v "setpts=10*PTS" -vcodec mpeg4 -r 10 -b 18000000 movie.mp4

Future plans:
- making the data extracting from the WHO website automatic.
- making the ffmpeg the video as well as deletion of all the photos automatic
