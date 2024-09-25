# Invoice Image to HTML with Placeholder Conversion

This project provides a pipeline that extracts text and layout data from an invoice image using OCR (Optical Character Recognition), processes the data, and generates an HTML representation of the invoice. The HTML output replaces sensitive or dynamic content (such as names, dates, amounts, etc.) with appropriate placeholders.

## Features

- **OCR-based Text Extraction**: Uses `pytesseract` to extract text and layout information from images of invoices.
- **Placeholder Substitution**: Dynamically identifies key fields (e.g., names, dates, invoice numbers) and replaces them with customizable placeholders.
- **HTML Generation**: Outputs an HTML file that retains the original layout and structure of the invoice, with placeholders replacing dynamic content.

## How It Works

1. **Extract Text and Layout from Invoice**: 
   The `extract_text_and_layout(image_path)` function reads the invoice image and extracts both the text and its spatial properties (such as position and size) using `pytesseract`.

2. **Generate Prompt for GPT-4 Turbo**:
   The `generate_prompt(elements)` function creates a detailed prompt that includes the OCR-extracted data and instructions for GPT-4 Turbo. The prompt asks the model to identify static and dynamic content and replace dynamic content with placeholders.

3. **Generate HTML Representation**:
   The `generate_html(prompt)` function interacts with the GPT-4 Turbo model to generate HTML output that maintains the invoice layout. Dynamic fields such as names, dates, amounts, and email addresses are replaced by placeholders like `@@Name@@`, `@@Date@@`, etc.

4. **Invoice to HTML**:
   The `invoice_to_html(image_path)` function ties everything together. It reads the image, extracts the text, generates the prompt, and produces the final HTML file with placeholders.

## Placeholders Used

The following placeholders are used to anonymize sensitive information from the invoice:

- `@@Name@@` – For names.
- `@@Email@@` – For email addresses.
- `@@Date@@` – For dates.
- `@@PaymentMethod@@` – For payment methods.
- `@@ID@@` – For IDs or numbers.
- `@@Address@@` – For addresses.
- `@@Organization@@` – For organization names.
- `@@PhoneNumber@@` – For phone numbers.
- `@@InvoiceNumber@@` – For invoice numbers.
- `@@Amount@@` – For amounts.
- `@@Tax@@` – For tax details.
- `@@ItemDescription@@` – For item descriptions.
- `@@Quantity@@` – For quantities.
- `@@UnitPrice@@` – For unit prices.
- `@@TotalPrice@@` – For total prices.

## Requirements

- Python 3.x
- `pytesseract`
- `Pillow`
- `openai`



Example
Input: An image of an invoice (invoice.jpg) with various fields like name, date, amount, and email.

Output: An HTML file with the same layout, but sensitive information replaced with placeholders such as @@Name@@, @@Date@@, etc.

