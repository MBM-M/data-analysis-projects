import urllib.request

# Download the fcc-forum-pageviews.csv file
url = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/master/fcc-forum-pageviews.csv'
filename = 'fcc-forum-pageviews.csv'

print(f"Downloading {filename}...")
try:
    urllib.request.urlretrieve(url, filename)
    print(f"Successfully downloaded {filename}")
except Exception as e:
    print(f"Error downloading file: {e}")
    print("\nAlternatively, you can manually download the file from:")
    print(url)
