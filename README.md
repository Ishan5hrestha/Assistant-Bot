# Assistant Bot
I love python. It's easy, has lots of packages readily available and I can focus more on what I want to achieve rather than how to achieve.  
Still, making new environment, remembering the names of my most frequently used module, creating files on every new project i start is time consuming, boring and ugly.  
  
  Hence here comes my Assistant bot. This is voice commanded as well as text based.  
## Installation
```
pip install -r requirements.txt
```
## Run
```
python base.py
```
Or configure assistant.bat to your assistant location and use it to load up.  
I personally have put it in windows startup application folder so that it starts automatically.

## Usage
- Press UP arrow to start talking.
- Or use Text to type

## Files
Inside functions/saves/ you can see various files:
- **command.txt**
  - left column is the action performed when any of the right column work is recognized.
  - & sign means both left and right word must be said together to be true. For eg: say "start specific" instead of "start" or "specific".
- **open_type.txt**
  - leftmost is the word to be spoken.
  - & has same meaning as above.
  - center is how to start. run means write on run and start means write on cmd key
  - right is the keyword to type for action
- **python_imports.txt**
  - for python project setup
  - left is package name
  - mid is how to install on terminal
  - right is what to write on editor after installation completes
- **specific_apps.txt**
  - left is which python file to run on what word of the right

## Trailer
