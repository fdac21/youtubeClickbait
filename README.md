# youtubeClickbait
You must have a file in the .gitignore file called `api.py`
In this file your google api key must be placed as
```
api_key = "your api key"
```
This is so the google api calls can be made.
**Please do not upload any api key to this repository.**


### Mac/Linux
```
pip install google-api-python-client
```

### Windows
Youtube video titles and descriptions have the possibility to contain non latin characters and emojis. Because of this if you are using a windows machine your enivronment must support the reading and writing of these characters.
One possible option
https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab

```
pip install google-api-python-client
```
## Supported Python Versions
Python 3.6, 3.7, 3.8, 3.9, and 3.10
This is limited by google-api

## Current usage
```
python getData.py [option] [num of loops] [pageToken]
```

### Current option arguments
* `popular`    searches through current most popular Videos
    * [ number of loops ]
        * must be between 1 and 4000
    * [ pageToken ]
        * can be `none` or any `pageToken` given by Youtube api

Each call to popular will pull at least 5 videos.
Returns amount of videos added to the file and the next page token.
The next page token can be used to call the next argument.


### Example arguments
```
python getData.py popular 3 none
```

```
python getData.py popular 1 CA8QAA
```

### Data
Video information is currently stored in [youtubeVideos.txt](youtubeVideos.txt)