import pandas as pd
import os

#Limit retrieved documents
limitDocuments = 10

memory = '8G'
cores = 4

#Pickled dataframe
useCache = False

#Starting point of the pipeline
startPipelineFrom ='start' #values: 'start', 'end'

#Topic Discovery parameters
numOfTopics = 2
topicTopfeatures = 3

#Corpus file
corpusFile = '/home/psmeros/workspace/bigFiles/sampleFoodArticles.tsv'
#gloveFile = '/Users/smeros/workspace/etc/bigFiles/sampleFoodArticles.tsv'
#gloveFile = '/home/smeros/backup_data/sampleFoodArticles.tsv'

#GloVe Embeddings file
gloveFile = None
#gloveFile = '/Users/smeros/workspace/etc/bigFiles/glove.6B/glove.6B.300d.txt'
#gloveFile = '/home/psmeros/workspace/bigFiles/glove.6B.300d.txt'
#gloveFile = '/home/smeros/glove_data/glove.6B.300d.txt'

#Cache and plots directory
os.makedirs('cache', exist_ok=True)
os.makedirs('plots', exist_ok=True)

#File with refined concepts
conceptsFile = 'concepts.csv'

#Pandas settings
pd.set_option('display.max_colwidth', -1)
