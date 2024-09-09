# examples
songs = ["song1:100", "song2:500", "song3:175"]
animations = ["anm1:350", "anm2:25", "anm3:50"]

def solve(songs, animations):
    # songs and animations are in the format ["name:duration",...]
    # i wanted to solve in O(len(songs)) + O(len(animations))
    # i want to return an array of strings in this format "animation_name:number_of_replays"
    # in the output array each element should correspond to the respective order of song in songs
    # the order of both array matter if an animation fits for a song i.e s_len % a_len == 0
    # then we have found the first fit animation and wont traverse ahead.