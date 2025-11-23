import requests

# Define the API endpoint
url = 'https://jsonplaceholder.typicode.com/posts'

# Define the data to send
new_post = {
    "title": "My New Post",
    "body": "This is the content of my new post.",
    "userId": 1
}

# Make a POST request
response = requests.post(url, json=new_post)

# Check the status code
if response.status_code == 201:
    # Parse JSON response
    created_post = response.json()
    print("Created Post:")
    print(f"Title: {created_post['title']}")
    print(f"Body: {created_post['body']}")
else:
    print(f"Failed to create post. Status code: {response.status_code}")
