from pytube import YouTube
import threading
import os


class YouTubeDownloaderApp:
    def __init__(self):
        self.yt = None
        self.stream_options = None

    def get_video_info(self, url):
        try:
            yt = YouTube(url)
            self.yt = yt  # Save YouTube object to class attribute for later use
            details = f"Title: {yt.title}\nLength (seconds): {yt.length}\nViews: {yt.views}"
            print(details)
            type_choice = input("Select type of stream:\n1. Video\n2. Audio\nEnter your choice (1 or 2): ")
            print("Searching...")
            if type_choice == '1':
                self.stream_options = yt.streams.filter(type="video")
            elif type_choice == '2':
                self.stream_options = yt.streams.filter(type="audio")
            else:
                print("Invalid choice. Please enter 1 for video or 2 for audio only.")
                return
            print("Available streams:")
            for i, stream in enumerate(self.stream_options, start=1):
                print(f"{i}. {stream}")
            if not self.stream_options:
                print("No stream available.")
            else:
                self.download()
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_video_info_threaded(self, url):
        threading.Thread(target=self.get_video_info, args=(url,)).start()

    def download(self):
        try:
            selection = int(input("Select an option to download: "))
            if selection < 1 or selection > len(self.stream_options):
                print("Invalid selection.")
                return
            stream = self.stream_options[selection - 1]
            download_location = input("Enter download location (e.g., D:\Downloads): ")
            if os.path.isdir(download_location):
                print("Download started...")
                stream.download(download_location)
                print("Downloaded successfully!")
            else:
                print("Invalid download location.")
        except ValueError:
            print("Invalid input for selection.")

        if __name__ == "__main__":
            app = YouTubeDownloaderApp()
            video_url = input("Enter the YouTube video URL: ")
            app.get_video_info_threaded(video_url)
