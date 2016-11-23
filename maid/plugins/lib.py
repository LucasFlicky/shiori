
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

class Plugin(object):

    def __init__(self, maid, name, type_):
        self.maid = maid
        self.name = name
        self.type = type_

    def load(self):
        pass

    def update_data(self):
        pass

    def loop_callback(self):
        pass


class PluginManager(object):

    def __init__(self, plugins, auto_load=True):
        self.plugins = plugins
        if auto_load:
            self.load()

    def load(self):
        for pl in self.plugins:
            pl.load()

    def update_data(self):
        pass

    def get_jobs(self):
        jobs = []
        for pl in self.plugins:
            if pl.type == 'loop':
                jobs.append(pl.loop_callback)
        return jobs

    def get_commands(self):
        pass
