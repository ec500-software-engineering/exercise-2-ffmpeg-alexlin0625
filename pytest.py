from math import isclose
import main as run
import os
import queue


def test_duration():
    fnin = "test.mp4"
    fnout1 = "test.mp4_480p.mp4"
    fnout2 = "test.mp4_720p.mp4"

    orig_meta = run.ffprobe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    meta_480 = run.ffprobe(fnout1)
    meta_720 = run.ffprobe(fnout2)

    duration_480 = float(meta_480['streams'][0]['duration'])
    duration_720 = float(meta_720['streams'][0]['duration'])

    assert orig_duration == isclose(orig_duration, duration_480, abs_tol=1)
    assert orig_duration == isclose(orig_duration, duration_720, abs_tol=1)
    print('successful')


if __name__ == '__main__':
    q = queue.Queue()
    format = [".mp4"]
    for file in os.listdir("testVideo"):
        filename, a = os.path.splitext(file)
        if a in format:
            q.put(file)

    while not q.empty():
        filename = q.get()
    run.convert480_test(filename)
    run.convert720_test(filename)
    test_duration()

