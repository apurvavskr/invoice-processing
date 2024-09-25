# Invoice-to-HTML Processor using OCR and GPT-4 Turbo

This project extracts text and layout information from invoice images using Tesseract OCR and processes the content to generate an HTML representation. The processed content includes both static and dynamic placeholders for personal and transactional details such as names, dates, amounts, and more. GPT-4 Turbo is used to analyze the extracted data and organize it into structured HTML, with a focus on retaining layout accuracy, especially for tables, while replacing dynamic content with appropriate placeholders.

## Features

- **Text Extraction**: Uses Tesseract OCR to extract text and layout information from an invoice image.
- **Dynamic Content Detection**: Identifies static and dynamic text elements such as names, emails, addresses, invoice numbers, amounts, etc., and replaces dynamic content with placeholders like `@@Name@@`, `@@Email@@`, and more.
- **Table Detection**: Recognizes table structures and identifies headers, dynamically building tables in HTML with placeholder content.
- **HTML Generation**: Produces an HTML version of the invoice, maintaining the original layout, coordinates, and alignment of elements.
- **Layout Preservation**: Ensures that the HTML maintains the same look and feel as the original invoice, preserving the exact layout and structure.

## How It Works

### 1. OCR and Text Layout Extraction
The script uses the Tesseract OCR library to extract text along with its positional data from an invoice image. Positional information like the text’s location, width, and height is included to maintain layout fidelity in the final HTML output.

### 2. Prompt Generation for GPT-4 Turbo
Once the text and layout are extracted, a custom prompt is generated, instructing GPT-4 Turbo to differentiate between static and dynamic content. It also organizes the invoice into a structured HTML format while identifying fields like names, dates, amounts, and invoice numbers that should be replaced with placeholders.

### 3. HTML Generation Using GPT-4 Turbo
The script sends the generated prompt to GPT-4 Turbo, which analyzes the extracted data and returns the HTML code. Dynamic content is replaced by placeholders (e.g., `@@Name@@`, `@@Date@@`, `@@Amount@@`), while the layout remains consistent with the original invoice.

### 4. Final Output
The resulting HTML is wrapped in a proper HTML structure with inline CSS for positioning. The final output retains the invoice’s original look and feel, including table structures, and is ready for display or storage.

## Requirements

- **pytesseract**: For OCR (Optical Character Recognition).
- **Pillow**: For image processing.
- **openai**: For integration with GPT-4 Turbo.
- **json**: For formatting the extracted OCR data.

Example Placeholders
Here are some of the placeholders used to anonymize dynamic information:

@@Name@@ – For names.
@@Email@@ – For email addresses.
@@Date@@ – For dates.
@@PaymentMethod@@ – For payment methods.
@@ID@@ – For IDs or numbers.
@@Address@@ – For addresses.
@@Organization@@ – For organization names.
@@PhoneNumber@@ – For phone numbers.
@@InvoiceNumber@@ – For invoice numbers.
@@Amount@@ – For amounts.
@@Tax@@ – For tax details.
@@ItemDescription@@ – For item descriptions.
@@Quantity@@ – For quantities.
@@UnitPrice@@ – For unit prices.
@@TotalPrice@@ – For total prices.
