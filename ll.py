class Node:
    def __init__(self, title: str, artist: str, album: str):
        self.data = {"title": title, "artist": artist, "album": album}
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'(DATA: {self.data} | NEXT: {self.next is not None} | PREV: {self.prev is not None})'


class LinkedList:
    def __init__(self):
        self.start = None

    def __repr__(self):
        nodes = ['START']
        for node in self:
            nodes.append(node.data["title"])
        nodes.append('NIL')
        return '\n' + ' --> '.join(nodes)

    def __iter__(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length

    def traverse(self):
        for node in self:
            print(node.data)

    def insert_at_beginning(self, element: Node):
        element.next = self.start
        element.prev = None

        if self.start is not None:
            self.start.prev = element

        self.start = element

    def insert_at_end(self, element: Node):
        if self.start is None:
            self.start = element
            element.next = None
            element.prev = None
            return

        current = self.start
        while current.next is not None:
            current = current.next

        current.next = element
        element.prev = current
        element.next = None

    def insert_after_node(self, element: Node, node_reference: any):
        current = self.start

        while current is not None:
            if current.data["title"] == node_reference:
                element.next = current.next
                element.prev = current

                if current.next is not None:
                    current.next.prev = element

                current.next = element
                return

            current = current.next

    def delete_node(self, element_data: any):
        if self.start is None:
            return

        if self.start.data["title"] == element_data:
            self.start = self.start.next

            if self.start is not None:
                self.start.prev = None

            return

        current = self.start.next

        while current is not None:
            if current.data["title"] == element_data:
                if current.prev is not None:
                    current.prev.next = current.next

                if current.next is not None:
                    current.next.prev = current.prev

                return

            current = current.next

    def search(self, element_data: any):
        current = self.start

        while current is not None:
            if current.data["title"] == element_data:
                return current

            current = current.next

        return None