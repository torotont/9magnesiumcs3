class MediaTrack:
    """Parent class: general info shared by any playable media item."""

    def __init__(self, title, duration):
        self.title = title
        self._duration = duration

    def getDuration(self):
        return self._duration

    def displayInfo(self):
        return f"Title: {self.title} | Duration: {self._duration}s"


class ListeningStatistics(MediaTrack):
    """Child class: IS-A MediaTrack, adds playback-tracking behavior."""

    def __init__(self, title, loopSong, replays, duration):
        super().__init__(title, duration)   # reuse parent's init
        self.loopSong = loopSong
        self.__replays = replays

    def playSong(self):
        self.__replays += 1
        print(f"Now playing '{self.title}'... replay count updated.")

    def changeSong(self, title):
        self.title = title
        self.__replays = 0
        print(f"Switched to new song: '{self.title}'. Replay count reset.")

    def displayStats(self):
        loop_status = "On" if self.loopSong else "Off"
        base_info = self.displayInfo()          # reused from MediaTrack
        return f"{base_info} | Loop: {loop_status} | Replays: {self.__replays}"

    def get_replays(self):
        return self.__replays

    def applyEqualizer(self, equalizer):
        """Dependency (USES-A): borrows an Equalizer temporarily, doesn't own it."""
        effect = equalizer.boostBass()
        print(f"Applying equalizer to '{self.title}': {effect}")


class Equalizer:
    """A tool that ListeningStatistics depends on temporarily, but never stores."""

    def boostBass(self):
        return "bass boosted +6dB"


class Artist:
    """Aggregation: holds ListeningStatistics objects that existed before joining it."""

    def __init__(self, artistName):
        self.artistName = artistName
        self.songs = []   # aggregated references, not owned/created by Artist

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
    print("--- TEST 1: INHERITANCE ---")
    song1 = ListeningStatistics("Pwede Ka Ba?", True, 23, 4.58)
    print("Using parent method displayInfo():", song1.displayInfo())
    print("Using child method displayStats(): ", song1.displayStats())

    print("\n--- TEST 2: AGGREGATION ---")
    song2 = ListeningStatistics("Kay Ganda Mo", False, 10, 3.14)
    song3 = ListeningStatistics("Minamahal", True, 15, 3.50)
    print("Songs already exist independently before joining an artist:")
    print("  -", song2.displayInfo())
    print("  -", song3.displayInfo())

    artist = Artist("Frank Ely")
    artist.addSong(song1)
    artist.addSong(song2)
    artist.addSong(song3)

    print("\nArtist's discography:")
    artist.displayDiscography()

    top_song = artist.mostReplayedSong()
    print(f"\nMost replayed song: {top_song.title} ({top_song.get_replays()} replays)")

    print("\n--- TEST 3: DEPENDENCY ---")
    eq = Equalizer()
    song1.applyEqualizer(eq)
    print("song1.__dict__ keys:", list(vars(song1).keys()))
