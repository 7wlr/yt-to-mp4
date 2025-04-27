import yt_dlp
import os

def download_video(url, output_path='downloads'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        if not filename.endswith('.mp4'):
            filename = filename.rsplit('.', 1)[0] + '.mp4'
    print(f"Downloaded: {filename}")
    return filename

if __name__ == "__main__":
    video_url = input("Please enter the YouTube video URL: ")
    download_video(video_url)
