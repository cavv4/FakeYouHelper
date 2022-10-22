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
### Usage
Put all your wave files into an "`input`" folder (it must be in the same folder as "`fakeyou.py`")
  
Start the script
```
python fakeyou.py
```
That's it, now wait