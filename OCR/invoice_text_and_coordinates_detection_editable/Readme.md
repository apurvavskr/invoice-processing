# Invoice Text Extraction and HTML Template Generation

This project is designed to extract text and layout information from an invoice image using Tesseract OCR and generate an editable HTML template. The HTML mirrors the layout of the original invoice and allows the text elements to be edited directly in the browser. GPT-4 Turbo is utilized to format the extracted details into a structured HTML document with absolute positioning.

## Features

- **Text and Layout Extraction**: Uses Tesseract OCR to extract text and its positional data (coordinates, width, height) from an invoice image.
- **Editable HTML Template**: Generates an HTML document where the extracted text is placed exactly at its original position using CSS absolute positioning.
- **Contenteditable Attribute**: Adds the `contenteditable="true"` attribute to make the text elements editable within the HTML document.
- **Table Representation**: If tables are detected in the invoice, they are accurately represented in the HTML template, ensuring correct rows, columns, and spacing.
- **Chunking for Large Invoices**: Processes large invoices in chunks to handle large amounts of text and ensure proper prompt creation for GPT-4 Turbo.

## How It Works

### 1. Text and Layout Extraction
The script first processes the invoice image using Tesseract OCR, extracting each piece of text along with its coordinates, width, and height. This information is crucial for accurately reproducing the layout of the invoice in HTML.

### 2. Prompt Preparation for GPT-4 Turbo
The extracted text and layout information are formatted into a prompt for GPT-4 Turbo. This prompt includes the text and its coordinates, instructing GPT-4 to generate a structured HTML document that mirrors the original invoice layout.

### 3. HTML Generation Using GPT-4 Turbo
GPT-4 Turbo generates an HTML output based on the prompt. The text elements are placed using absolute positioning to match their original coordinates, and each text element is made editable by adding the `contenteditable` attribute.

### 4. Combining HTML Parts (for Large Invoices)
If the invoice contains a large amount of text, the process is divided into smaller chunks. These chunks are sent to GPT-4 Turbo individually, and the resulting HTML parts are combined into a single HTML document.

### 5. Final Output
The final HTML is a full, editable representation of the invoice, where each text element is positioned accurately, and the layout resembles the original image.

## Requirements

- **pytesseract**: For OCR (Optical Character Recognition) to extract text and layout data.
- **Pillow**: For image handling and manipulation.
- **openai**: For interacting with GPT-4 Turbo to generate the HTML template.
- **json**: For managing the extracted data format.

Output
Editable HTML: The output HTML file replicates the layout of the invoice with all text elements positioned at their original coordinates. Each text element is editable via the contenteditable attribute.
Accurate Layout: The generated HTML maintains the structure and alignment of text from the original invoice image.


This README provides clear details on how your code works, what it does, and how to use it, making it ideal for sharing on GitHub.

