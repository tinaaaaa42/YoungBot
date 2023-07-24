import os
from queue import Queue
from random import choice

resources_address = os.path.abspath(os.path.join(os.getcwd(), "resources/memes/ChineseBQB"))
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']

class Memer():
    def __init__(self) -> None:
        self.memes = {}
        self.path_queue = Queue()
        self.path_queue.put(resources_address)
        self.find_all_memes(resources_address)

    def find_all_memes(self, path: str) -> None:
        while self.path_queue.empty() == False:
            path = self.path_queue.get()
            for parent, dirnames, filenames in os.walk(path):
                for dirname in dirnames:
                    self.path_queue.put(os.path.join(parent, dirname))
                for filename in filenames:
                    if filename.lower().endswith(tuple(image_extensions)):
                        self.memes[filename] = os.path.join(parent, filename)

    def get_one_meme(self) -> str:
        return choice(list(self.memes.values()))
    
if __name__ == '__main__':
    memer = Memer()
    print(memer.get_one_meme())