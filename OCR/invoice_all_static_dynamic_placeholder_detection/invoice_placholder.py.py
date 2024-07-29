import pytesseract
from PIL import Image
import openai
import json
import re

openai.api_key = 'sk-pr'

def extract_text_and_layout(image_path):
    image = Image.open(image_path)
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    elements = []
    for i in range(len(data['level'])):
        if data['text'][i].strip():  # Only consider non-empty text
            element = {
                'text': data['text'][i],
                'left': data['left'][i],
                'top': data['top'][i],
                'width': data['width'][i],
                'height': data['height'][i]
            }
            elements.append(element)
    
    return elements

def generate_prompt(elements):
    # Convert the OCR data to a JSON formatted string
    ocr_json_str = json.dumps(elements, indent=4)
    
    # Define the task for GPT-4 Turbo
    task_description = """
    Analyze the provided OCR data and differentiate between static and dynamic text. 
    - Static text should remain unchanged.
    - Dynamic text should be replaced with placeholders according to these rules:
      - Replace names with @@Name@@
      - Replace email addresses with @@Email@@
      - Replace dates with @@Date@@
      - Replace payment methods with @@PaymentMethod@@
      - Replace IDs or numbers with @@ID@@
      - Replace addresses with @@Address@@
      - Replace organization names with @@Organization@@
      - Replace phone numbers with @@PhoneNumber@@
      - Replace invoice numbers with @@InvoiceNumber@@
      - Replace amounts with @@Amount@@
      - Replace tax details with @@Tax@@
      - Replace item descriptions with @@ItemDescription@@
      - Replace quantities with @@Quantity@@
      - Replace unit prices with @@UnitPrice@@
      - Replace total prices with @@TotalPrice@@

    Maintain the coordinates of the text elements and ensure that placeholders are grouped appropriately.
    Finally, generate an HTML representation of the invoice where each text is replaced by its respective placeholder, maintaining the coordinates.
    Here is the OCR extracted data in JSON format:
    """
    
    prompt = f"{task_description}\n{ocr_json_str}"
    return prompt

def generate_html(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048,
        temperature=0.5
    )
    
    html_output = response.choices[0].message['content'].strip()
    return html_output

def invoice_to_html(image_path):
    elements = extract_text_and_layout(image_path)
    prompt = generate_prompt(elements)
    html_output = generate_html(prompt)

    # Wrap the HTML in the required structure
    full_html = "<!DOCTYPE html>\n<html>\n<head>\n<style>\n.container { position: relative; }\n"
    full_html += "div { position: absolute; }\n"
    full_html += "</style>\n</head>\n<body>\n<div class='container'>\n"
    full_html += html_output
    full_html += "\n</div>\n</body>\n</html>"

    return full_html

# Example usage
image_path = r"C:\Users\User\Desktop\shashankbaraicollege\case_studeis\test2_out.jpg"

html_output = invoice_to_html(image_path)
print(html_output)

