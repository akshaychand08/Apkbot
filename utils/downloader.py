import yt_dlp
import asyncio

def get_video_formats(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info.get("formats", [])
        except Exception:
            return []

async def download_video_by_format(url, format_id=None):
    ydl_opts = {
        'format': format_id if format_id else 'bestvideo+bestaudio/best',
        'outtmpl': 'temp/%(id)s.%(ext)s',
        'quiet': True,
        'noplaylist': True,
        'merge_output_format': 'mp4'
    }
    result = []

    def download():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return [ydl.prepare_filename(info)]

    loop = asyncio.get_event_loop()
    try:
        result = await loop.run_in_executor(None, download)
    except Exception as e:
        result = [f"❌ Error: {str(e)}"]

    return result
  
