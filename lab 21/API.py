
# Define the API endpoint
import requests
url = 'https://jsonplaceholder.typicode.com/posts'

# Make a GET request
response = requests.get(url)

# Check the status code
if response.status_code == 200:
    # Parse JSON response
    posts = response.json()
    print("Fetched Posts:")
    for post in posts[:5]:  # Print the first 5 posts
        print(f"Title: {post['title']}")
else:
    print(f"Failed to retrieve posts. Status code: {response.status_code}")
