# TORRENT SEARCH GUI

For all those who gets irritated with all the ads from torrent sites for just to search the favourite movie, games, applications and hell alot many things. Just phase through all the pop ups and gets your loving content in front of you by downloading this.

For windows: [torrent search](https://github.com/karu007/TORRENT_SEARCH/blob/master/python/TorrentSearch.exe?raw=true)

## For developers 

Well, if you're the developer you must be here with the keen interest of knowing the code and running on your machine. Here are the steps to follow after you clone this project:-

### Step 0: Install python 3.x on your machine (if not installed)
 - 0.1 Go to [python download](https://www.python.org/downloads) and download the version of python that suits for your machine
 - 0.2 Install python executable

### Step 1: Create your virtual environment for this project
 - 1.1: Open terminal/command prompt in root/adminstrator mode.
 - 1.2: Type the following commands in sequence:
   - 1.2.1: `py -m pip install --upgrade pip`
   - 1.2.2: `py -m pip install --user virtualenv`
 - 1.3: Go to our project python folder and open terminal/command prompt
 - 1.4: Type the following commands in sequence:
   - 1.3.1: `py -m virtualenv torrent_search`
   - 1.3.2: `.\torrent_search\Scripts\activate ` This command is just to ensure there are no errors
   - 1.3.3: `deactivate`
 - 1.5: Close terminal/command prompt

### Step 2: Install the modules that are required to run this project
  - 2.1: Open terminal/command prompt in our project python path { example: ..\python> }
  - 2.2: Type the following commands in sequence:
    - 2.2.1: `.\torrent_search\Scripts\activate`
    - 2.2.2: `pip install -r requirements.txt`
  - 2.3: Close terminal/command prompt

### Step 3: Run the python file on your terminal/command prompt
  - 3.1: Open windows terminal/command prompt in our project path { example: ..\python> }
  - 3.2: Type the following commands in sequence:
    - 3.2.1: `.\torrent_search\Scripts\activate`
    - 3.2.2: `python src/torrent_search.py`
