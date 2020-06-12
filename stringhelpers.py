#String Helpers

from settings import * # Importing everything from settings.py
import re # Importing the regular expression

#Get correct url format (lowercase with dashes)
def dashes(seriesName):
	#return re.sub("\s+", "-", seriesName.lower()) #Replace whitespaces with dash (-)
	return "-".join(seriesName.split(" ")).lower()


#Adding trailing zeros to the page number
def add_zero(pageNum):
	digits = len(pageNum) # if page is 455, len(pageNum) -> 3
	zeros = "0" * (ESTIMATED_MAX_DIGITS - digits)
	return zeros + pageNum


#Assemble the page url (the website's html)
def get_page_url(seriesName, episodeNum, pageNum=1):
	 # http://mangareader.net/black-clover/500/1
	return PROVIDER + dashes(seriesName + "/" + str(episodeNum) + "/" + str(pageNum))

# Assemble the path to the folder to download the episode
def get_download_path(seriesName, episodeNum):
	# "C:/Users/MADUKOMA BLESSED C/Pictures/Manga/Black Clover/500/"
	return LOCAL_Path + seriesName + "/" + episodeNum + "/"