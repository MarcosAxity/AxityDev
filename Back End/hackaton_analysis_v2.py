import sys
import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
import string
import nltk
from nltk .corpus import stopwords
from nltk import word_tokenize
nltk.download('stopwords')

def hackaton_2022(tweeter_user):
    
    # Print iterations progress
    def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        # Print New Line on Complete
        if iteration == total: 
            print()

    # Creating list to append tweet data to
    attributes_container = []
    users_list = []
    query = str(tweeter_user)

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i > 20:
            break
        attributes_container.append([tweet.user.username,
                                     tweet.date,
                                     tweet.likeCount,
                                     tweet.sourceLabel,
                                     tweet.content])
        items = tweet.renderedContent.split()
        users_iter = [x for x in items if x.startswith("@")]
        users_iter = [x for x in users_iter if x not in query]
        users_list.extend(users_iter)
        users_list = list(dict.fromkeys(users_list))
        
    # Creating a dataframe to load the list
    main_df = pd.DataFrame(attributes_container,
                             columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    
    main_df["extract"] = "main"
    
    # Creating list to append tweet data to
    all_iter_df = pd.DataFrame()
    iterations = len(users_list)
    k = 0

    # Initial call to print 0% progress
    printProgressBar(0, iterations, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for j in users_list:
        attributes_container = []
        #print(j)
        query = j

        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper("from:"+query).get_items()):
            if i > 20:
                break
            attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
            items = tweet.renderedContent.split()
            
        iter_df = pd.DataFrame(attributes_container,
                               columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])

        all_iter_df = pd.concat([all_iter_df, iter_df], ignore_index=True)
        k += 1
        printProgressBar(k, iterations, prefix = 'Progress:', suffix = 'Complete', length = 50)
        
    all_iter_df["extract"] = "rendered"
    
    main_df = pd.concat([main_df,all_iter_df], ignore_index=True)
    
    def clean_tweet(text):
        stopWords = set(stopwords.words('spanish'))
        text = str(text).lower()
        text = re.sub(r'@[A-Za-z0-9]+', ' ', text)  # remover @
        text = re.sub(r'RT[|\s]', ' ', text)        # remove RTs
        text = re.sub(r'#', ' ', text)              # remove # into the tweet
        text = re.sub(r'https?:\/\/\S+', ' ', text) # remove links

        pattern = r'''(?x)                  # set flag to allow verbose regexps
                    (?:[A-Z]\.)+            # abbreviations, e.g. U.S.A
                    | \w+(?:-\w+)*          # Words with optional internal hyphens
                    | \$?\d+(?:\.\d+)?%?    # Currency and precentages, e.g. $12.40 82%
                    | \.\.\.                # Ellipsis
                    | [][.,;"'?():-_`]      # These are separate tokens; includes ],[
                    '''
        words = nltk.regexp_tokenize(text, pattern)
        re_punc = re.compile('[%s]' % re.escape(string.punctuation)) # Remover signos de puntuacion
        stripped = [re_punc.sub('', w) for w in words]
        #stripped = re.sub(' +', ' ', stripped) # remove multiple spaces
        no_garbage = [w for w in stripped if  w.lower() not in stopWords] # remove stopwords
        no_multiple_spaces = [w for w in no_garbage if  w.lower() not in ' '] # remover multiple spaces

        return (" ".join(no_multiple_spaces))
        
    main_df = main_df[:23]
    main_df['text_clean'] = main_df['Tweet'].apply(clean_tweet)
    
    rows, columns = main_df.shape
    print("Clean step: complete!")
    print("Dataset created ::: Rows: {} ::: Columns: {}".format(rows, columns))
    
    #main_df.to_csv("main_tweet_df.txt", sep="|")
    
    main_df["text_clean"].to_csv("text_clean.txt", index=False, header=False)

if "__main__" == __name__:
    hackaton_2022(sys.argv[1])