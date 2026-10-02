class GoogleSheetRepository:
    def __init__(self):
        self._sheet_url: str | None = None
        self._spreadsheet_id: str | None = None

    def save(self, sheet_url: str, spreadsheet_id: str) -> None:
        self._sheet_url = sheet_url
        self._spreadsheet_id = spreadsheet_id

    def get_sheet_url(self) -> str | None:
        return self._sheet_url

    def get_sheet_id(self) -> str | None:
        return self._spreadsheet_id

    def check_duplicate(self, spreadsheet_id: str) -> bool:
        if self._spreadsheet_id == spreadsheet_id:
            return True
        else:
            return False
