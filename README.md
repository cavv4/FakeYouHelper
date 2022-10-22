# FakeYouHelper
 Conversion and Speech-To-Text script to help with creation of FakeYou datasets

### What does this do?
1. Resamples all wave files to 22050Hz mono (FakeYou standard)
2. Transcribes text from them and generates a list to use for AI training
### Setup
Clone this repository
```
git clone https://github.com/cavv4/FakeYouHelper.git
```
Change directory
```
cd FakeYouHelper
```
Install requirements
```
pip3 install -r requirements.txt
```
Install ffmpeg  
  
Linux:
```
sudo apt install ffmpeg
```
  
Windows:
1. Download build from [here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z)
2. Open the archive and extract the contents of `ffmpeg-[version]-essentials_build` in `C:\ffmpeg\`
3. Go to your `Computer properties` and open `Advanced system settings`
4. Click on `Environment Variables`
5. Find the `PATH` (or `Path`) variable in the bottom window, select it and click on `Edit...`
6. Click on `New` and paste in `C:\ffmpeg\bin`
7. Click `OK` and you are done
  
Download a VOSK model for your language from [here](https://alphacephei.com/vosk/models)  
and extract its content into a `model` folder like this:  
![VOSK model folder structure](https://cavv.it/assets/images/2022-10-22%2015_01_51-Window.png)  
### Usage
Put all your wave files into an `input` folder  
![Wave files folder structure](https://cavv.it/assets/images/2022-10-22%2015_10_26-input.png)  
Start the script
```
python3 fakeyou.py
```
That's it, now wait