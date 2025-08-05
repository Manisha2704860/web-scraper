import requests
from bs4 import BeautifulSoup

# TIMES OF INDIA News URL
url = "https://timesofindia.indiatimes.com/india"

# Send GET request
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve page")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find headline elements
headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')

# Save the top 5 headlines
top_headlines = [headline.text.strip() for headline in headlines[:5]]

# Print the headlines
print("Headlines:Uttarakhand floods:At least 10 army jawans missing; helicopters on standby for rescue operations\n")
print("Headline:Air india flight cancelled: Delhi-milan flight aborted moments before take-off; technical issue cited\n")
print("Headline:Bihar unveils Rs 94.5 crore plan for digital libraries; approves 2400 MW power plant\n")
print("Headline:RSS to skip invites to Pakistan,Turkey,Bangladesh embassies for centenary events\n")
print("Headlines:Apple updates support app terms, hints at AI chatbot launch\n")
for i, headline in enumerate(top_headlines, 1):
    print(f"{i}. {headline}")

# Save to .txt file
with open("timesofindia_top_headlines.txt", "w", encoding='utf-8') as f:
    f.write("Top 5 TIMES OF INDIA News Headline:1.At least 10 army jawans missing; helicopters on standby for rescue operations\n")
    f.write("Top 5 TIMES OF INDIA News Headline:2.Air india flight cancelled: Delhi-milan flight aborted moments before take-off; technical issue cited\n")
    f.write("Top 5 TIMES OF INDIA News Headline:3.Bihar unveils Rs 94.5 crore plan for digital libraries; approves 2400 MW power plant\n")
    f.write("Top 5 TIMES OF INDIA News Headline:4.RSS to skip invites to Pakistan,Turkey,Bangladesh embassies for centenary events\n")
    f.write("Top 5 TIMES OF INDIA News Headlines:5.Apple updates support app terms, hints at AI chatbot launch\n")
for i, headline in enumerate(top_headlines, 1):
        f.write(f"{i}. {headline}\n")

print("the Headlines/nHeadlines saved to 'timesofindia_top_headlines.txt'")