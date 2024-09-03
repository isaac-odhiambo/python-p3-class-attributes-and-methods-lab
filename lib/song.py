class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = set()
    artists = set()
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update counts and sets
        Song.count += 1
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0
        Song.genre_count[genre] += 1
        Song.genres.add(genre)
        
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0
        Song.artist_count[artist] += 1
        Song.artists.add(artist)
    
    @classmethod
    def reset(cls):
        cls.count = 0
        cls.genre_count = {}
        cls.artist_count = {}
        cls.genres = set()
        cls.artists = set()
