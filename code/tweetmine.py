import sys

class Tweet(object):
    def __init__(self, content, user, time):
        self.content = content
        self.user = user
        self.time = time

# Takes a file and returns a List of Tweet objects. The file
# should be a scrape of a Storify page.
def read_tweets(fname):
    report = []
    f = open(fname)
    step = 0
    content, user, time = " ", " ", " "
    for l in f:
        step += 1
        if l.strip() == "":
            if step == 5:
                report.append( Tweet(content, user, time))
                content, user, time = " ", " ", " "               
            step = 0
        else:
            if step == 1: content = l.strip()
            if step == 2: user = l.strip()
            if step == 3: time = l.strip()
            if step == 4: pass
    return report

# Return all of the unique users and their tweet counts.
def count_users(tweets):
    users = {}
    for t in tweets:
        if t.user not in users: users[t.user] = 0
        users[t.user] += 1
    return users

def clean(w):
    w = w.lower()
    for c in ".,/;':\"~!@$%^&*()_+=-`{}[]:\"'<>?,./":
        w = w.replace(c,"")
    return w

# Return a list of all of the unique words used.
def count_words(tweets):
    words = {}
    for t in tweets:
        for w in t.content.split():
            ww = clean(w)
            if ww not in words: words[ww] = 0
            words[ww] += 1
    return words

tw = read_tweets(sys.argv[1])

print "Number of tweets: ",len(tw)

k = count_users(tw)
for n in k: print n, k[n]
print "Number of users: ", len(k)


l = []
k = count_words(tw)
for n in k: l.append( (n, k[n]) )
l.sort(key=lambda x:x[1])
for a in l: print a
print len(l)

