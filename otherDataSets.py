import sys
from apiCalls import single_id
from fileData import read_mj_file

# Data from data set of Trending Youtube Videos
# https://mitchelljolly.com/
# https://www.kaggle.com/datasnaek/youtube-new?select=USvideos.csv

def combine_mj(f, fd, mjfd):

    try:
        with open('USvideos.csv', mode='r', encoding="utf-8") as mj:
            read_mj_file(mj, mjfd)
            print("file: {} finished reading\n".format(mj.name))
    except IOError:
        print('USvideos.csv cant be opened')
    except EOFError as e:
        sys.exit()
    i = 0

    if f.closed:
        print("its closed")

    for id in mjfd.videos_dict:
        if id not in fd.videos_dict:
            if id not in fd.not_added:
                #do api call on mj ids
                single_id(id, f, fd)
        