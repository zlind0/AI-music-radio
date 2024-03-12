# AI classical music radio

I came across this idea even before the emergence of LLMs while I was listening to ClassicFM. It feels awesome that the host tells you knowledge of the song to be played such as the background, music form and composition technique of that song. With some degree of expectation, enjoying classical music becomes much more pleasurable, instead of being lengthy and boring. This is even true for me who possibly suffers from ADHD.

Then, LLMs brought this idea possible. And I am implementing it now.

This project is at early development. Now it's a simple PoC. It's a very simple python script to announce you the song to be played. Then, it will use ChatGLM's API to get a text of some of the basic knowledge and use macOS say command to read it loud, as if there is really a host speaking. Then the whole song would be played as usual. Theoreatically, it supports all the music players that exposes music metadata to the macOS.

Thanks for "nowplaying-cli" project to make it possible to control music play and fetch what is being played.

## Usage

Currently this just works as how I prefer. There are not many things that you can customize. There will be some in the future.

There are some essential steps to make it running.

1. Make sure you are running it on macOS

2. Put your ChatGLM APIKEY into apikey.txt

3. Set a voice that pleases you in "Settings > Accessibility > Spoken Content > System voice"

4. Install essential python requirements 

```
python3 -m pip install -r requirements.txt
```

5. build nowplaying-cli

```
make
```

5. Start music playing

6. Start this application. Your music player will be paused and a dummy welcome will be spoken. When the music play progress is about to end, the host will introduce you the next piece, just as the radio host. Enjoy!

```
python3 run.py
```

## TODO

Though it works right now, here are some of the most urgent things that I am concerned right now. 

1. Most urgently, `say` command produces an annoying sound after all the contents are spoken.

2. AI needs time to return response, something should be done to minimize the silence gap to make everything sounds smooth. There are 2 ways to solve it: a) know what will be played in advance (requires more API). b) add some transition sounds (like applause) in this silence gap.

3. Support for more AI models options, such as local models, other AI platforms (OpenAI), etc...

4. Support for some other AI Text-to-Voice models. Would it be nice if Genshin character 可莉 is speaking?!

5. Bring this idea to more platforms and integrate with some open source music player so that the general public can use it.

6. Add support to random local file playing and streaming, then it will be a real Internet radio. In this scenario, AI can even select which song to play next, so that the random playlist can have a fine flavour.

# nowplaying-cli

Below is how to install nowplaying-cli

nowplaying-cli is a macOS command-line utility for retrieving currently playing media, and simulating media actions.

Use nowplaying-cli to get song information and play/pause your media through an easy to use CLI!

**Disclaimer:** nowplaying-cli uses private frameworks, which may cause it to break with future macOS software updates.

**Tested and working on:** 
- Ventura 13.1, 13.2, 13.3, 13.6

## Installation

### Homebrew

You can install nowplaying-cli using [Homebrew](https://brew.sh/).
```bash
brew install nowplaying-cli
```

### Build from source

Clone the repository and run `make` to build the binary. You can then move the binary to your desired location.
```bash
make
mv nowplaying-cli ~/.local/bin
```

## Usage
`nowplaying-cli <cmd>`
| command | description |
| --- | --- |
| get [propName1 propName2 ... ] | get now playing media properties | 
| get-raw | get all non-nil now playing media properties in dictionary format |
| play | play the currently playing media regardless of current state |
| pause | pause the currently playing media regardless of current state |
| togglePlayPause | toggle play/pause based on current state |
| next | skip to next track | 
| previous | go to previous track |

## Examples
![screenshot of examples in terminal](screenshots/examples.png)

## Available properties
| native  |  nowplaying-cli |
|---|---|
| kMRMediaRemoteNowPlayingInfoTotalDiscCount | totalDiscCount |
|  kMRMediaRemoteNowPlayingInfoShuffleMode | shuffleMode
|  kMRMediaRemoteNowPlayingInfoTrackNumber | trackNumber
|  kMRMediaRemoteNowPlayingInfoDuration | duration
|  kMRMediaRemoteNowPlayingInfoRepeatMode | repeatMode
|  kMRMediaRemoteNowPlayingInfoTitle | title
|  kMRMediaRemoteNowPlayingInfoPlaybackRate | playbackRate | 
|  kMRMediaRemoteNowPlayingInfoArtworkData | artworkData |
|  kMRMediaRemoteNowPlayingInfoArtworkDataWidth | artworkDataWidth |
|  kMRMediaRemoteNowPlayingInfoArtworkDataHeight | artworkDataHeight |
|  kMRMediaRemoteNowPlayingInfoAlbum | album |
|  kMRMediaRemoteNowPlayingInfoTotalQueueCount | totalQueueCount | 
|  kMRMediaRemoteNowPlayingInfoArtworkMIMEType | artworkMIMEType
|  kMRMediaRemoteNowPlayingInfoMediaType | mediaType |
|  kMRMediaRemoteNowPlayingInfoDiscNumber | discNumber |
|  kMRMediaRemoteNowPlayingInfoTimestamp | timestamp |
|  kMRMediaRemoteNowPlayingInfoGenre | genre |
|  kMRMediaRemoteNowPlayingInfoQueueIndex | queueIndex |
|  kMRMediaRemoteNowPlayingInfoArtist | artist |
|  kMRMediaRemoteNowPlayingInfoDefaultPlaybackRate | defaultPlaybackRate |
|  kMRMediaRemoteNowPlayingInfoElapsedTime | elapsedTime |
|  kMRMediaRemoteNowPlayingInfoTotalTrackCount | totalTrackCount |
|  kMRMediaRemoteNowPlayingInfoIsMusicApp | isMusicApp |
|  kMRMediaRemoteNowPlayingInfoUniqueIdentifier | uniqueIdentifier |
