import re
import reprlib
import collections


RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        return SentenceIterator(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == '__main__':
    s = Sentence('hello world')
    for word in s:
        print(word)

    # Sentence 는 Iterable 이지만 Iterator 가 아님(__iter__()만 구현, iter()를 통해 Iterator 생성)
    print(issubclass(Sentence, collections.Iterable))
    print(issubclass(Sentence, collections.Iterator))

    # SentenceIterator 는 Iterable 이면서 Iterator(__iter__(), __next__() 구현)
    print(issubclass(SentenceIterator, collections.Iterable))
    print(issubclass(SentenceIterator, collections.Iterator))
