# SG4 - Understanding Classes and Objects 


## Class Name ListeningStatistics


## Class Description ListeningStatistics represents the data obtained from any song in your playlist.

## Properties 
| Property | Data Type | Description | 
|---|---|---| 
| title | string | Tile of the song | 
| loopSong | boolean | Determines if current song is being looped | 
| replays | int | Number of replays of the song | 
| songLength | float | Duration of the song | 

## Methods
| Method | Description |
|---|---| 
| playSong() | Plays the selected song |
| changeSong(title: string) | Skips to the next song | 
| displayStats() | Displays the listening statistics for the selected song |

## Class Diagram
| ListeningStatistics |
|------|
| title : string |
| loopSong : boolean |
| replays : int |
| songLength : float |
|---|
| playSong() |
| changeSong(title : string) |
| displayStats() |
|------|

## Design Explanation

### Why did you choose this class? 
I chose ListeningStatistics because as someone who listens to music daily, I get curious about how many times I listen to specific songs.
### Which property is the most important? Why? 
title is the most important property. It tells you the song you’re listening to right now so it’s easier for people to not get confused with similar sounding songs.
### Which method is the most useful? Why? 
playSong() is the most useful method, obviously you can’t listen to a song if it isn’t playing which is why it’s the most important despite being simple.

