"""Count words."""
from operator import itemgetter
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # Count the number of occurences of each word in s
    splitStr = s.split(' ')
    wordCount = {}
    for word in splitStr:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    
    
    # Sort the occurences in descending order (alphabetically in case of ties)
    '''
    In other words, this sort puts things in order by value (-x[1]) 
    (the negative sign puts big numbers first) and then for numbers which are the same,
    it orders according to key (x[0]).
    '''
    wordList = sorted(wordCount.items(),key=lambda x:(-x[1],x[0]))
    
    
    # Return the top n words as a list of tuples (<word>, <count>)
    top_n = wordList[:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    count_words("cat bat mat cat bat cat", 3)
    count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()