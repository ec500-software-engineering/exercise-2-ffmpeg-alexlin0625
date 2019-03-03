# EC500 Exercise 2 - FFmpeg
This exercise is to utilize theading and ffmpeg to covert videos concurrently in 480p and 720p quality. This application ran and tested on a macbook air. This macbook air contains 4 CPU cores, the following pictures showed the CPU usage when the ffmpeg is compiled and all cores of CPU are running concurrently. 

## run 
After downloading all the videos files and codes, simply run main.py. The videos are automatically generated into the output video file which include both 480p and 720p. The output videos are also tagged with clearly names to clarify the videos are either 480p or 720p. 

I also implemented testing(pytest.py) to estimate if the video conversion and compare the durations of original video to all output videos to ensure no data loss during the conversion

## CPU_cores
![alt text](https://github.com/ec500-software-engineering/exercise-2-ffmpeg-alexlin0625/blob/master/CPU_cores.png)

## CPU_Usage 
![alt text](https://github.com/ec500-software-engineering/exercise-2-ffmpeg-alexlin0625/blob/master/CPU%20usage.png)
