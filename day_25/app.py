import gradio as gr
import easyocr
import cv2
import tempfile
reader = easyocr.Reader(["en"])
def extract_text(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    processed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = reader.readtext(processed)
    text = ""
    for item in result:
        text += item[1] + "\n"
    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".txt",
        mode="w",
        encoding="utf-8"
    )
    temp.write(text)
    temp.close()
    return (
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
        processed,
        text,
        temp.name
    )
demo = gr.Interface(
    fn=extract_text,
    inputs=gr.Image(type="numpy", label="Upload Document"),
    outputs=[
        gr.Image(label="Original Image"),
        gr.Image(label="Processed Image"),
        gr.Textbox(label="Extracted Text", lines=12),
        gr.File(label="Download TXT")
    ],
    title="Document OCR Web Application",
    description="Upload a document image and extract text using EasyOCR."
)
demo.launch(
    debug=True,
    inbrowser=True
)