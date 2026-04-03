from icrawler.builtin import BingImageCrawler
import os

# Define your categories
categories = ['cat', 'dog', 'car']
number_of_images = 100

for category in categories:
    print(f"--- Starting download for: {category} ---")

    # Create a folder for the category if it doesn't exist
    if not os.path.exists(category):
        os.makedirs(category)

    # Initialize the crawler (Bing is usually the most stable for scraping)
    bing_crawler = BingImageCrawler(downloader_threads=4, storage={'root_dir': category})

    # Start crawling
    bing_crawler.crawl(keyword=category, max_num=number_of_images)

print("Finished downloading 150 images!")