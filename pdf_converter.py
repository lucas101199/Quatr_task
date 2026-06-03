import requests
from weasyprint import HTML


# Convert URL from SEC to PDF and save it to a specific folder
# @param    url             URL received from SEC
# @paran    output_path     Path to save the PDF
def url_to_pdf(url: str, output_path: str):
    # Getting the HTML page from the HTM url
    html_page = requests.get(
        url,
        headers={"User-Agent": "test@example.com"}).text


    # Converting the HTML to PDF and saving it
    HTML(string=html_page, base_url=url).write_pdf(output_path)
