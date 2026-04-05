import os
from datetime import date
from icrawler.builtin import GoogleImageCrawler, BaiduImageCrawler

# 1. Keyword Expansion: Define specific sub-categories for better variance
dataset_map = {
    'cat': ['kitten', 'cat playing', 'siamese cat photo', 'sleeping cat', 'funny cat photo', 'cat art'],
    'dog': ['funny dog photo', 'puppy', 'dog sleeping', 'dog playing', 'pup', 'dog art', 'doggo'],
    'car': ['modern SUV', 'classic sports car', 'electric vehicle', 'old car', 'tesla', 'mercedes', 'toyota corolla'],
    'amogus': ['among us character', 'amogus meme', 'red among us', 'abobus', 'among us art', 'sus meme', 'jerma amogus'],
    'bee': ['honey bee', 'bumblebee', 'bee flying', 'bee art', 'bee 3d model'],
    'atom': ['atom model diagram', 'molecular structure', 'hydrogen atom', 'atom', 'atom photo', 'atom model']
}

# 2. Settings
images_per_subquery = 50  # Lower number per query avoids bot detection
for main_category, sub_keywords in dataset_map.items():
    print(f"\n==== Gathering: {main_category} ====")

    if not os.path.exists(main_category):
        os.makedirs(main_category)

    for sub_key in sub_keywords:
        print(f"--- Crawling: {sub_key} ---")

        # Initialize Bing Crawler
        bing_crawler = GoogleImageCrawler(
            downloader_threads=2,
            storage={'root_dir': main_category}
        )

        bing_filters = dict(
            type='photo',
            size='large'
        )

        bing_crawler.crawl(
            keyword=sub_key,
            max_num=images_per_subquery,
            filters=bing_filters
        )

        # Optional: Baidu for extra volume
        baidu_crawler = BaiduImageCrawler(
            downloader_threads=2,
            storage={'root_dir': main_category}
        )
        baidu_crawler.crawl(keyword=sub_key, max_num=10)

print("\nDataset gathering complete!")