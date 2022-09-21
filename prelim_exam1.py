from flask import Flask, jsonify, request

app = Flask(__name__)
heart = [


        {
            "heart_id" : "1",
            "date" : "February 2, 2022",
            "heart_rate" : "130"
        },
         {
            "heart_id" : "2",
            "date" : "December 7, 2021",
            "heart_rate" : "124"
        }, 

]

@app.route('/heart', methods=['GET'])
def getHeart():
    return jsonify(heart)
if __name__ == '__main__':
    app.run()