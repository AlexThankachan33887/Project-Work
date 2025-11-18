import os
import csv

def get_files(path):
    return os.listdir(path)

def get_urls(path):
    urls = []
    for file in get_files(path):
        with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
            urls.append(f.read())
    return urls

def write_urls(path):
    if not os.path.exists(path):
        raise ValueError("Invalid path")
        
    urls = get_urls(path)
    with open('urls.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['url'])
        for url in urls:
            writer.writerow([url])

# Example usage with a valid local directory path
write_urls(r'C:\Users\alext\internship\urls.csv')