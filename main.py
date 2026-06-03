import pdf_converter
import sec_form
import pdf_converter
from fastapi import FastAPI, HTTPException
from pathlib import Path


app = FastAPI()

OUTPUT_DIR = Path("pdf")
OUTPUT_DIR.mkdir(exist_ok=True)

companies = {
    "Apple": "0000320193",
    "Meta": "0001326801",
    "Alphabet": "0001652044",
    "Amazon": "0001018724",
    "Netflix": "0001065280",
    "Goldman Sachs": "0000886982"
    }


# Get the latest 10-K report PDF from one company
@app.get("/companies/{cik}/latest-10k")
def latest_10k_pdf(cik: str) -> dict[str, str]:
    try:
        pdf_path = str(OUTPUT_DIR) + "/" + cik + "_latest_10k.pdf"
        url_report = sec_form.get_10k_form("10k-form", cik)
        pdf_converter.url_to_pdf(url_report, pdf_path)
        return {"status": "success", "pdf_file": str(pdf_path)}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# Get PDFs for all the companies define in the dict above
@app.get("/companies/latest-10k-all")
def latest_10k_all_pdf() -> dict[str]:
    try:
        for name, cik in companies.items():
            url_report = sec_form.get_10k_form(name, cik)
            pdf_path = str(OUTPUT_DIR)+ "/" + name + "-" + cik + "_latest_10k.pdf"
            pdf_converter.url_to_pdf(url_report, pdf_path)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


def main():
    for name, cik in companies.items():
        url_report = sec_form.get_10k_form(name, cik)
        output_path = name + "_report.pdf"
        pdf_converter.url_to_pdf(url_report, output_path)


if __name__ == "__main__":
    main()