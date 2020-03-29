# Scraping-comments-of-all-videos-of-a-Youtube-playlist
Webscraping comments on YouTube videos of a playlist using Beautiful Soup and Selenium Webdriver 

First we make a youtube playlist of all the videos whose comments we want to scrape.

Next we substitute the youtube playlist link provided in the code with the link to our playlist. The program uses Beautiful Soup 4 to first scrape the links of all the videos in the playlist's main page hence fetching the links of all the videos whose comments we want.

Then the code opens up Chrome and uses Selenium to scroll through the video's comments. The problem with Youtube comments is lazy loading which requires us to scroll repeatedly downwards to load more comments and this responsibility is handled by Selenium. The extent to which the comments are to be fetched can be adjusted in the code. The comments are scraped and stored in an Excel file and with the index of the video (the video's position in the playlist).

