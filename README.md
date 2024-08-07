Invoice to Editable Template Converter

Overview
This project aims to convert any invoice image into an editable HTML template, where specific dynamic text elements are replaced with placeholders for ease of customization. The primary goal is to facilitate businesses in quickly generating consistent and modifiable invoice templates, streamlining their invoicing processes.

Features
OCR Extraction: Utilizes Tesseract OCR to extract text and layout information from an invoice image.
Dynamic Text Identification: Differentiates between static and dynamic text elements based on predefined rules.
Placeholder Replacement: Replaces dynamic text (e.g., names, dates, amounts) with specific placeholders.
Table Structure Recognition: Identifies and structures table headers and contents within the invoice.
HTML Generation: Produces an HTML representation of the invoice with the dynamic placeholders, preserving the original layout and coordinates.

How It Works
Text and Layout Extraction: The extract_text_and_layout function uses Tesseract OCR to extract text along with its positional data from the provided invoice image.
Prompt Generation: The generate_prompt function creates a detailed prompt for the GPT-4 Turbo model, including the OCR data and task description for generating an editable HTML template.
HTML Conversion: The generate_html function leverages the OpenAI API to convert the prompt into an HTML structure, replacing dynamic elements with placeholders.
HTML Output: The final HTML code is wrapped in a container, ensuring proper styling and positioning, making it ready for further use or customization.

Usage
To use this project, follow these steps:

Install Dependencies:

pytesseract for OCR processing
Pillow for image handling
openai for interacting with the GPT-4 Turbo API

Example
Given an invoice image, the project will output an HTML file with placeholders like @@Name@@, @@Date@@, @@Amount@@, etc., allowing you to easily customize and generate new invoices.

Future Enhancements
Enhanced Table Detection: Improve accuracy in detecting and formatting complex tables.
Custom Placeholder Definitions: Allow users to define custom placeholders based on their specific needs.
Support for Multiple Languages: Extend OCR and placeholder replacement for invoices in various languages.
Improved Background Color Detection: Implement a more advanced image processing model to achieve accurate color detection and replication within the template.

Conclusion
This project provides a powerful tool for converting invoice images into editable HTML templates, making it easier for businesses to manage their invoicing needs with greater efficiency and consistency.
