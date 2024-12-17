class ProviderNotFound(Exception):
    def __init__(self, key: str = None):
        super().__init__(f"No provider found for {key}.")
