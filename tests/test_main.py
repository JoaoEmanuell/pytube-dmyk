from pytube import YouTube, Playlist


def test_answer() -> None:

    url_video = r"https://www.youtube.com/watch?v=9bZkp7q19f0"
    url_playlist = (
        r"https://youtube.com/playlist?list=PLYHoqTjX7zMqNKwL28GuWd8AfVTjF5iB0"
    )

    youtube = YouTube(url_video)
    youtube.streams.get_highest_resolution().download()
    youtube.streams.get_lowest_resolution().download()
    youtube.streams.get_audio_only().download()

    playlist = Playlist(url_playlist)
    assert type(playlist) == Playlist
    assert playlist != []
