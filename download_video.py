from pytube import YouTube

url = "https://www.youtube.com/watch?v=your_video_id"


def download_youtube_video(video_url: str, ):
    # Создание объекта YouTube
    yt = YouTube(video_url)
    # Получение первого доступного формата видео
    video = yt.streams.first()
    audio = yt.streams.get_audio_only()
    # Загрузка видео
    video.download()
    audio.download()


download_youtube_video("https://www.youtube.com/watch?v=TpIrJmVwfBo")
