import re
import sys
import smtplib
import optparse
import urllib2
import datetime
from email import Encoders
from bs4 import BeautifulSoup
from datetime import timedelta
from email.MIMEBase import MIMEBase
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

def send_email(user, pwd, to, subject, text):
	msg = MIMEText(text)
	msg['FROM'] = user
	msg['To'] = to
	msg['Subject'] = subject
	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(user, pwd)
		server.sendmail(user, to, msg.as_string())
		server.close()
	except:
		print("failed")

def get_day(day, month, year):
	base = 'https://www.timeanddate.com/date/weekday.html?'
	base = base + "day=" + str(day)
	base = base + "&month=" + str(month)
	base = base + "&year=" + str(year)

	page = BeautifulSoup(urllib2.urlopen(base), 'html.parser')

	#class results
	#id dayOfWeek
	day =  page.find("span", {"id":"dayOfWeek"})
	day = re.findall(r'(?<=>).*(?=<)', str(day))[0]
	return day

def last_monday():
	timeline= {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
	#get dates
	date = datetime.datetime.now().date()
	dayofweek = get_day(date.day, date.month, date.year)
	lastmonday = dayofweek
	#t = timedelta(days=-1)
	date = date + timedelta(days= (0-timeline[dayofweek]))
	#print "last Monday was on " + str(date)
	return date

def next_monday():
	timeline= {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
	#get dates
	date = datetime.datetime.now().date()
	dayofweek = get_day(date.day, date.month, date.year)
	nextmonday = dayofweek
	date = date + timedelta(days=(7-timeline[dayofweek]))
	#print "next Monday is on " + str(date)	
	return date

def get_week_schedule():
	days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
	text = ""
	#get last monday
	text = text + "This week:\n\n"
	mon = last_monday()
	#https://www.bbc.co.uk/schedules/p00fzl7j/2017/12/27/
	for x in range(2):
		if x==1: 
			text = text + "===============================================\n"
			text = text + "Next week:\n\n"
			mon = next_monday()
		
		for i in range(5):

			if mon.month < 10:
				url = "https://www.bbc.co.uk/schedules/p00fzl7j/"+ str(mon.year) + "/0" + str(mon.month)
			else:
				url = "https://www.bbc.co.uk/schedules/p00fzl7j/"+ str(mon.year) + "/" + str(mon.month)
			if mon.day < 10:
				url = url + "/0" + str(mon.day) + "/"
			else:
				url = url + "/" + str(mon.day) + "/"

			mon = mon + timedelta(days=+1)
			try:
				soup = BeautifulSoup((urllib2.urlopen(url)), 'html.parser')

				#<span class="timezone--time">18:30</span>
				
				programs = soup.find("li", {"id":"evening"})
				for program in programs.findAll("li"):
					if '<span class="timezone--time">18:30</span>' in str(program):
						#text = text + str(program)
						titles = re.findall(r'(?<=property="name">).*?(?=</span)', str(program))
						
						title = titles[0]
						subtitle = titles[1]
						link = ""
						if "#play" in str(program):
							link = re.findall(r'(?<=resource=").*?#play(?=")', str(program))[0]
						else:
							link = re.findall(r'(?<=href=")https://.*?(?=")', str(program))[0]

						#text = text + "<b>"+title + "</b>"
						text = text + days[i] + "\n"
						text = text + title + "\n"
						text = text + subtitle + "\n"
						text = text + link + "\n\n"
			except:
				text = text + "No information yet"
	return text

text = get_week_schedule()
print text
outro = """
"""
recipients = ['recipient1', 'recipient2']
for recipient in recipients:
	send_email('email@gmail.com', 'emailpassword', recipient, 'Weekly radio update', text)
#email to meeeee
#get day of week
#from https://www.timeanddate.com/date/weekday.html?day=11&month=5&year=2012
