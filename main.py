import pytube 
def download_video(video_url, output_path):
    try:
        # Create a YouTube object with the video URL
        yt = pytube.YouTube(video_url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video to the specified output path
        stream.download(output_path)
        
        print(f"Video '{yt.title}' downloaded successfully to '{output_path}'")
    except Exception as e:
        print(f"An error occurred: {e}") 
        

