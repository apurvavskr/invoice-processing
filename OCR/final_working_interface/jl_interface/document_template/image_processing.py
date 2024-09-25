import pytesseract
from PIL import Image
import openai
import json
from django.conf import settings

# Set the API key for your OpenAI requests
openai.api_key = settings.OPENAI_API_KEY

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

def extract_text_boundaries(elements):
    """
    This function calculates the extreme left and right boundaries of the text layout in the invoice.
    """
    min_left = float('inf')
    max_right = float('-inf')
 
    for element in elements:
        # Calculate the right boundary of the element
        right = element['left'] + element['width']
       
        # Update min_left and max_right based on current element's position
        if element['left'] < min_left:
            min_left = element['left']
        if right > max_right:
            max_right = right
   
    return min_left, max_right

def generate_prompt(elements):
    # Convert the OCR data to a JSON formatted string
    ocr_json_str = json.dumps(elements, indent=4)
   
    # Define the task for GPT-4 Turbo
    task_description = """
    Analyze the provided OCR data and differentiate between static and dynamic text.
    - Static text should remain unchanged.
    - Dynamic text should be replaced with placeholders according to these rules:
      - Replace names with @@Name@@ (consider full names as a single placeholder)
      - Replace email addresses with @@Email@@
      - Replace dates with @@Date@@
      - Replace payment methods with @@PaymentMethod@@
      - Replace IDs or numbers with @@ID@@
      - Replace addresses with @@Address@@ (consider full addresses as a single placeholder)
      - Replace organization names with @@Organization@@ (consider full organization names as a single placeholder)
      - Replace phone numbers with @@PhoneNumber@@
      - Replace invoice numbers with @@InvoiceNumber@@
      - Replace amounts with @@Amount@@
      - Replace tax details with @@Tax@@
      - Replace item descriptions with @@ItemDescription@@
      - Replace quantities with @@Quantity@@
      - Replace unit prices with @@UnitPrice@@
      - Replace total prices with @@TotalPrice@@
 
    Maintain the coordinates of the text elements and ensure that placeholders are grouped appropriately.
 
    Additionally, identify elements that are likely to be table headers based on their alignment, font, and style. These headers should be used to create a table structure with placeholders for the dynamic content. Ensure that the columns align properly and that the headers are easily identifiable.
 
    Ensure that the table is positioned correctly in the context of the entire invoice layout and does not overlap with any header or other static text elements. The table should be placed in its own distinct section with proper spacing above and below it.
 
    Generate an HTML representation of the invoice where each text is replaced by its respective placeholder, maintaining the coordinates. For the identified tables, create a table structure with headers and some example rows.
    - Ensure that the table columns' width adjusts to fit the header text.
    - Use `table-layout: auto` and `width: auto` to automatically adjust the table width to the content.
    - Ensure the table remains in the same position as indicated by the OCR data.
 
    Here is the OCR extracted data in JSON format. In the output, print only the HTML code:
    """
   
    prompt = f"{task_description}\n{ocr_json_str}"
    return prompt

def generate_html_with_table_width(prompt, min_left, max_right, width_increase_percentage=40):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048,
        temperature=0.5
    )
   
    html_output = response['choices'][0]['message']['content'].strip()
   
    # Calculate the container width based on the extreme text boundaries
    container_width = max_right - min_left
   
    # Calculate the increased width for the table
    increased_table_width = container_width * (1 + width_increase_percentage / 100)
   
    # Inject the width into the HTML and CSS for the container and table
    full_html = f"<!DOCTYPE html>\n<html>\n<head>\n<style>\n"
    full_html += f".container {{ position: relative; width: {increased_table_width}px; left: {min_left}px; }}\n"
    full_html += f"div {{ position: absolute; }}\ntable {{ width: 100%; border-collapse: collapse; }}\n"
    full_html += "th, td { border: 1px solid black; padding: 4px; }\n"
   
    # Increasing each cell's width
    full_html += "th, td { width: calc(100% / 5); } /* Adjust '5' to the number of columns in your table */\n"
   
    full_html += "</style>\n</head>\n<body>\n<div class='container'>\n"
    full_html += html_output
    full_html += "\n</div>\n</body>\n</html>"
 
    return full_html

def invoice_to_html(image_path, width_increase_percentage=40):
    # Extract the text elements from the image
    elements = extract_text_and_layout(image_path)
   
    # Get the text layout boundaries (left-most and right-most points)
    min_left, max_right = extract_text_boundaries(elements)
   
    # Generate the prompt based on extracted elements
    prompt = generate_prompt(elements)
   
    # Generate the HTML with adjusted table width
    html_output = generate_html_with_table_width(prompt, min_left, max_right, width_increase_percentage)
   
    return html_output
