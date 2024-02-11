import os
import cv2
import numpy as np
import pytesseract
import tempfile


def process_image(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        uploaded_file.save(temp.name)
        temp_path = temp.name

    image = cv2.imread(temp_path, cv2.IMREAD_GRAYSCALE)

    os.unlink(temp_path)
    if image is None:
        raise ValueError("Error: The image cannot be loaded.")

    blur = cv2.GaussianBlur(image, (3, 3), 0)
    binary_image = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_area = 0
    largest_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > largest_area:
            largest_area = area
            largest_contour = contour

    if largest_contour is not None:
        x, y, w, h = cv2.boundingRect(largest_contour)
        grid_image = binary_image[y:y + h, x:x + w]
    else:
        raise Exception("Не удалось найти сетку судоку на изображении.")

    mask = np.full_like(grid_image, fill_value=255)
    cell_size = grid_image.shape[0] // 9
    for i in range(0, grid_image.shape[0], cell_size):
        cv2.line(mask, (0, i), (mask.shape[1], i), color=0, thickness=3)
        cv2.line(mask, (i, 0), (i, mask.shape[0]), color=0, thickness=3)
    cv2.rectangle(mask, (0, 0), (grid_image.shape[1], grid_image.shape[0]), color=0, thickness=3)
    masked_sudoku_image = cv2.bitwise_and(grid_image, mask)

    cells = []
    for i in range(9):
        row = []
        for j in range(9):
            start_y = i * cell_size
            start_x = j * cell_size
            cell = masked_sudoku_image[start_y:start_y + cell_size, start_x:start_x + cell_size]
            row.append(cell)
        cells.append(row)

    custom_config = r'--oem 3 --psm 10 outputbase digits'
    sudoku_matrix = [['*' for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            inverted_image = cv2.bitwise_not(cells[i][j])
            denoised_image = cv2.medianBlur(inverted_image, 3)
            resized_image = cv2.resize(denoised_image, (100, 100), interpolation=cv2.INTER_LINEAR)
            text = pytesseract.image_to_string(resized_image, config=custom_config)
            digits = ''.join(filter(str.isdigit, text))
            sudoku_matrix[i][j] = int(digits[-1]) if digits else '*'

    return sudoku_matrix


def main():
    image_path = 'Sudoku.png'
    sudoku = process_image(image_path)
    for row in sudoku:
        print(row)


if __name__ == '__main__':
    main()
