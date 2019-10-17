import re
import reprlib
import collections


RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':
    s = Sentence('"THe time has come," the Walrus said.')
    print(s)

    for word in s:
        print(word)

    print(list(s))

    it = iter(s)
    print(it)
    print(next(it))

    print(issubclass(Sentence, collections.Iterable))
    print(issubclass(Sentence, collections.Iterator))
    print(isinstance(iter(s), collections.Iterable))
    print(isinstance(iter(s), collections.Iterator))
