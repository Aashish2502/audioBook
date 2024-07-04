from flask import Flask, render_template,request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.audiobookDB
collection = db.audiobooks


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        genre = request.form.get('genre')
        author = request.form.get('author')
        min_rating = request.form.get('min_rating')
        sort_by = request.form.get('sort_by', 'title')  # Default sort by title

        query = {}
        if genre:
            query['genre'] = genre
        if author:
            query['author'] = author
        if min_rating:
            query['rating'] = {'$gte': int(min_rating)}
        print(query)
        sort_criteria = [(sort_by, 1)]  # 1 for ascending, -1 for descending

        res = collection.find(query).sort(sort_criteria)
        
        
        return render_template('index.html', items=res)   
    else:
        docs = collection.find()
        length = collection.count_documents({})
        return render_template('index.html', items=docs, count = length)



@app.route("/page/<id>")
def page(id):
    select = collection.find_one({"_id":ObjectId(id)})
    return render_template('indvidual.html', item=select)

@app.route("/page/<id>", methods=['POST'])
def review(id):
    review = request.form.get("review")

    res = collection.update_one(
        {"_id":ObjectId(id)},
        { "$push": { "reviews": { "$each": [review] } } }
    )
    if res.modified_count > 0:
        return redirect(url_for('page', id=id))
    else:
        return "<h1>Update failed</h1>", 500

if __name__=="__main__":
    app.run(debug=True)