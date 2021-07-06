import sys

from urllib.request import urlopen

#pass the url argument and fetch the text to story_words
def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

#print function
def print_items(items):
    for item in items:
        print(item)


#main call
def main():

    url = sys.argv[1]
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main()