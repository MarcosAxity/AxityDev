# importing libraries
import random
from nltk.corpus import names
import nltk
import json
import pandas as pd
import translators as ts

def texto(file):
    my_file = open(file, "r",encoding = 'latin-1')
  
    # reading the file
    data = my_file.read()
  
    # replacing end of line('/n') with ' ' and
    # splitting the text it further when '.' is seen.
    data_into_list = data.split("\n")
    return data_into_list[0:-1]

def gender_features(word):
    if len(word) > 3:
        return {'last_letter':word[-4:]}
    elif len(word) > 2:
        return {'last_letter':word[-2:]}
    else:
        return {'last_letter':word[-1:]}
        
femenino = texto('palabras_femenino.txt')
masculino = texto('palabras_masculino.txt')
# preparing a list of examples and corresponding class labels.

labeled_names = ([(name, 'male') for name in masculino]+
             [(name, 'female') for name in femenino])
random.shuffle(labeled_names)
  
# we use the feature extractor to process the names data.
featuresets = [(gender_features(n), gender) 
               for (n, gender)in labeled_names]
  
# Divide the resulting list of feature
# sets into a training set and a test set.
train_set, test_set = featuresets[800:], featuresets[:800]
  
# The training set is used to 
# train a new "naive Bayes" classifier.
classifier = nltk.NaiveBayesClassifier.train(train_set)
  
#print(classifier.classify(gender_features('Juan')))
  
# output should be 'male'
#print(nltk.classify.accuracy(classifier, train_set))
  
# it shows accuracy of our classifier and 
# train_set. which must be more than 99 % 
# classifier.show_most_informative_features(10)
def traducir(word):
    return(classifier.classify(gender_features(str(word))))

#reading json files
data1 = 'sample4.json'#scores by entity
data2 = 'sample.json'#global sentiment of each tweet
# Opening JSON file
f = open(data1)
g = open(data2)
# returns JSON object as 
# a dictionary
data1= json.load(f)
data2= json.load(g)
#Closing file
f.close()
g.close()

#analysis sentiment percentages

sentiments= [data2[i]['Sentiment'] for i in range(len(data1))]
df = pd.DataFrame(sentiments)

def get_percentage(df,target):
    long = df.index.size
    res = df.value_counts()[str(target)]*100/long
    return res
def create_sentiment_percentage_json(df):
    sentiments_percentage ={"negativeTweets":get_percentage(df,'NEGATIVE'),
                        "positiveTweets":get_percentage(df,'POSITIVE'),
                        "neutralTweets":get_percentage(df,'NEUTRAL'),
                        "mixedTweets":get_percentage(df,'MIXED'),"id":"1"}
    with open("tweetsFeelings.json", "w") as outfile:
        json.dump(sentiments_percentage, outfile)    

#merging both files to have all the information in only one of them, data1
for i in range(len(data1)):
    data1[i]['global_sentiment']= data2[i]['Sentiment']

def processing(data):
    datos = []
    datos=[{'entidad': {'tipo':data['Entities'][i]['Mentions'][0]['Type'],'texto':data['Entities'][i]['Mentions'][0]['Text']},
            'sentiment_entity': data['Entities'][i]['Mentions'][0]['MentionSentiment']['Sentiment'],
            'negative_score':data['Entities'][i]['Mentions'][0]['MentionSentiment']['SentimentScore']['Negative'],
            'positive_score':data['Entities'][i]['Mentions'][0]['MentionSentiment']['SentimentScore']['Positive'],
            'neutral_score':data['Entities'][i]['Mentions'][0]['MentionSentiment']['SentimentScore']['Neutral'],
            'global_sentiment': data['global_sentiment']} for i in range(len(data['Entities']))]
            
    return datos

def get_data(lista):#input data1
    data = []
    for t in lista:
        p = (processing(t))
        data.append(processing(t))
    return data
