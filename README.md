# Radioer

Situation: I enjoy listening to comedians on the radio

Problem 1: I don't like all of them

Problem 2: I am too lazy / forgetful myself to go to the website with the schedule and check which ones I do and don't like this week

Solution: Write a computer program to check for me and send an email to me with a quick update on the weeks comedy 

### Technical details:

the schedule is hosted at:

	https://www.bbc.co.uk/schedules/p00fzl7j/2017/12/27#evening

(replacing the parts of url for date I am interested in)

And I am interested in the 6:30 slot which can be found using the following html:

 ...
< span class="timezone--time">18:30</span > 
 ...

 So the program inspects the 6:30 slot of each day in the week and emails the results to me

 The program relies on web scraping, first it finds the current date and uses a website to determine day of the week (although I think there is a mathematical way of doing that).

 Then the program uses the bbc iplayer website, determined by the date in question to look for the title, description and link to whatever is in the 6:30 slot.

 once the information is gathered it emails them to any recipients. 

 =========================================================================

To sanitise the file I uploaded to the repo I have removed the email address and password and recipient email, however all 3 are needed to send the email. You will need a valid gmail address and password, because the program uses the gmail servers to send the email. you could of course substitute the email sending code for your own if you want to work with a different email provider, or you could use the text generated and host it on a website or something.

### Cron example:

This tool is useful if run automatically on a regular basis at least once per week, on a linux system this is done using cron.
run cron with

	crontab -e

and add the following line

	0 12 * * 1 python ~/Documents/git/Radioer/radio.py 

This makes the too run at 12 (midday I think) the first day of each week 