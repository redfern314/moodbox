# in Playlist.play
if mixer.music.get_busy():
    self.stop()

# in Playlist
def stop(self):
    mixer.music.fadeout(500)

# in run
if not queue.empty():
    newmood = queue.get()
    # send light command?
    playlist.selectPlaylist(newmood)
    playlist.selectSong()
elif not mixer.music.get_busy():
    playlist.selectSong()