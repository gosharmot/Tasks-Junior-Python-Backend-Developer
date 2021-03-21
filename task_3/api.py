from flask import Flask, jsonify

from task_3 import appearance, tests


app = Flask(__name__)

@app.route('/task_3')
def get_task():
    answer = {}
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        answer[f'{i+1} урок'] = f'{test_answer}'

    print(answer)
    return jsonify(answer)


if __name__ == '__main__':
    app.run()