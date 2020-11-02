from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbnike


@app.route('/')
def home():
    return render_template('index.html', title='home')


@app.route('/cart')
def cart():
    return render_template('cart.html', title='cart')


@app.route('/api/home', methods=['GET'])
def showHome():
    shoes = list(db.shoes.find({}, {'_id': 0}))
    jacket = list(db.clothes_jacket.find({}, {'_id': 0}))
    hoodie = list(db.clothes_hood.find({}, {'_id': 0}))
    pants = list(db.clothes_pants.find({}, {'_id': 0}))
    top = list(db.clothes_top.find({}, {'_id': 0}))
    equipment = list(db.equip.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'shoes': shoes, 'jacket': jacket, 'hoodie': hoodie, 'pants': pants, 'top': top,
                    'equipment': equipment})


@app.route('/api/cart', methods=['GET'])
def showCart():
    result = list(db.cart.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'cart': result})


@app.route('/api/cart', methods=['POST'])
def saveCart():
    name = request.form['name_give']
    result = db.all.find_one({'name': name}, {'_id': 0})
    db.cart.insert_one(result)
    return jsonify({'result': 'success', 'msg': '장바구니 담기 완료'})


@app.route('/api/cart/del', methods=['POST'])
def delCart():
    name = request.form['name_give']
    db.cart.delete_one({'name': name})
    return jsonify({'result': 'success', 'msg': '장바구니 삭제 완료'})


@app.route('/api/search', methods=['POST'])
def goSearch():
    db.search.drop()
    name = request.form['name_give']
    temp = list(db.all.find({}, {'_id': 0}))

    for one in temp:
        if name in one['name']:
            db.search.insert_one(one)
    return jsonify({'result': 'success', 'msg': '검색 완료'})


@app.route('/api/search', methods=['GET'])
def showSearch():
    result = list(db.search.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'target': result})


if __name__ == '__main__':
    app.run()
