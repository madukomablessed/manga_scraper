from bs4 import BeautifulSoup as bs # The source code parser
from settings import *              # importing everything from settings.py
from request import *               # importing everything from request.py
from stringhelpers import *         # importing everything from the stringhelpers.py
import sys

def download_episode(seriesName, episodeNum):
	current_page = INTIAL_PAGE
	download_path = get_download_path(seriesName, episodeNum)

	# Exit function if episode hasn't been released
	if not_released(seriesName, episodeNum):
		print(NOT_RELEASED_Message)
		return None

	while True: # Loops through the pages until the last one
		page_url = get_page_url(seriesName, episodeNum, current_page)
		request = send_request(page_url)
		raw_html = request.text

		# If the page or manga doesn't exist...
		if request.status_code != 200 or not len(raw_html):
			print(DOESNT_Exist if not len(raw_html) else SUCCESS_Message)
			break #Exits the while loop

		# Scrap the html to find the page's image link
		parsed_html = bs(raw_html, "html.parser")
		img_url = parsed_html.find("img", { "id": "img" }).get("src")

		# Save the page's image in the download path
		download_img(img_url, download_path, current_page)

		# Change the current page to the next one
		current_page = current_page + 1

# Run the main function and pass the 2nd and 3rd arguments
download_episode(sys.argv[1], sys.argv[2])