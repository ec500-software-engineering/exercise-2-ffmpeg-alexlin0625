import json
import subprocess
import queue
import threading
import os.path


def convert480(filename):
    """
    convert the videos in input_videos to 480p
    """
    # if filename + "_480p.mp4" in os.listdir("outputVideos"):
    #     os.remove("outputVideos/" + filename + "_720p.mp4")

    subprocess.check_output(
        "ffmpeg -loglevel panic -i inputVideos/" + filename + " -vf scale=-1:480 -b:v 1048576 -r 30 outputVideos/" + filename + "_480p.mp4",
        shell=True)
    print("video converted to 480p")


def convert720(filename):
    """
    convert the videos in input_videos to 720p
    """
    # if filename + "_720p.mp4" in os.listdir("outputVideos"):
    #     os.remove("outputVideos/" + filename + "_720p.mp4")

    subprocess.check_output(
        "ffmpeg  -loglevel panic -i inputVideos/" + filename + " -vf scale=-1:720 -b:v 2097152 -r 30 outputVideos/" + filename + "_720p.mp4",
        shell=True)
    print("video converted to 720p")


def convert480_test(filename):
    """
    convert the test video in input_videos to 480p
    """
    # if filename + "_480p.mp4" in os.listdir("outputVideos"):
    #     os.remove("outputVideos/" + filename + "_720p.mp4")

    subprocess.check_output(
        "ffmpeg -loglevel panic -i testVideo/" + filename + " -vf scale=-1:480 -b:v 1048576 -r 30 outputVideos/" + filename + "_480p.mp4",
        shell=True)
    print("video converted to 480p")


def convert720_test(filename):
    """
    convert the test video in input_videos to 720p
    """
    # if filename + "_720p.mp4" in os.listdir("outputVideos"):
    #     os.remove("outputVideos/" + filename + "_720p.mp4")

    subprocess.check_output(
        "ffmpeg  -loglevel panic -i testVideo/" + filename + " -vf scale=-1:720 -b:v 2097152 -r 30 outputVideos/" + filename + "_720p.mp4",
        shell=True)
    print("video converted to 720p")

def ffprobe(filename) -> dict:
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                        '-print_format', 'json',
                                        '-show_streams',
                                        '-show_format',
                                        filename], universal_newlines=True)
    return json.loads(meta)


if __name__ == "__main__":
    threads = []
    format = ['.mp4']
    q = queue.Queue()

    for file in os.listdir("inputVideos"):
        filename,a = os.path.splitext(file)
        if a in format:
            q.put(file)

    while not q.empty():
        filename = q.get()

        t = threading.Thread(target=convert480, args=(filename,))
        t1 = threading.Thread(target=convert720, args=(filename,))
        threads.append(t)
        threads.append(t1)
        t.daemon = True
        t1.daemon = True
        t.start()
        t1.start()

    for thread in threads:
        thread.join()

