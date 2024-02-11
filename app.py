import copy
from flask import Flask, request, jsonify, render_template
from src.load_image import process_image
from src.solve import solve_sudoku

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/solve_sudoku', methods=['POST'])
def solve_sudoku_puzzle():
    if 'file' not in request.files:
        return 'Файл не был загружен', 400

    file = request.files['file']
    puzzle = process_image(file)  # process the image
    for row in puzzle:
        print(row)
    sudoku = copy.deepcopy(puzzle)
    solved_sudoku_ = solve_sudoku(sudoku)  # solve the sudoku
    for row in sudoku:
        print(row)

    table_html = '<table class="table table-bordered">'
    for row in solved_sudoku_:
        table_html += '<tr>'
        for cell in row:
            table_html += f'<td>{cell}</td>'
        table_html += '</tr>'
    table_html += '</table>'

    return table_html, 200


if __name__ == '__main__':
    app.run(debug=True)
