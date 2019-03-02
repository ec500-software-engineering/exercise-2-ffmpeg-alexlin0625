from math import isclose
import main as run
import os
import queue


def test_duration():
    fnin = "test.mp4"
    fnout1 = "test.mp4_480p.mp4"
    fnout2 = "test.mp4_720p.mp4"
    
    # get the time duration for original video
    orig_meta = run.ffprobe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])
    
    # time duration for both 480p/720p video that are generated
    duration_480 = float(meta_480['streams'][0]['duration'])
    duration_720 = float(meta_720['streams'][0]['duration'])
    
    # get meta for 480p/720p videos
    meta_480 = run.ffprobe(fnout1)
    meta_720 = run.ffprobe(fnout2)
    
    # compare each 480p/720p video with the original
    assert orig_duration == isclose(orig_duration, duration_480, abs_tol=1)
    assert orig_duration == isclose(orig_duration, duration_720, abs_tol=1)
    print('successful')


if __name__ == '__main__':
    q = queue.Queue()
    format = [".mp4"]
    # get video from tsetVideo and put into queue
    for file in os.listdir("testVideo"):
        filename, a = os.path.splitext(file)
        if a in format:
            q.put(file)
    
    # covert videos and run test_duration for result
    while not q.empty():
        filename = q.get()
    run.convert480_test(filename)
    run.convert720_test(filename)
    test_duration()

