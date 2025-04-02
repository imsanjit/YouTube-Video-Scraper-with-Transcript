# Installing required libraries
%%capture
!pip install google-api-python-client
!pip install youtube-transcript-api

#Importing required libraries
from apiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi as yta
import pandas as pd
import datetime
import json
import csv
from google.colab import files

# taking input from user for youtube api key and youtube channel id

api_key = 'AIzaSyCzV48CWFgrAgEUTay1h6xh0EsDXRh8STY' # Add your "youtube api v3"api key here (sangya)
channel_id = 'UCnBVMVxqw6TOYdwPBlIJXyQ' #channel id needs to be fetch

# Get upload playlist id

yt = build('youtube', 'v3', developerKey= api_key)

req = yt.channels().list(id= channel_id, part= 'contentDetails').execute()


def get_transcript(id):
    try:
        data = yta.get_transcript(id)
        data_json = json.dumps(list(data), indent=2)
        json_object = json.loads(data_json)

        final_data = ''

        try:
            for val in json_object:
                for key, value in val.items():
                    if key == "text":
                        final_data += value + " "
        except:
            final_data = 'Something went worng'

        return final_data

    except:
        return 'Transcript not available'


def get_channel_videos(channel_id):
    # get Uploads playlist id
    res = yt.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while 1:
        res = yt.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break

    return videos

# scraping videos from youtube upload playlist

videos = get_channel_videos(channel_id)
print(f'\nTotal number of video are: {len(videos)}')

# get all video from youtube channel in json file

all_Yt_Details = []

for i, video in enumerate(videos):
    print(f'Scraping video number: {i+1}')
    video_id = str(video['snippet']['resourceId']['videoId'])
   
    ytDetails = {
        "Sno." : i+1,
        "Video_ID" : f" {video_id}",
        "URL" : f"https://www.youtube.com/watch?v={video['snippet']['resourceId']['videoId']}",
        "Title" : video['snippet']['title'],
        "Description" : video['snippet']['description'],
        "Thumbnails" : video['snippet']['thumbnails']['default']['url'],
        "Published_Date": video['snippet']['publishedAt'].split("T")[0],
        "Transcript" : get_transcript(video_id)
    }
    all_Yt_Details.append(ytDetails)

with open('youtube_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_Yt_Details, f, ensure_ascii=False, indent=4)
files.download("youtube_data.json")

## get all video from youtube channel in excel file

data = pd.read_json('/content/youtube_data.json')
data.to_csv('youtube_data.csv', index= False, encoding='utf-8')
files.download("youtube_data.csv")

print('\n\nFile Downloaded')
