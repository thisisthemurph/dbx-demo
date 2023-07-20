from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

DB_NAME = "claims.temp.airport_temperatures_mu"

spark = SparkSession.builder.appName("calcs_project.calculate_average_temperature").getOrCreate()

print(f"Obtained data from the {DB_NAME} database.")

df = spark.read.table(DB_NAME)
num_rows = df.count()

averages, = df.select(avg("TempHighF"), avg("TempLowF"))\
    .withColumnRenamed("avg(TempHighF)", "TempHighF")\
    .withColumnRenamed("avg(TempLowF)", "TempLowF")\
    .collect()

avg_temp_low = averages["TempLowF"]
avg_temp_high = averages["TempHighF"]

print(f"The average airport temperature has a low of {avg_temp_low:.2f}°F and a high of {avg_temp_high:.2f}°F")
