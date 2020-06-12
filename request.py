from stringhelpers import *     # importing everything from the stringhelpers.py
from settings import *          # importing everything from settings.py
import requests                 # Library to make HTTP requests
import shutil                   # Does advanced file operations
import os                       # To operate with directories


# Send a reuquest via HTTP
def send_request(url, binary=False):
    try:  # Incase of connection errors
        request = requests.get(url, stream=binary)  # HTTP request
    except:  # What to do if something bad happens
        print(REQUEST_Error)
        exit()

    # If request is successful, send request
    return request

# Check to see if the episode has not been released


def not_released(seriesName, episodeNumber):
    manga_url = get_page_url(seriesName, episodeNumber)
    html = send_request(manga_url).text

    return NOT_Released_Text in html

# Download the image to the hard drive
def download_img(url, download_path, pageNum):
    # Create the download path if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Assemble the page's image file path
    img_name = add_zero(str(pageNum)) + FILE_Ext
    img_path = download_path + img_name

    # Make a request but get binary data
    # Also, wait until it finishes downoading
    request = send_request(url, True)

    # Create a binary file with img extension
    # Get the decoded contente of the image tream
    # Copy them into the image path we constructed
    with open(img_path, 'wb') as file_path:
        request.raw.decode_content = True
        shutil.copyfileobj(request.raw, file_path)
    print(DOWNLOADING_Message + str(pageNum))