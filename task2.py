from fpdf import FPDF

def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.splitlines()
    a = len(lines)
    b = len(content.split())
    c = len(content)
    return a,b,c

def generate_pdf_report(report_path, file_path, a, b, c):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(0, 10, "File Analysis Report", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Analyzed File: {file_path}", ln=True)
    pdf.cell(0, 10, f"Total Lines: {a}", ln=True)
    pdf.cell(0, 10, f"Total Words: {b}", ln=True)
    pdf.cell(0, 10, f"Total Characters: {c}", ln=True)
    pdf.output(report_path)
    print(f"PDF report generated: {report_path}")

if __name__ == "__main__":
    input_file = "input.txt"      
    output_pdf = "report.pdf"     
    a, b, c = analyze_file(input_file)
    generate_pdf_report(output_pdf, input_file, a, b, c)