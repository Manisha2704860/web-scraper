# web-scraper
#What it does

This script is a web scraper that extracts the top headlines from the Times of India news website and saves them to a text file.

#How it works

1. The script sends a GET request to the Times of India news website to retrieve the HTML content of the page.
2. It then uses BeautifulSoup to parse the HTML content and find the headline elements on the page.
3. The script extracts the text of the top 5 headlines and stores them in a list.
4. It prints the headlines to the console and saves them to a text file named timesofindia_top_headlines.txt.

# Why it was built
This script was likely built to:

1. Automate news collection: The script automates the process of collecting news headlines from the Times of India website, saving time and effort.
2. Monitor news trends: By extracting headlines, the script can help monitor news trends and track important stories.
3. Save news for later: The script saves the headlines to a text file, allowing users to refer to them later.

However, it's worth noting that the script has some redundant code, where it manually prints and saves the headlines instead of using the scraped headlines. A more efficient version of the script would use the scraped headlines for both printing and saving.
