class Song:
    
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
   
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
       
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)
       
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
       
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)
   
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.add(artist)
   
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
   
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
