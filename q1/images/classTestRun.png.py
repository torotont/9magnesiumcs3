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


if __name__ == "__main__":
    song1 = ListeningStatistics("Pwede Ka Ba?", True, 23, 4.58)
    song2 = ListeningStatistics("Kay Ganda Mo", False, 10, 3.14)

    print("--- BEFORE ---")
    print("Song 1:", song1.displayStats())
    print("Song 2:", song2.displayStats())

    print("\nPerforming action on Song 1 (playSong)...\n")
    song1.playSong()

    print("--- AFTER ---")
    print("Song 1:", song1.displayStats())
    print("Song 2:", song2.displayStats())