#! /usr/bin/env python2.6
import sys
from zipfsong import Album, Song

if __name__=='__main__':
        # un modo per fare le main testabili è questo
        # 
        # import sys
        # import yourlogic
        # 
        # if __name__ == '__main__':
        #     yourlogic.main(sys.stdin, sys.stdout)
        #
	lines = []
	for line in sys.stdin:
		lines.append(line)

	[ totalTracks, selectTracks ] = map(int, lines[0].split())
		
	album = Album(totalTracks, selectTracks)
	for index in range(0, album.totalSongs):
		[ playcount, title ] = lines[index+1].split()
		album.append(index + 1, playcount, title)

	for song in album.extract():
		print song


		

		
