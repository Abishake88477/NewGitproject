data = """
{   
	"id" :  1    ,     
	"trainer" : "Sai",
	"zeyoAddress" :  {
						"permanentAddress" : "Hyderabad",
						"temporaryAddress" : "Chennai"	
	}    
}
"""

jsondf = spark.read.option("header","true").json(sc.parallelize([data]))
jsondf.show()
jsondf.printSchema()


seldf = jsondf.select(

    "id",
    "trainer",
    "zeyoAddress.permanentAddress",
    "zeyoAddress.temporaryAddress"


)

seldf.show()
seldf.printSchema()



withdf = (

    jsondf.withColumn("permanentAddress"  ,  expr("zeyoAddress.permanentAddress"))
    .withColumn("temporaryAddress"  ,  expr("zeyoAddress.temporaryAddress"))

)


withdf.show()
withdf.printSchema()