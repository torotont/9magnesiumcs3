# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: Listening Statistics 

Description: It represents a song and tracks its playback behavior.

## New Related Class
Class: SongArtist

Description: It represents the musician or band who creates the songs.

## Association
Relationship: SongArtist owns ListeningStatistics

Explanation: Every song is created by an artist, so an Artist object needs to store and manage the ListeningStatistics objects that make up their discography.

## Multiplicity
Multiplicity: 1 : 0..*

Explanation: One artist can own zero or more songs, while each song in this system belongs to a single artist.

## UML Class Relationship Diagram
[Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
[Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
[Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
The SongArtist class owns a group of ListeningStatistics objects. It stores each song created by that artist and can perform actions across the collection, such as displaying the full discography or finding the most replayed song.
### What multiplicity did you choose and why?
I chose a one-to-many multiplicity because a single artist can have any number of songs while each song will be tied to only one artist.
### How did you implement the relationship in Python?
The relationship is implemented through the self.songs list inside the SongArtist class. When addSong() is called, the ListeningStatistics object is appended to this list.
### Why did you store an object reference instead of copying its data?
I stored the ListeningStatistics object instead of just copying its data, so that the artist's discography always reflects the song's current state.
### If your relationship uses many, why is a list appropriate?
A list is appropriate because an artist's number of songs isn't fixed and can grow as new songs are released.
