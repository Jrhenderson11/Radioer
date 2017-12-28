# Radioer



Situation: I enjoy listening to comedians on the radio

Problem 1: I don't like all of them

Problem 2: I am too lazy / forgetful myself to go to the website with the schedule and check which ones I do and don't like this week

Solution: Write a computer program to check for me and send an email to me with a quick update on the weeks comedy 

Technical details:

the schedule is hosted at:

	https://www.bbc.co.uk/schedules/p00fzl7j/2017/12/27#evening

(replacing the parts of url for date I am interested in)

And I am interested in the 6:30 slot which can be found using the following html:

 ...
< span class="timezone--time">18:30</span > 
 ...

 So the program inspects the 6:30 slot of each day in the week and emails the results to 