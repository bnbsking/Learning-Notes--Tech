#!bin
mongod -dbpath "C:/MongoDB/data/db" -logpath "C:/MongoDB/data/log/mon.log"

#!bin/mongo.exe
show dbs
use myDB
db.stats()
db.dropDatabase()

db.createCollection('myCo', {capped:true, size:6142800, max:10000})
db.getCollectionNames(); show collections
db.myCo.drop()
db.myCo.renameCollection('myCo2')
db.createCollection('person', {collation:{locale:'zh'}})

db.myCo.insert({'name':'bobo'})
db.myCo.insert([ {'a':1,'b':2}, {'c':3} ])
db.myCo.insert({'_id':10, 'item':'box', 'qty':20})  //_id: primary key
db.myCo.find()
db.myCo.find({$size:3})
db.person.find().sort({'name':1})  //1 increase, -1 decrease
db.myCo.update({item:"box"},{$set:{'qty':35}})
db.myCo.remove({'a':1})
db.myCo.remove({'c':$gt:3}) // delete key > 3
db.myCo.deleteMany({})
db.myCo.deleteMany({'a':1})
db.myCo.deleteOne({'a':1})

var cursor = db.myCo.find()
while (cursor.hasNext()) {
var doc = cursor.next();
print(doc.name);
print(doc);
printjson(doc);
}

db.collection.createIndex( {key:1} )
db.records.insert({"score":1034, "location":{state:"NY", city:"New York"}})
db.records.createIndex( {score:1} )
db.records.find( {score:1034} ).explain()
db.records.getIndexes()
db.getCollectionNames().forEach(function(myCo){
indexes = db[myCo].getIndexes();
print("Indexes for" + myCo + ":");
printjson(indexes);
});
db.collection.dropIndex()

