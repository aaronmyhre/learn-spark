from pyspark import SparkContext

#

def main():
    sc = SparkContext("local", "Simple App")

    # count the number of lines in sampleFile
    sampleFile = sc.textFile("sample_text.txt").cache()

    # Split file into works and count the number of workds
    result1 = sampleFile.map(lambda line: line.split()).count()
    print("results:")
    print(result1)

    # Split the file into words, then into letters, count the number of letters
    words = sampleFile.flatMap(lambda line: line.split())
    letters = words.flatMap(lambda word: list(word))
    letterPairs = letters.map(lambda letter: (letter, 1))
    countLetters = letterPairs.reduceByKey(lambda a,b: a + b)
    mostCommon = countLetters.map(lambda letter: (letter[1], letter[0])).sortByKey(ascending=False).take(10)
    print(mostCommon)

    # stop spark
    sc.stop()

# Run main
main()

# Submit
#$SPARK_HOME/bin/spark-submit --master local[4] "4_map_and_reduce.py"
