import random
from ll import LinkedList, Node
from songs import SONGS


def build_playlist(song_tuples):
    playlist = LinkedList()
    for title, artist, album in song_tuples:
        playlist.insert_at_end(Node(title, artist, album))
    return playlist


class PlaylistPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.current = playlist.start
        self.shuffle_enabled = False
        self.original_order = None

    def play(self):
        if self.current is None:
            print("\nLa playlist está vacía.")
            return

        song = self.current.data
        print("\nReproduciendo ahora:")
        print(f"  Título : {song['title']}")
        print(f"  Artista: {song['artist']}")
        print(f"  Álbum  : {song['album']}")

    def next(self):
        if self.current is None:
            print("\nNo hay canción actual.")
            return

        if self.current.next is None:
            print("\nYa estás en la última canción.")
            return

        self.current = self.current.next
        self.play()

    def previous(self):
        if self.current is None:
            print("\nNo hay canción actual.")
            return

        if self.current.prev is None:
            print("\nYa estás en la primera canción.")
            return

        self.current = self.current.prev
        self.play()

    def toggle_shuffle(self):
        if self.shuffle_enabled:
            self.disable_shuffle()
        else:
            self.enable_shuffle()

    def _relink_nodes(self, nodes):
        if not nodes:
            self.playlist.start = None
            self.current = None
            return

        for i, node in enumerate(nodes):
            node.prev = nodes[i - 1] if i > 0 else None
            node.next = nodes[i + 1] if i < len(nodes) - 1 else None

        self.playlist.start = nodes[0]

    def enable_shuffle(self):
        nodes = [node for node in self.playlist]

        if len(nodes) < 2:
            print("\nNo hay suficientes canciones para activar shuffle.")
            return

        current_song = self.current
        self.original_order = nodes[:]

        shuffled_nodes = nodes[:]
        random.shuffle(shuffled_nodes)
        self._relink_nodes(shuffled_nodes)

        self.current = current_song
        self.shuffle_enabled = True

        print("\nShuffle activado.")
        self.show_playlist_preview(limit=5)

    def disable_shuffle(self):
        if self.original_order is None:
            print("\nShuffle ya está desactivado.")
            return

        current_song = self.current
        self._relink_nodes(self.original_order)

        self.current = current_song
        self.shuffle_enabled = False
        self.original_order = None

        print("\nShuffle desactivado.")
        self.show_playlist_preview(limit=5)

    def show_status(self):
        total = len(self.playlist)
        mode = "ON" if self.shuffle_enabled else "OFF"

        print("\n")
        print("        DSA MIDTERM - MUSIC PLAYER BY JIMENA\n")
        print(f"        Total canciones : {total}")
        print(f"        Shuffle         : {mode}")

        if self.current is not None:
            song = self.current.data
            print(f"        Ahora suena     : {song['title']} - {song['artist']}")
        else:
            print("        Ahora suena     : Ninguna")

        print("\n")

    def show_playlist_preview(self, limit=5):
        print("\n        Vista previa de la playlist:\n")

        count = 0
        for node in self.playlist:
            song = node.data
            marker = "->" if node is self.current else "  "
            print(f"        {marker} {count + 1}. {song['title']} - {song['artist']} ({song['album']})")
            count += 1
            if count >= limit:
                break

        remaining = len(self.playlist) - limit
        if remaining > 0:
            print(f"\n        ... y {remaining} canciones más\n")
        else:
            print()

    def menu(self):
        while True:
            self.show_status()

            print("        Opciones:\n")
            print("        P  Play")
            print("        N  Next")
            print("        B  Previous")
            print("        S  Shuffle on/off")
            print("        L  List preview")
            print("        Q  Quit\n")

            choice = input("        Elige una opción: ").strip().lower()

            if choice == "p":
                self.play()
                input("\n        Presiona Enter para continuar...")
            elif choice == "n":
                self.next()
                input("\n        Presiona Enter para continuar...")
            elif choice == "b":
                self.previous()
                input("\n        Presiona Enter para continuar...")
            elif choice == "s":
                self.toggle_shuffle()
                input("\n        Presiona Enter para continuar...")
            elif choice == "l":
                self.show_playlist_preview()
                input("\n        Presiona Enter para continuar...")
            elif choice == "q":
                print("\n        Saliendo del reproductor.")
                break
            else:
                print("\n        Opción inválida. Intenta otra vez.")
                input("\n        Presiona Enter para continuar...")


def main():
    playlist = build_playlist(SONGS)
    player = PlaylistPlayer(playlist)
    player.menu()


if __name__ == "__main__":
    main()