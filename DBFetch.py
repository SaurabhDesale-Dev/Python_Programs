import pymongo
myclient = pymongo.MongoClient("mongodb+srv://saurabh:123@cluster0.5tnrd.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient['user_data']
mycol = mydb["student_record"]

x=mycol.find_one()

print('done')
print(x)

# OUTPUT
# done
# {'_id': ObjectId('6237771ba21369e34c50dafc'), 'name': 'Saurabh', 'degree_earned': 'Undergraduate'}