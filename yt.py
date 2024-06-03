from pytube import YouTube

# Create a YouTube object
video_url = "https://youtu.be/j6pyGYiF254?si=8NvIYfNOBDILUIwK"
yt = YouTube(video_url)

# Choose the stream (resolution) you want to download
stream = yt.streams.get_lowest_resolution()

# Download the video to a specified path
download_path = "C:/Users/Mayuresh/Desktop/Python"
stream.download(output_path=download_path)

print("Video downloaded successfully!")
