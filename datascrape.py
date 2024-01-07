import bs4
import urllib.request
import time

base_url = "https://algogene.com/community/post/"

combined_text = ""

for i in range(1, 144):
    link = base_url + str(i)
    retry_attempts = 3
    while retry_attempts > 0:
        try:
            webpage = urllib.request.urlopen(link).read()
            soup = bs4.BeautifulSoup(webpage, "html.parser")
            text = soup.get_text()
            cleaned_text = text.strip()
            combined_text += cleaned_text + "\n"
            print("Processed:", link)
            break  # Break out of the while loop if the link retrieval is successful
        except urllib.error.HTTPError:
            print("HTTP error occurred for link:", link)
            print("Retrying link:", link)
            retry_attempts -= 1
            time.sleep(1)  # Add a delay before retrying the link

# Save the combined text to a file
text_file_path = "data/community_posts.txt"
with open(text_file_path, "w", encoding="utf-8") as f:
    f.write(combined_text)

print("Combined text saved as:", text_file_path)