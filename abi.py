df = spark.createDataFrame([("Renuka1992@gmail.com", "9856765434"), ("zeyotw@yahoo.com", "9844567788")], ["email", "mobile"])
df.show()


splitdf = (
            df
            .withColumn("mail_id",expr("split(email,'@')[0]"))
            .withColumn("mail_c",expr("split(email,'@')[1]"))
)
splitdf.show()



sub_length = (

            splitdf.withColumn("first",expr("substring(mail_id,1,1)"))
            .withColumn("last_2",expr("substring(mail_id,-2,2)"))
            .withColumn("length_less_3", expr("length(mail_id)-3"))


)

sub_length.show()



mask_df = (

    sub_length.withColumn("maskdata", expr("  concat( first, repeat('*',length_less_3) , last_2   )     "))



)


mask_df.show()


final_email = mask_df.withColumn("domain_attached",expr("concat(maskdata,'@',mail_c)"))

final_email.show()