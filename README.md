# <img src="https://upload.wikimedia.org/wikipedia/commons/e/ef/Youtube_logo.png" alt="Image of youtube logo" width="32" height="22"> youtube-search
*by Jacob Field*

## Description
Uses the [YouTube Data API v3](https://developers.google.com/youtube/v3) to search YouTube and return the top 5 results

Takes a string as input and returns each video's view count, like count, and like-to-view ratio

## How To Use
1. Create a **Google Developer** project with the **YouTube Data API v3** using this setup guide:
[youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)

2. In python, install the **google-api-python-client** using pip:
```python
pip install google-api-python-client
```

3. In `main.py`, change the variable `API_KEY` to your **API key**:
```python
API_KEY = 'your key here'
```

## Example Output
```
Please enter what you would like to search for: mark rober

Searching YouTube for mark rober...

Result #1: Testing If You Can Blow Your Own Sail
24,621,311 views	 834,353 likes	 3.3887% of viewers liked

Result #2: MrBeast Pranked With Falling Bottles
30,065,342 views	 1,872,938 likes	 6.2296% of viewers liked

Result #3: I NEED 1 MORE SUBSCRIBER!
149,242,872 views	 9,536,167 likes	 6.3897% of viewers liked

Result #4: How To GUARANTEE Your Team Wins
48,061,551 views	 2,612,331 likes	 5.4354% of viewers liked

Result #5: MrBeast vs Electric Shock Jenga
13,638,491 views	 749,285 likes	 5.4939% of viewers liked
```
