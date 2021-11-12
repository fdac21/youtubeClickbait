class FileData:
    searchedTokens = set()
    videos_dict = {}
    new_videos = set()
    new_tokens = set()
    def __init__(self):
        self.searchedTokens = set()
        self.videos_dict = {}
        self.new_videos = set()
        self.new_tokens = set()

    def print_dict_ids(self):
        for k, v in self.videos_dict.items():
            print("id: {}".format(k))
        print("videos_dict size: {}".format(len(self.videos_dict)))

    def titles(id, self):
        v = self.videos_dict[id]
        return v.title
            
class Video:
    def __init__(self, videoId, title, channelId, categoryId,
                channelTitle, description, duration, viewCount,
                likeCount, dislikeCount, favoriteCount,
                commentCount):
        self.videoId = videoId
        self.title = title
        self.channelId = channelId
        self.categoryId = categoryId
        self.channelTitle = channelTitle
        self.description = description
        self.duration = duration
        self.viewCount = viewCount
        self.likeCount = likeCount
        self.dislikeCount = dislikeCount
        self.favoriteCount = favoriteCount
        self.commentCount = commentCount
    
    def print_video(self):
        print("id: " + self.videoId)
        print("title: " + self.title)
        print("channelId: " + self.channelId)
        print("categoryId: " + self.categoryId)
        print("channelTitle: " + self.channelTitle)
        print("description: " + self.description)
        print("duration: " + self.duration)
        #print("dimension: " + self.dimension)
        #print("definition: " + self.definition)
        #print("caption: " + self.caption)
        #print("licensedContent: " + self.licensedContent)
        #print("regionRestriction: " + self.regionRestriction)
        #print("contentRating: " + self.contentRating)
        #print("projection: " + self.projection)
        print("viewCount: " + self.viewCount)
        print("likeCount: " + self.likeCount)
        print("dislikeCount: " + self.dislikeCount)
        print("favoriteCount: " + self.favoriteCount)
        print("commentCount: " + self.commentCount)

    def write_video(self, f):
            f.write("id: "+ self.videoId + '\n')
            f.write("title: " + str(self.title) + '\n')
            f.write("channelId: " + str(self.channelId) + '\n')
            f.write("categoryId: " + str(self.categoryId) + '\n')
            f.write("channelTitle: " + str(self.channelTitle) + '\n')
            f.write("description: \n")
            f.write(self.description)
            f.write("duration: " + str(self.duration) + '\n')
            f.write("viewCount: " + str(self.viewCount) + '\n')
            f.write("likeCount: " + str(self.likeCount) + '\n')
            f.write("dislikeCount: " + str(self.dislikeCount) + '\n')
            f.write("favoriteCount: " + str(self.favoriteCount) + '\n')
            f.write("commentCount: " + str(self.commentCount) + '\n')
            f.write("\n")
            f.flush()
            print("ADDED VIDEO")
            print("video title: {}\n".format(str(self.title)))



def read_file_data(f, fd):
    for line in f:
        line = line.strip()
        #if the line is not a newline
        if line != '\n':
            #get the id of the data and the value itself
            data = line.split(": ", 1)
            id = data[0]
            if len(data) == 2:
                val = data[1]
            else:
                val = ''
        #if val is not empty read the entry
        if val:
            #read the previously searched pageTokens
            if id == "Searched on pageToken":
                if val != "none":
                    fd.searchedTokens.add(val)
            #read the video
            elif id == "id":
                videoId = val
                title = f.readline().strip().split(": ", 1)
                channelId = f.readline().strip().split(": ", 1)
                categoryId = f.readline().strip().split(": ", 1)
                channelTitle = f.readline().strip().split(": ", 1)
                descId = f.readline()
                if descId == "description: \n":
                    description = ""
                    l = ""
                    while l != "-??end-of-description??-\n":
                        l = f.readline()
                        description += l    
                duration = f.readline().strip().split(": ", 1)
                viewCount = f.readline().strip().split(": ", 1)
                likeCount = f.readline().strip().split(": ", 1)
                dislikeCount = f.readline().strip().split(": ", 1)
                favoriteCount = f.readline().strip().split(": ", 1)
                commentCount = f.readline().strip().split(": ", 1)

                v = Video(videoId, title[1], channelId[1], categoryId[1], channelTitle[1],
                        description[1], duration[1], viewCount[1], likeCount[1] ,dislikeCount[1],
                        favoriteCount[1], commentCount[1])
                #v.print_video()
        
                if videoId not in fd.videos_dict:
                    fd.videos_dict[videoId] = v
