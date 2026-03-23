'''import time
from memory_profiler import profile
from ll import LinkedList, Node
from songs import SONGS


@profile
def load_playlist(song_tuples):
    playlist = LinkedList()

    for title, artist, album in song_tuples:
        node = Node(title, artist, album)
        playlist.insert_at_end(node)

    return playlist


def main():
    start_time = time.perf_counter()
    playlist = load_playlist(SONGS)
    end_time = time.perf_counter()

    print("\nPlaylist cargada correctamente.")
    print("Total de canciones:", len(playlist))
    print(f"Tiempo de carga: {end_time - start_time:.6f} segundos")
    print(f"Uso de memoria: {playlist.__sizeof__()} bytes")


if __name__ == "__main__":
    main()
    '''