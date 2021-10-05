import os
from googleapiclient.discovery import build

# for linux and mac add the folowing to the file. Replace value with the YouTube API key
#./bash_profile
# export YTC_API_KEY="value"

# for Windows add an environment variable
# user variable -> NEW -> Variable name  = YTC_API_KEY
#                      -> Variable value = ***YouTube api key***
api_key = os.environ.get('YTC_API_KEY')

# https://developers.google.com/youtube/v3
# https://github.com/googleapis/google-api-python-client
# pip install google-api-python-client      suggested vitrual client use

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    
    youtubeV3 = build('youtube', 'v3', developerKey=api_key)

    # limit of 10,000 request per day 
    # test on small amounts first before getting full data set
    request = youtubeV3.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        maxResults=20,
        regionCode="US"
    )
    response = request.execute()

    # needs better printing
    print(response)

if __name__ == "__main__":
    main()