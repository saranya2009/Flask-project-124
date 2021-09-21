from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'Contact': '9876512345',
        'Name': 'Rahul',
        'done':False,
        'id':1
    },
    {
        'Contact': '9876554321',
        'Name': 'Ramesh',
        'done':False,
        'id':2
    }
]
@app.route('/add-data',methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide data'
        },400)
        
    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        'status':'success',
        'message':'task added successfully'
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        'data':tasks
    })

if (__name__ == '__main__'):
    app.run(debug=True)