import sys
from fileData import Video, read_file_data
from fileData import FileData
from apiCalls import most_popular, single_id
from textAnalysis import titleAnalysis, print_titles_dict, print_titles_option
from otherDataSets import combine_mj
from convertCsv import convertCsv


def main():
    fd = FileData()         # our file data
    mjfd = FileData()       # file data from added data set
    titles_dict = {}        # dictonary of single words in titles to ids

    try:
        with open('youtubeVideos.txt', mode='r+', encoding="utf-8") as f:
            read_file_data(f, fd)
            print("file: {} finished reading\n".format(f.name))
            print("usage: [option] [num of loops] [pageToken]")
            print("example usage: popular 1-40 none")
            command = ''
        
            while input != 'Q':
                command = input("command: ")
                command = command.split()

                if len(command) == 3:
                    option = command[0]
                    if (option == 'popular'):        #popular [num] [token]     try to insert all the most popular videos
                        numOfLoops = int(command[1])
                        pageToken = command[2]
                        if (numOfLoops > 0) and (numOfLoops <= 40):
                            most_popular(numOfLoops, pageToken, f, fd)
                        else:
                            print("number of loops must be between 1 and 40")
                    elif (option == 'print'):
                        value1 = command[1]
                        value2 = command[2]
                        if (value1 == 'titles') and (value2 == 'dict'):
                            print_titles_dict(titles_dict)
                        elif (value1 == 'titles') and (value2 in titles_dict):
                            print_titles_option(titles_dict, value2)
                        elif (value1 == 'titles'):
                            print("{} not in titles dict".format(value2))
                        else:
                            print('not valid command')
                    else:
                        print('option: ' + option + ' not available')
                    


                elif len(command) == 2:
                    option = command[0] 
                    if (option == 'single_id'):        #single_id [id]      try to insert single id
                        user_id = str(command[1])
                        single_id(user_id, f, fd)
                    elif (option == 'print'):
                        fd_var = command[1]
                        if(fd_var == 'ids'):           #print ids           print list of all ids in file
                            fd.print_dict_ids()
                        elif fd_var == 'amount':       #print amount        print number of ids in file
                            print("number of videos: {}".format(len(fd.videos_dict)))
                        elif fd_var in fd.videos_dict:
                            v = fd.videos_dict[fd_var]
                            v.print_video()
                        else:
                            print("not valid command")
                    elif (option == 'analysis'):      #analysis titles      this doesn't work right now
                        analysis_type = command[1]
                        if(analysis_type == 'titles'):
                            titleAnalysis(fd, titles_dict)
                        else:
                            print("not valid command")
                    elif (option == 'merge'):        #merge [data set]      merges the data set with our data file
                        data_set = str(command[1])
                        if(data_set == 'mj'):        
                            combine_mj(f, fd, mjfd)
                        else:
                            print("not valid command")
                    elif (option == 'convert'):
                        con_type = command[1]
                        if(con_type == 'csv'):
                            convertCsv(fd)
                    else:
                        print("not valid command")
                else:
                    print("not valid command")
    except IOError:
        print('Data file cant be opened')
    except EOFError as e:
        del fd
        del mjfd
        sys.exit()

    sys.exit()

if __name__ == "__main__":
    main()