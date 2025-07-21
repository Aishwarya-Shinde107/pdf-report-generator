from reportlab.pdfgen import canvas

# Function to read lines from a text file
def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Function to generate a PDF using ReportLab
def generate_pdf(data, filename):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica", 14)
    y = 800  # Starting position from the top

    for line in data:
        c.drawString(50, y, line)
        y -= 25  # Move down for next line

    c.save()

# Main logic
if __name__ == "__main__":
    input_file = "data.txt"  # The file from which to read data
    output_file = "task2_codtech_report.pdf"  # The PDF file to create

    data = read_data(input_file)
    generate_pdf(data, output_file)

    print("✅ PDF report generated successfully!")
    print(data)