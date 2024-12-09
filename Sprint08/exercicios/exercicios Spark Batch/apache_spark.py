from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Etapa 1
spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)
df_nomes.show(5)

# Etapa 2
df_nomes = df_nomes.withColumnRenamed("_c0", "Nome")
df_nomes.printSchema()
df_nomes.show(10)

# Etapa 3
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    F.when(F.rand() < 1/3, "Fundamental")
     .when(F.rand() < 2/3, "Medio")
     .otherwise("Superior")
)
df_nomes.show(5)

# Etapa 4
df_nomes = df_nomes.withColumn(
    "Pais",
    F.when(F.rand() < 1/12, "Argentina")
     .when(F.rand() < 2/12, "Bolivia")
     .when(F.rand() < 3/12, "Brasil")
     .when(F.rand() < 4/12, "Chile")
     .when(F.rand() < 5/12, "Colombia")
     .when(F.rand() < 6/12, "Equador")
     .when(F.rand() < 7/12, "Guiana")
     .when(F.rand() < 8/12, "Paraguai")
     .when(F.rand() < 9/12, "Peru")
     .when(F.rand() < 10/12, "Suriname")
     .when(F.rand() < 11/12, "Uruguai")
     .otherwise("Venezuela")
)
df_nomes.show(5)

# Etapa 5
df_nomes = df_nomes.withColumn("AnoNascimento", (F.lit(1945) + (F.rand() * 66).cast("int")))
df_nomes.show(5)

# Etapa 6
df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2000).select("Nome")
df_select.show(10)

# Etapa 7
df_nomes.createOrReplaceTempView("pessoas")
df_sql = spark.sql("select * from pessoas where AnoNascimento >= 2000")
df_sql.show(10)

# Etapa 8
millennials = df_nomes.filter((F.col("AnoNascimento") >= 1980) & (F.col("AnoNascimento") <= 1994)).count()
print(f"Há {millennials} pessoas da geração Millennials")

# Etapa 9
millennials_sql = spark.sql("select count(*) from pessoas where AnoNascimento between 1980 and 1994")
millennials_sql.show()

# Etapa 10
df_geracoes = spark.sql("""
    select Pais,
        case
            when AnoNascimento between 1944 and 1964 then 'Baby Boomers'
            when AnoNascimento between 1965 and 1979 then 'Geração X'
            when AnoNascimento between 1980 and 1994 then 'Millennials (Geração Y)'
            when AnoNascimento between 1995 and 2015 then 'Geração Z'
        end as Geracao,
        count(*) as quantidade
    from pessoas
    group by Pais, Geracao
    order by Pais, Geracao
""")
df_geracoes.show()
