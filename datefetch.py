import re
import datetime
import urllib
def fetch():
	data = urllib.urlopen("http://nist.time.gov/timezone.cgi?Eastern/d/-5").read()
	m = re.findall(".*?[A-Za-z]*?, ([A-Za-z]*? [0-9]{1,2}, [0-9]{4})",data)
	if m != []:
		today = datetime.datetime.strptime(m[0],"%B %d, %Y")
	else:
		today = datetime.datetime.now()

	return today
