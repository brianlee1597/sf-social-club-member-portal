import requests
import json

URL = "https://api.partiful.com/getGuests"

HEADERS = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjhkMjUwZDIyYTkzODVmYzQ4NDJhYTU2YWJhZjUzZmU5NDcxNmVjNTQiLCJ0eXAiOiJKV1QifQ.eyJwaWN0dXJlIjoiaHR0cHM6Ly9maXJlYmFzZXN0b3JhZ2UuZ29vZ2xlYXBpcy5jb20vdjAvYi9nZXRwYXJ0aWZ1bC5hcHBzcG90LmNvbS9vL3Byb2ZpbGVJbWFnZXMlMkZmZTEyZTMxNC04NDNhLTQ3N2QtYmY_YWx0PW1lZGlhJnRva2VuPWE4ZTFjMTg3LWU1NjUtNDRkYy1hNTQ0LTYzNjRlYWE5NTE2MiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9nZXRwYXJ0aWZ1bCIsImF1ZCI6ImdldHBhcnRpZnVsIiwiYXV0aF90aW1lIjoxNzM2MDMyMTU4LCJ1c2VyX2lkIjoiR09rTmhyQXVTQ2hBMnVWR0U4QnpMS3V1NWI4MiIsInN1YiI6IkdPa05ockF1U0NoQTJ1VkdFOEJ6TEt1dTViODIiLCJpYXQiOjE3MzkzOTM5MjYsImV4cCI6MTczOTM5NzUyNiwicGhvbmVfbnVtYmVyIjoiKzE0NDM0NjczNjg3IiwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJwaG9uZSI6WyIrMTQ0MzQ2NzM2ODciXX0sInNpZ25faW5fcHJvdmlkZXIiOiJjdXN0b20ifX0.uO8EK7KI4hsPWK66VIPY6qA87iixoTyFc0YktsRyLKFSotaDukfwvlK1a3zWu9MrpjD7vdthHGWzMRX_GjG_DW7ZckWr0D53tIU5Zi2Xim8x4pLagtwOU8lpof5paTqzH9fdMVEYHf2fVzQkgOb7Ar8QVCSH2GWnnnfU5D4mAD_NipNWEDRk87o1_4Tk9INhtJ5MLNzvKBjWQJUjqtnkDMlvvRhysoTU7p5dCtqkMQzZY_kYmX-ucT0Y6rTgsuNI4lM3ylX_ef2XdT47nuFmg6BS5MUEk8K0RhwpNXPShrVWzeY5xZ8znmoyAqWzm3L4mP9v4Dzobtc1JBEeq4i2DA',
  'content-type': 'application/json',
  'origin': 'https://partiful.com',
  'priority': 'u=1, i',
  'referer': 'https://partiful.com/',
  'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}

def extract_event_data(event_id):
    payload = json.dumps({
  "data": {
    "params": {
      "eventId": event_id,
      "includeInvitedGuests": True
    },
    "paging": {
      "cursor": None,
      "maxResults": 500
    },
    "userId": "GOkNhrAuSChA2uVGE8BzLKuu5b82"
  }
})
    response = requests.request("POST", URL, headers=HEADERS, data=payload)

    print(response.text)