from pytube import YouTube
def download_youtube_video(video_url: str, ):
    # Создание объекта YouTube
    yt = YouTube(video_url)
    # Получение первого доступного формата видео
    video = yt.streams.filter(progressive=True).desc().first()
    # Загрузка видео
    video.download("videos/")


def download_youtube_audio(video_url: str, ):
    # Создание объекта YouTube
    yt = YouTube(video_url)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download("audios/")
