import os


class Tail:

    def __init__(self, filename, num_of_lines=10, follow=False):
        self._filename = filename
        self._lines = num_of_lines
        self._follow = follow

    def tail(self):

        buffer = 4096
        fsize = os.stat(self._filename).st_size
        count = 0

        file = open(self._filename)
        if buffer - fsize > 0:
            buffer = fsize

        lines = list()

        while len(lines) <= self._lines:
            count += 1
            file.seek(fsize - buffer * count)
            lines.extend(file.readlines())

        for line in lines[-self._lines:]:
            yield line

        if self._follow:
            file.seek(0, os.SEEK_END)
            while True:
                line = file.readline()
                if not line:
                    continue
                yield line

