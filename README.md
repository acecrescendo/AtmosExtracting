# Dolby Atmos Track Extracting
Mass extract ATMOS surround tracks from M4As into individual WAV files using FFmpeg and a simple python script.

# Prerequisites
## Python 3.14 or higher
Go to https://python.org/downloads and download the installer for your OS

## FFmpeg

### MacOS
</p> Install Homebrew at the website https://brew.sh </p>
</p> Run the command </p>
<code> brew install ffmpeg </code>

### Windows
</p> Download FFmpeg from https://www.gyan.dev/ffmpeg/builds (ffmpeg-release-full.zip) </p>
</p> Extract it and move the folder to: </p> 
<code> C:\ffmpeg </code>
</p> Add FFmpeg to PATH by pressing Win + R and type 'sysdm.cpl' </p>
</p> Go to Advanced → Environment Variables </p>
</p> Inside, edit Path and add </p>
<code> C:\ffmpeg\bin </code>
</p> Verify using the command </p> 
<code> ffmpeg -version </code>

### Linux
<p> Install FFmpeg using your distro’s package manager. </p>
<p> <strong> Ubuntu / Debian </strong> </p>
<p> <code> sudo apt update </code> </p>
<p> <code> sudo apt install ffmpeg </code> </p>
<p> ---------- </p>
<p> <strong> Arch </strong> </p>
<code> sudo pacman -S ffmpeg </code>
<p> ---------- </p>
<p> <strong> Fedora </strong> </p>
<code> sudo dnf install ffmpeg </code>
<p> ---------- </p>
<p> Verify installation </p>
<code> ffmpeg -version </code>

# Guide
<p> Install the python script from the repository, then put the script in a memorable location </p>
<p> ---------- </p>
<p> Open up your terminal or command prompt and enter the folder of your script </p>
<code> cd Location/Of/Script </code>
<p> Then open the scipt using the command </p>
<code> python3 AcesAtmosExtraction.py </code>
<p> Follow the scripts instructions </p>
