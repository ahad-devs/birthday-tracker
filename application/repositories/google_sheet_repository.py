class GoogleSheetRepository:
    def __init__(self):
        self._sheet_url: str | None = None

    def save(self, sheet_url: str) -> None:
        self._sheet_url = sheet_url

    def get(self) -> str | None:
        return self._sheet_url

    def check_duplicate(self, sheet_url: str):
        if self._sheet_url == sheet_url:
            raise sheet_url
            
