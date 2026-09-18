# Advanced Class Relationships

## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)

## Existing System Description
The system originally had two classes which were ListeningStatistics and SongArtist. This activity will refactor ListeningStatistics to inherit shared media properties from a new parent class. This will also formalize the Artist–Song connection as an aggregation while adding a temporary dependency on an Equalizer.

## Inheritance Relationship
Parent: MediaTrack
Child: ListeningStatistics
Explanation: MediaTrack will hold the general properties that any playable media item would have. This includes title and duration. ListeningStatistics IS-A MediaTrack because a song is a type of media item.

## Inheritance UML
[Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation
Relationship: Aggregation — Song Artist aggregates ListeningStatistics
Explanation: Song objects are created independently. Since the songs could exist and be used even if the Artist object were removed, the part does not depend on the whole for its existence, which defines aggregation.

## Advanced UML Diagram
[Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
[Test](images/advancedTestRun.png)

## Object Diagram
[Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:

### 1. Why did you choose your inheritance relationship?
ListeningStatistics is a type of MediaTrack because every song has a title and a duration before anything about listening behavior is even tracked. This makes MediaTrack the parent captures that general concept, while ListeningStatistics specializes it into something that also tracks loops and replays.

#### 2. How did inheritance reduce duplicate code?*
Before the refactor, title and length logic lived only inside ListeningStatistics. Now MediaTrack defines title, duration, and displayInfo() once, and ListeningStatistics reuses them through super().__init__() and by calling self.displayInfo() inside displayStats(), instead of re-declaring that logic.

### 3. Why is your HAS-A relationship Composition or Aggregation?
It's aggregation because the Artist and its songs have independent cycles. Songs are represented on their own and simply passed into addSong(). The artist never creates them internally the way composition would require, and deleting the artist wouldn't delete the songs.

### 4. What is the difference between Association from Part III and the advanced relationship you implemented?
The Part III association said Artist manages songs gnereally. Aggregation is a more precise version of that same HAS-A idea. It specifically states that the contained objects can exist independently of the container, which the Part III diagram didn't clarify.

### 5. How does your design follow the DRY principle?**
Instead of repeating title and duration-handling code in every media-related class, I will use the shared logic in MediaTrack. Any class that IS-A MediaTrack automatically gets it through inheritance.
