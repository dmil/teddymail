def email_checker():
    '''
    Loads the atomfeed from gmail
    Checks to see if loved_ones are in the current unread emails
    If they are, output a 1 to the page (signaling the arduino to light up)
    If they are not, output a 0 to the page (signaling the arduino to turn its light off)
    '''

    import urllib2, base64
    import pickle

    #Get Credentials
    credentials_file = open('./password.txt','r')
    username = pickle.load(credentials_file)
    password = pickle.load(credentials_file)
    credentials_file.close()

    #Login to gmail atomfeed and store output in "feed" variable
    url = "https://mail.google.com/mail/feed/atom/"
    req = urllib2.Request(url)
    authstr = base64.encodestring("%s:%s" % (username, password))[:-1]
    req.add_header("Authorization", "Basic " + authstr)
    feed = urllib2.urlopen(req).read()

    #Get Search terms from 'loved_ones.txt'
    loved_ones_file = open("loved_ones.txt", 'r')
    loved_ones_str = loved_ones_file.read()
    loved_ones = loved_ones_str.split("\n") #This array stores the list of search terms
    loved_ones_file.close()

    #If any one of the strings in loved_ones is found in the feed, return 1
    for search_term in loved_ones:
        if search_term in feed:
            return '1'
    #If no search_term is found, return 0
    return '0'


def hello_world():
    s = email_checker()
    print s
    return s
