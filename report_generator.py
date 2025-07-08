import csv
from fpdf import FPDF

def read_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["Sales"] = int(row["Sales"])
            data.append(row)
    return data

def analyze_data(data):
    sales = [row["Sales"] for row in data]
    return {
        "Total Sales": sum(sales),
        "Average Sales": round(sum(sales)/len(sales), 2),
        "Max Sales": max(sales),
        "Min Sales": min(sales),
    }

def generate_pdf_report(data, analysis, output_file="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Sales Report", ln=1, align="C")

    # Table headers
    pdf.set_font("Arial", "B", 12)
    pdf.cell(60, 10, "Name", 1)
    pdf.cell(60, 10, "Department", 1)
    pdf.cell(60, 10, "Sales", 1, ln=1)

    # Table rows
    pdf.set_font("Arial", "", 12)
    for row in data:
        pdf.cell(60, 10, row["Name"], 1)
        pdf.cell(60, 10, row["Department"], 1)
        pdf.cell(60, 10, str(row["Sales"]), 1, ln=1)

    # Summary
    pdf.ln(10)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Summary", ln=1)
    pdf.set_font("Arial", "", 12)
    for key, value in analysis.items():
        pdf.cell(0, 10, f"{key}: {value}", ln=1)

    pdf.output(output_file)
    print(f"PDF report generated: {output_file}")

if __name__ == "__main__":
    filename = "D"
    data = read_csv(filename)
    analysis = analyze_data(data)
    generate_pdf_report(data, analysis)
