# Author: Kunal PATIL 

import twint
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count
from pyspark.sql.types import *

c = twint.Config()
c.Search = "dassault systemes"
c.Hide_output = True
c.Pandas = True
c.Limit = 10

tweets = twint.run.Search(c)

columns = twint.storage.panda.Tweets_df.columns

df = twint.storage.panda.Tweets_df[['hashtags', 'tweet']]

sc = SparkContext.getOrCreate()
sc.setLogLevel('WARN')
spark = SparkSession(sc)
htags = sc.parallelize(df['hashtags'])
htags = htags.reduce(lambda x, y: x+y)
twitter_hashtags = spark.createDataFrame(htags, StringType()).createTempView('data')
spark.sql('SELECT value, count(value) As tag_count from data group by value order by tag_count DESC LIMIT 5').show()
sc.stop()