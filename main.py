from googleapiclient.discovery import build

API_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def youtube_search(search_string):
    print(f'\nSearching YouTube for {search_string}...\n')

    youtube = build('youtube', 'v3', developerKey=API_KEY)
    search_response = youtube.search().list(q=search_string, part='id,snippet', type='video', maxResults=5).execute()

    result = 1

    for video in search_response['items']:
        video_ID = video['id']['videoId']
        video_data = youtube.videos().list(part='statistics', id=video_ID).execute()
        video_stats = video_data['items'][0]['statistics']

        views = int(video_stats['viewCount'])
        likes = int(video_stats['likeCount'])
        view_like_ratio = likes/views

        print(f"Result #{result}: {video['snippet']['title']}")
        print(f"{views:,} views\t {likes:,} likes\t {round(view_like_ratio * 100, 4)}% of viewers liked\n")

        result += 1


if __name__ == '__main__':
    search_string = input('Please enter what you would like to search for: ')

    try:
        youtube_search(search_string)
    except:
        print(f'[!] Error searching for {search_string} with API-KEY: {API_KEY}')
