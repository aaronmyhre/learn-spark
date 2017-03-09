from pyspark import SparkContext


#
sc = SparkContext("local", "Simple App")

# count the number of lines in sampleFile
sampleFile = sc.textFile("sample_text.txt").cache()
count = sampleFile.count()

# print
print("fuck")
print(count)

# stop spark
sc.stop()



# Submit
#$SPARK_HOME/bin/spark-submit --master local[4] 3_first_stand_alone_application.py
