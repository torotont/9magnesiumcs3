class ListeningStatistics:
    def __init__(self, title, loopSong, replays, songLength):
        self.title = title
        self.loopSong = loopSong
        self.__replays = replays
        self.__songLength = songLength

    def playSong(self):
        self.__replays += 1
        print(f"Now playing '{self.title}'... replay count updated.")

    def changeSong(self, title):
        self.title = title
        self.__replays = 0
        print(f"Switched to new song: '{self.title}'. Replay count reset.")

    def displayStats(self):
        loop_status = "On" if self.loopSong else "Off"
        return (f"Title: {self.title} | Loop: {loop_status} | "
                f"Replays: {self.__replays} | Length: {self.__songLength}s")

    def get_replays(self):
        return self.__replays


class Artist:
    def __init__(self, artistName):
        self.artistName = artistName
        self.songs = [] 

    def addSong(self, song_reference):
        self.songs.append(song_reference)
        print(f"'{song_reference.title}' added to {self.artistName}'s discography.")

    def mostReplayedSong(self):
        if not self.songs:
            return None
        return max(self.songs, key=lambda song: song.get_replays())

    def displayDiscography(self):
        print(f"{self.artistName}'s discography:")
        for song in self.songs:
            print("  -", song.displayStats())


if __name__ == "__main__":
  
    print("--- BEFORE RELATIONSHIP ---")
    artist = Artist("Frank Ely")
    song1 = ListeningStatistics("Pwede Ka Ba?", True, 23, 4.58)
    song2 = ListeningStatistics("Kay Ganda Mo", False, 10, 3.14)
    song3 = ListeningStatistics("Minamahal", True, 15, 3.50)

    print(f"Artist created: {artist.artistName}")
    print(f"Songs owned so far: {len(artist.songs)}")
    print("Songs created (still independent):")
    print("  -", song1.displayStats())
    print("  -", song2.displayStats())
    print("  -", song3.displayStats())

  print("\n--- BUILDING RELATIONSHIP ---")
    print("Assigning songs to the artist...")
    artist.addSong(song1)
    artist.addSong(song2)
    artist.addSong(song3)

   
    print("\n--- AFTER RELATIONSHIP ---")
    print(f"{artist.artistName} now owns {len(artist.songs)} song(s).")
    print("\nRelated object(s):")
    artist.displayDiscography()

    top_song = artist.mostReplayedSong()
    print(f"\nMost replayed song: {top_song.title} ({top_song.get_replays()} replays)")

    song1.playSong()

    print("  After playing Pwede Ka Ba? directly, the artist's list shows:")
    print("  -", artist.songs[0].displayStats())
