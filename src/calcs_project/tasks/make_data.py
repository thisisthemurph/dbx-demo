from pyspark.sql import SparkSession

from pyspark.sql.types import StringType, DateType, IntegerType, StructField, StructType
from datetime import date

spark = SparkSession.builder.appName("calcs_project.make_data").getOrCreate()

schema = StructType([
   StructField("AirportCode", StringType(), nullable=False),
   StructField("Date", DateType(), nullable=False),
   StructField("TempHighF", IntegerType(), nullable=False),
   StructField("TempLowF", IntegerType(), nullable=False)
])

data = [
   [ "BLI", date(2021, 4, 3), 52, 43],
   [ "BLI", date(2021, 4, 2), 50, 38],
   [ "BLI", date(2021, 4, 1), 52, 41],
   [ "PDX", date(2021, 4, 3), 64, 45],
   [ "PDX", date(2021, 4, 2), 61, 41],
   [ "PDX", date(2021, 4, 1), 66, 39],
   [ "SEA", date(2021, 4, 3), 57, 43],
   [ "SEA", date(2021, 4, 2), 54, 39],
   [ "SEA", date(2021, 4, 1), 56, 41]
]

temps = spark.createDataFrame(data, schema)

spark.sql("USE default")
spark.sql("DROP TABLE IF EXISTS demo_temps_table")
temps.write.saveAsTable("demo_temps_table")
