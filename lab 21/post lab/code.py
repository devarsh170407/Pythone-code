import requests

class SimpleAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_posts(self, limit=5):
        """Fetch a list of posts."""
        url = f"{self.base_url}/posts"
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            print("Fetched Posts:")
            for post in posts[:limit]:
                print(f"Title: {post['title']}")
        else:
            print(f"Failed to retrieve posts. Status code: {response.status_code}")

    def create_post(self, title, body, user_id):
        """Create a new post."""
        url = f"{self.base_url}/posts"
        new_post = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(url, json=new_post)

        if response.status_code == 201:
            created_post = response.json()
            print("Created Post:")
            print(f"Title: {created_post['title']}")
            print(f"Body: {created_post['body']}")
        else:
            print(f"Failed to create post. Status code: {response.status_code}")

    def fetch_post_by_id(self, post_id):
        """Fetch a single post by its ID, with error handling."""
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.get(url)

        if response.status_code == 200:
            post = response.json()
            print("Fetched Post:", post)
        else:
            print(f"Error: {response.status_code} - {response.reason}")


# Using the API Client
api_client = SimpleAPIClient("https://jsonplaceholder.typicode.com")
api_client.fetch_posts()
api_client.create_post("My New Post", "This is the content of my new post.", 1)
api_client.fetch_post_by_id(1000)
