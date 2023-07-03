import os
from dotenv import load_dotenv
import googleapiclient.discovery
import spacy

load_dotenv()

apikey = os.getenv('YOUTUBE_API_KEY')

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=apikey)
nlp = spacy.load('en_core_web_sm')

def format_view_count(count):
    if count >= 1_000_000:
        return f"{count // 1_000_000}m"
    elif count >= 1_000:
        return f"{count // 1_000}k"
    else:
        return str(count)

def analyze_video_data(query):
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='snippet',
        maxResults=10
    ).execute()

    channel_names = []
    view_counts = []
    video_titles = []
    view_sum = 0
    view_num = 0

    for search_result in search_response.get('items', []):
        video_id = search_result['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        video_response = youtube.videos().list(
            id=video_id,
            part='snippet,statistics'
        ).execute()

        channel_name = video_response['items'][0]['snippet']['channelTitle']
        channel_names.append(channel_name)

        if 'statistics' in video_response['items'][0]:
            view_count = int(video_response['items'][0]['statistics']['viewCount'])
            view_sum = view_sum + view_count
            view_num = view_num + 1
        else:
            view_count = 0
        view_counts.append(view_count)

        video_title = video_response['items'][0]['snippet']['title']
        video_titles.append(video_title)

#        print(f"Channel Name: {channel_name}")
#        print(f"View Count: {format_view_count(view_count)}")
#        print(f"URL: {video_url}")
#        print()

    # Perform NLP analysis on video titles
    entities = []
    for doc in nlp.pipe(video_titles):
        proper_nouns = [token.text for token in doc if token.pos_ == 'PROPN']
        entities.extend(proper_nouns)

    # Get the most common proper nouns and their frequencies
    entity_frequencies = {}
    for entity in entities:
        entity_frequencies[entity] = entity_frequencies.get(entity, 0) + 1

    # Sort the entities by frequency in descending order
    sorted_entities = sorted(entity_frequencies.items(), key=lambda x: x[1], reverse=True)

    avg_views = view_sum / view_num

    return sorted_entities[:3], avg_views


#data = input("Search something to analyze: ")
#analyze_video_data(data)