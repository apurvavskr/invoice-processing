import pytesseract
from PIL import Image
import openai

openai.api_key = 'sk-proj-pPDnILkYoGPa7y1EfZBMT3BlbkFJdI1HQqy_use_your_key'

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

def prepare_prompt(elements):
    prompt = "I have an invoice image with the following extracted details:\n\n"

    for element in elements:
        prompt += f"- Text: \"{element['text']}\"\n"
        prompt += f"  Coordinates: ({element['left']}, {element['top']}, {element['width']}, {element['height']})\n"
        prompt += "\n"
    
    prompt += (
        "Using this information, generate an editable HTML template that mirrors the layout and design of the original invoice image. "
        "Ensure that the text elements are placed at the same coordinates using absolute positioning within a relatively positioned container. "
        "Make sure each text element is editable by adding 'contenteditable=\"true\"'. "
        "Include tables if present, and ensure they are represented accurately with the same number of rows and columns, and maintain the same spacing between lines. "
        "The output should be well-structured HTML content without omitting any part of the HTML structure. Do not include any explanations or interruptions in the output. Thank you!"
    )
    
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
    return response.choices[0].message['content'].strip()

def split_elements(elements, chunk_size):
    for i in range(0, len(elements), chunk_size):
        yield elements[i:i + chunk_size]

def invoice_to_html(image_path, chunk_size=20):
    elements = extract_text_and_layout(image_path)
    html_parts = []

    for chunk in split_elements(elements, chunk_size):
        prompt = prepare_prompt(chunk)
        html_output = generate_html(prompt)
        html_parts.append(html_output)

    # Combine all HTML parts into a single document
    full_html = "<!DOCTYPE html>\n<html>\n<head>\n<style>\n.container { position: relative; }\n"
    full_html += "div { position: absolute; }\n"
    full_html += "</style>\n</head>\n<body>\n<div class='container'>\n"
    for part in html_parts:
        # Remove any potential HTML boilerplate from parts to avoid duplication
        if "<body>" in part:
            part = part.split("<body>")[1].split("</body>")[0].strip()
        full_html += part
    full_html += "\n</div>\n</body>\n</html>"

    return full_html

# Example usage
image_path = r"C:\Users\User\Desktop\shashankbaraicollege\case_studeis\dataset\training\7579746.jpg"

html_output = invoice_to_html(image_path)
print(html_output)