data_flat = []  
for j in range(len(get_data(data1))):
    data_flat.append([(get_data(data1)[j][i]['global_sentiment'],get_data(data1)[j][i]['entidad'], get_data(data1)[j][i]['negative_score'],get_data(data1)[j][i]['positive_score']) for i in range(len(get_data(data1)[j]))]
)
def traducir(word):
    return ts.google(str(word), from_language='en', to_language='es') 
def just_person(data):
    lista = []
    for p in data:
        if p[1]['tipo']== 'PERSON':
            lista.append(p)
    return lista
data_flat = [just_person(p) for p in data_flat]
def get_bias(data):#pasar data_flat
    not_bias = 0
    female_bias = 0
    male_bias = 0
    #dic = {}
    for i in range(len(data)):
        if data[i]==[]:
            not_bias = not_bias+1
            #dic[str(0)] = 'no sesgado'
        else:
            if data[i][0][0]=='NEUTRAL':
                not_bias = not_bias+1
            elif data[i][0][0]=='MIXED':
                not_bias = not_bias+1
            if data[i][0][1]['texto']=='I':
                
                not_bias = not_bias+1
            elif data[i][0][1]['texto']=='WE':
                
                not_bias = not_bias+1
            elif data[i][0][1]['texto']=='We' :
                
                not_bias = not_bias+1
            elif data[i][0][1]['texto']=='we':
                
                not_bias = not_bias+1
            elif data[i][0][1]['texto']=='i':
                
                not_bias = not_bias+1
            elif data[i][0][0]=='NEGATIVE':
                
                if len(data[i])==1 and traducir(data[i][0][1]['texto']) == 'male':
                    female_bias = female_bias +1   
                    #dic[str(i)] = 'sesgado en favor de la mujer'
                elif len(data[i])==1 and traducir(data[i][0][1]['texto']) == 'female':
                    male_bias = male_bias +1                 
                    #dic[str(i)] = 'sesgado en favor del hombre'
                if len(data[i])!=1 and traducir(data[i][1][1]['texto']) == 'female' and  traducir(data[i][0][1]['texto']) == 'male' and data[i][0][1][2] > data[i][1][1]:
                    female_bias = female_bias +1                 
                    #dic[str(i)] = 'sesgado en favor de la mujer'       
                elif len(data[i])!=1 and traducir(data[i][1][1]['texto']) == 'male'  and  traducir(data[i][0][1]['texto']) == 'male' and data[i][1][1]>data[i][0][1][2] :
                    male_bias = male_bias +1                 
                    #dic[str(i)] = 'sesgado en favor del hombre'        
            elif data[i][0][0]=='POSITIVE':
                if len(data[i])==1 and traducir(data[i][0][1]['texto']) == 'male':
                    male_bias = male_bias +1  
                    #dic[str(i)] = 'sesgado en favor del hombre'
                elif len(data[i])==1 and traducir(data[i][0][1]['texto']) == 'female':
                    female_bias = female_bias +1     
                    #dic[str(i)] = 'sesgado en favor de la mujer'
                if len(data[i])!=1 and traducir(data[i][1][1]['texto']) == 'female':
                    female_bias = female_bias +1                 
                    #dic[str(i)] = 'sesgado en favor de la mujer'       
                elif len(data[i])!=1 and  traducir(data[i][1][1]['texto']) == 'male':
                    male_bias = male_bias +1                 
                    #dic[str(i)] = 'sesgado en favor del hombre'  
    return [female_bias,male_bias,not_bias] #dic
       
def create_bias_percentage_json(lista):
    long =sum(lista)
    res = [r*100/long for r in lista]
    bias_percentage ={"relatedToWomen":res[0],"relatedToMen":res[1],"tweetPercentageWithoutBias":res[2],"id":"1"}
    with open("gender.json", "w") as outfile:
        json.dump(bias_percentage, outfile)   

if "__main__" == __name__:
    create_bias_percentage_json(get_bias(data_flat))

    create_sentiment_percentage_json(df)
