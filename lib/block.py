from collections import namedtuple

Block = namedtuple('Block', ['start', 'end', 'type'])
Block.__new__.__defaults__ = ('quantum',)
Block.expand = lambda self : ' '.join(map(str, range(int(self.start), int(self.end) + 1)))
