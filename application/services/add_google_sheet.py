from urllib.parse import urlparse
from application.repositories.google_sheet_repository import GoogleSheetRepository

class AddGoogleSheet:
    def __init__(self, repository: GoogleSheetRepository):
        self.repository = repository

    def execute(self, sheet_url: str):
        # Validate if googel sheet url is not empty or missing
        if not sheet_url:
            raise ValueError("Google Sheet URL cannot be empty.")

        parsed_url = urlparse(sheet_url)

        # Validate HTTPs in the URL
        if parsed_url.scheme != "https":
            raise ValueError("URL has to contain https.")

        # Validate if the right domain is triggered i.e google docs
        if parsed_url.netloc != "docs.google.com":
            raise ValueError("Invalid Google Sheet URL.")

        # Validate if the google spreadsheet id is missing
        if "/spreadsheets/d/" not in parsed_url.path:
            raise ValueError("Invalid Google Sheet URL.")

        # spreadsheet_id = self._extract_spreadsheet_id(parsed_url.path)

        self.repository.save(sheet_url)
        
        return sheet_url

    # Removed after making google_sheet_repository, saving path instead of just id.
    # Extracting spreadsheet id for later APIs
    # def _extract_spreadsheet_id(self, path: str) -> str:
    #     split_path = path.split("/")

    #     # Find the index d and id is the next item in split_path list
    #     try:
    #         spreadsheet_index = split_path.index("d")
    #         spreadsheet_id = split_path[spreadsheet_index + 1]
        
    #     except(ValueError, IndexError):
    #         raise ValueError("Could not extract spreadsheet ID")

    #     if not spreadsheet_id:
    #         raise ValueError("Spreadsheet ID cannot be empty")

    #     return spreadsheet_id