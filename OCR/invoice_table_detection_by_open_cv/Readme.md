# Invoice Table Detection and HTML Representation

This project detects table structures in an invoice image using OpenCV and generates an HTML representation with bounding boxes for each detected table cell. The process involves applying image processing techniques to identify horizontal and vertical lines, which form the boundaries of table cells, and then converting these detections into an HTML file that visually represents the table layout.

## Features

- **Table Detection**: Identifies horizontal and vertical lines in an invoice image that form the structure of tables.
- **Bounding Box Detection**: Finds and draws bounding boxes around the detected table cells.
- **HTML Conversion**: Converts the bounding boxes into an HTML format where each detected table cell is represented by a `<div>` element positioned absolutely based on its coordinates in the image.
- **Image Processing**: Uses adaptive thresholding and morphological operations for accurate line detection.

## How It Works

### 1. Image Preprocessing
The image is first converted to grayscale using OpenCV. Adaptive thresholding is then applied to create a binary image where table lines can be easily detected.

### 2. Horizontal and Vertical Line Detection
- **Horizontal Lines**: A rectangular structuring element is applied horizontally to detect the horizontal lines in the image.
- **Vertical Lines**: Similarly, a vertical structuring element is used to detect vertical lines.

### 3. Combining Line Detections
The detected horizontal and vertical lines are combined to form the structure of the tables. The result is a binary mask representing the table lines in the image.

### 4. Table Cell Detection
Contours are detected from the combined lines, and bounding boxes are drawn around each detected table cell. These bounding boxes are saved, and the processed image is output with the table cells outlined.

### 5. HTML Generation
The bounding boxes are converted into an HTML file, where each box is represented by an absolutely positioned `<div>` element. The coordinates of the boxes in the image correspond to the positions of the `<div>` elements in the HTML file.

## Requirements

- **OpenCV**: For image processing and table detection.
- **Pillow**: For image loading and manipulation.
- **NumPy**: Used for array operations.
- **HTML Output**: The results are converted to HTML to visually represent the detected table cells.

Output
Processed Image: An image with bounding boxes drawn around the detected table cells.
HTML Output: An HTML file where each detected table cell is represented by a <div> with absolute positioning, simulating the table structure of the invoice.
Example
Input:
An image of an invoice (invoice.jpg) containing a table.

Output:
Processed Image: The image is saved with table cells outlined in green boxes.
HTML: The table cells are represented by red-bordered <div> elements that maintain their relative positions as in the original image.


This README provides a detailed explanation of the code, including how it detects tables in an invoice and how the results are converted into an HTML format, making it suitable for sharing on GitHub.
