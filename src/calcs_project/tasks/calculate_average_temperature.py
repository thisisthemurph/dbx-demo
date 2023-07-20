from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

DB_NAME = "claims.temp.airport_temperatures_mu"

spark = SparkSession.builder.appName("calcs_project.calculate_average_temperature").getOrCreate()

print(f"Obtained data from the {DB_NAME} database.")

df = spark.read.table(DB_NAME)
averages_df = df.select(avg("TempHighF"), avg("TempLowF")).collect()

print(averages_df)
