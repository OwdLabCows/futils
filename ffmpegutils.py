import ffmpeg


def convert_mp4_to_wav(mp4path: str, wavpath: str):
    stream = ffmpeg.input(mp4path)
    stream = ffmpeg.output(stream, wavpath)
    ffmpeg.run(stream)
