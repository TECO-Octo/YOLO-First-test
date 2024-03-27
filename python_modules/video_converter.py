import ffmpeg


# TODO: (put in the archive) YOLO can save video directly in mp4 format now
def convert_video(input_path, output_path):
    """
        Converts a video file to a specified format using FFmpeg.

        This function attempts to convert a video file from one format to another using the FFmpeg library.
        It takes an input file path and an output file path as arguments. The conversion process is set to
        use 'libx264' as the video codec and 'aac' as the audio codec for the output file, which are common
        codecs compatible with many devices and platforms.

        Parameters:
        - input_path (str): The path to the input video file that needs to be converted.
        - output_path (str): The path where the converted video file will be saved.

        The function uses the FFmpeg library to read the input video file, apply the specified codecs during
        the conversion process, and write the output to the given path. If the conversion fails for any reason,
        an error message is printed to the console indicating the issue.

        Exceptions:
        - ffmpeg.Error: Catches and handles any errors raised by the FFmpeg library during the conversion process.
                        The error details are printed, including the input path and the error message.

        Note:
        Ensure that FFmpeg is correctly installed and accessible in your environment path before using this function.
        """
    try:
        stream = ffmpeg.input(input_path)
        stream = ffmpeg.output(stream, output_path, vcodec='libx264', acodec='aac')
        ffmpeg.run(stream)
    except ffmpeg.Error as e:
        print(f"Error converting file {input_path}: {e}")
