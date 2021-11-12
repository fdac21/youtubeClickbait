import sys
from fileData import read_file_data
from fileData import FileData
from apiCalls import most_popular
from apiCalls import single_id
from textAnalysis import titleAnalysis


def main():
    fd = FileData
    try:
        with open('youtubeVideos2.txt', mode='r+', encoding="utf-8") as f:
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
                    if (option == 'popular'):
                        numOfLoops = int(command[1])
                        pageToken = command[2]
                        if (numOfLoops > 0) and (numOfLoops < 40):
                            most_popular(numOfLoops, pageToken, f, fd)
                        else:
                            print("number of loops must be between 1 and 40")
                    else:
                        print('option: ' + option + ' not available')


                elif len(command) == 2:
                    option = command[0]
                    if (option == 'single_id'):
                        user_id = str(command[1])
                        single_id(user_id, f, fd)
                    elif (option == 'print'):
                        fd_var = command[1]
                        if(fd_var == 'videos_dict'):
                            fd.print_dict_ids(fd)
                    elif (option == 'analysis'):
                        analysis_type = command[1]
                        if(analysis_type == 'titles'):
                            titleAnalysis(fd)
                    else:
                        print("not valid command")
                else:
                    print("not valid command")
    except IOError:
        print('File cant be opened')
    except EOFError as e:
        sys.exit()


if __name__ == "__main__":
    main()