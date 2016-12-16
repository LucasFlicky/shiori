
"""
MIT License

Copyright (c) 2016 William Tumeo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from random import randint


def code_block(string, lang='') -> str:
    """Format a string using Markdown codeblock"""
    return "```{0}\n{1}\n```".format(lang, string)


class RandomPick(object):

    def __init__(self, items):
        self.items = items
        self.last_index = -1
        self.index = -1


    def pick_one(self):
        while self.last_index == self.index:
            self.index = randint(0, len(self.items)-1)
        self.last_index = self.index
        return self.items[self.index]


if __name__ == '__main__':
    
    print('TEST:', code_block)
    print(code_block("Lorem ipsum dolor sit amet"))
    print(code_block("Lorem ipsum dolor sit amet", "python"))
    

    print('TEST:', RandomPick)
    mini_list = 'lorem', 'ipsum', 'dolor', 'sit', 'amet'
    test_pick = RandomPick(mini_list)
    for n in range(10):
        print(test_pick.pick_one())
