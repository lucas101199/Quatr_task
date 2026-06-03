import requests


# Fetch the latest 10-K report for a specific company and return the URL
# @param    name                Name of the company
# @param    cik                 CIK number of the company
# @return   Return the URL of the latest report            
def get_10k_form(name: str, cik: str) -> str:
    HEADERS = {
        "User-Agent": "test@example.com",
        "Accept-Encoding": "gzip, deflate",
        "Host": "data.sec.gov",
    }

    # Get the URL with all the information specific to a company
    url = "https://data.sec.gov/submissions/CIK" + cik + ".json"
    data = requests.get(url, headers=HEADERS).json()

    # Get all the filings
    recent = data["filings"]["recent"]

    latest_10k = None

    # Looking for the first(most recent) 10-k report
    # And getting the ascencion document address
    for i, form_type in enumerate(recent["form"]):
        if form_type == "10-K":
            latest_10k = {
                "filing_date": recent["filingDate"][i],
                "accession_number": recent["accessionNumber"][i],
                "primary_document": recent["primaryDocument"][i],
            }
            break
    
    if latest_10k is None:
        raise RuntimeError("No 10-K found")

    accession_no_dashes = latest_10k["accession_number"].replace("-", "")

    # Getting the full URL
    filing_url_latest_report = "https://www.sec.gov/Archives/edgar/data/" \
                                + cik + "/" + accession_no_dashes + "/"\
                                + latest_10k['primary_document']
    
    return filing_url_latest_report
