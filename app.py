from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
from docx import Document
from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# Helper function to convert .docx to .pdf
def convert_to_pdf(docx_path, pdf_path):
    document = Document(docx_path)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for paragraph in document.paragraphs:
        pdf.multi_cell(0, 10, paragraph.text)
    pdf.output(pdf_path)

# Helper function to add password protection
def add_password(pdf_path, password):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    protected_path = pdf_path.replace(".pdf", "_protected.pdf")
    with open(protected_path, "wb") as file:
        writer.write(file)
    return protected_path

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and file.filename.endswith('.docx'):
        filename = secure_filename(file.filename)
        docx_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(docx_path)

        # Convert to PDF
        pdf_path = docx_path.replace('.docx', '.pdf')
        convert_to_pdf(docx_path, pdf_path)

        # Add password if provided
        password = request.form.get('password')
        if password:
            pdf_path = add_password(pdf_path, password)

        return send_file(pdf_path, as_attachment=True)
    return "Invalid file type. Only .docx files are supported.", 400


if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(host='0.0.0.0', port=5000, debug=True)

