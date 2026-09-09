# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
Describe any changes made to your original class.

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| title | string | Public | 	The song title needs to be freely read and displayed by other parts of the program. |
| loopSong | boolean | Public | The loop toggle is meant to be switched on/off directly, so it stays accessible. |
| replays | int | private | The replay count should only ever increase through the class's own logic. |
| songLength | float | private | A song's length is a fixed property of the audio file. It shouldn't be edited. |

## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)

## Python Implementation
[View Python Source](classImplementation.py)

## Test Run
![Test Run](images/classTestRun.png)

## Object Diagram
![Object Diagram](images/objectDiagram.png)

## Analysis

## Class Diagram
