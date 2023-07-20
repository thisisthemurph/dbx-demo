from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

from pyspark.sql.types import StringType, DateType, IntegerType, StructField, StructType

spark = SparkSession.builder.appName("calcs_project.calculate_average_temperature").getOrCreate()

RESULT_TABLE_NAME = "claims.temp.airport_temperatures_mu"

df = spark.read.table(RESULT_TABLE_NAME)
averages_df = df.select(avg("TempHighF"), avg("TempLowF")).collect()

print(averages_df)
