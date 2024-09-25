Invoice-to-HTML Processor using OCR and GPT-4 Turbo

This project is designed to extract text and layout information from invoices using Tesseract OCR and process the content to generate an HTML representation. The processed content includes static and dynamic placeholders for personal and transactional details such as names, dates, amounts, and more. GPT-4 Turbo is used to analyze the extracted data and organize it into structured HTML with a focus on retaining layout accuracy, especially for tables, and replacing dynamic content with appropriate placeholders.

Features:

 Text Extraction: Uses Tesseract OCR to extract text and layout information from an invoice image.
 Dynamic Content Detection: Identifies static and dynamic text elements such as names, emails, addresses, invoice numbers, amounts, etc., and replaces dynamic content with placeholders like @@Name@@, @@Email@@, etc.
 Table Detection: Recognizes table structures and identifies headers, dynamically building tables in HTML with placeholder content.
 HTML Generation: Produces an HTML version of the invoice, maintaining the original layout, coordinates, and alignment of elements.
 Layout Preservation: Ensures that the HTML maintains the same look and feel as the original invoice.

How It Works
OCR and Text Layout Extraction: The script uses the Tesseract OCR library to extract text along with its positional data from an invoice image.


Prompt Generation for GPT-4 Turbo: Once the text and layout are extracted, a custom prompt is generated that instructs GPT-4 Turbo to differentiate between static and dynamic content and organize the invoice into a structured HTML format.

HTML Generation Using GPT-4 Turbo: The script sends the generated prompt to GPT-4 Turbo, which analyzes the extracted data and returns HTML code with placeholders for dynamic content.

Final Output: The resulting HTML is wrapped in a proper HTML structure with CSS for positioning, and the final output is displayed or saved.

Required packages include:

pytesseract for OCR
Pillow for image processing
openai for GPT-4 Turbo integration
json for data formatting










