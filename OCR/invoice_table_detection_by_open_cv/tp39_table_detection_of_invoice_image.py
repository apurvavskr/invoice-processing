import cv2
import numpy as np
from PIL import Image

# Load the image
image_path = r"C:\Users\User\Desktop\shashankbaraicollege\case_studeis\7579746.jpg"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Detect horizontal lines
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
horizontal_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)

# Detect vertical lines
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40))
vertical_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)

# Combine detected lines
table_lines = cv2.addWeighted(horizontal_lines, 0.5, vertical_lines, 0.5, 0.0)

# Find contours to detect the table cells
contours, _ = cv2.findContours(table_lines, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes around the detected cells
boxes = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    boxes.append((x, y, x + w, y + h))
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Save the processed image with detected table cells
processed_image_path = r"C:\Users\User\Desktop\shashankbaraicollege\case_studeis\processed_invoice_with_boxes.png"
cv2.imwrite(processed_image_path, image)

# Function to convert results to HTML
def results_to_html(boxes):
    html = "<html><body>"
    for box in boxes:
        xmin, ymin, xmax, ymax = box
        html += f'<div style="position:absolute; border: 1px solid red; left: {xmin}px; top: {ymin}px; width: {xmax-xmin}px; height: {ymax-ymin}px;">'
        html += "</div>"
    html += "</body></html>"
    return html

# Convert the results to HTML
html = results_to_html(boxes)

# Save the HTML to a file
html_output_path = r"C:\Users\User\Desktop\shashankbaraicollege\case_studeis\output.html"
with open(html_output_path, "w") as f:
    f.write(html)

print(f"HTML saved to {html_output_path}")
