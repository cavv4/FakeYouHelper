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
pip install -r requirements.txt
```
Download a VOSK model for your language from [here](https://alphacephei.com/vosk/models)  
and extract it's content into a "`model`" folder (same directory as "`fakeyou.py`") like this:  
![VOSK model folder structure](https://cavv.it/assets/images/2022-10-22%2015_01_51-Window.png)  
### Usage
Put all your wave files into an "`input`" folder (same directory as "`fakeyou.py`")  
![Wave files folder structure](https://cavv.it/assets/images/2022-10-22%2015_10_26-input.png)  
Start the script
```
python fakeyou.py
```
That's it, now wait