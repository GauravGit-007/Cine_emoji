import os
import sys

sys.path.append(r"c:\github projects\cine_emoji")

from backend.main import generate_movie

def test():
    print("Testing 10 generations of Sci-Fi Hollywood movies...")
    titles = []
    for i in range(10):
        res = generate_movie(category="Hollywood", genre="Sci-Fi")
        titles.append(res['title'])
        print(f"{i+1}: {res['title']}")
        
    unique_titles = set(titles)
    print(f"\nUnique movies out of 10: {len(unique_titles)}")

if __name__ == '__main__':
    test()
