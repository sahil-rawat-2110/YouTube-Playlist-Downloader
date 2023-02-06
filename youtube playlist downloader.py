from pytube import YouTube                                     # import YouTube submodule/class from pytube module
from pytube import Playlist                                    # import Playlist submodule/class from pytube module

link = input("Enter YouTube Video or Playlist URL: ")  

# Check URl is playlist or a single video
x = "playlist" in link                                        

print("..............Downloading Start...........")


# for download Playlist 
if (x == True) :                                               

    yt_playlist = Playlist(link)

    for video in yt_playlist.videos:
        video.streams.get_highest_resolution().download()
        print("Video Downloaded: ", video.title)

    print("\nAll videos are downloaded.")

    
# for download a single video
else:                                                         

    youtube_1 = YouTube(link)

    print("Title : ", youtube_1.title)                                     # print title of video
 
    print("Thumbnail : ", youtube_1.thumbnail_url)                         # print thumbnail of video

    print("Subtitle/Caption: ", youtube_1.captions)

    print("Subtitle/Caption in only English language: ", youtube_1.captions.get_by_language_code('en'))


    videos = youtube_1.streams.all()                           # All Format streams 

    # videos = youtube_1.streams.filter(only_audio=True)       # only audio streams
    # videos = youtube_1.streams.filter(only_video=True)       # only video streams

    vid = list(enumerate(videos))                              # list of all streams 
    for i in vid: 
        print(i)
    print()

    strm = int(input("Enter index of quality for downloading : "))                              
    videos[strm].download()

    print("Your video is downloaded")