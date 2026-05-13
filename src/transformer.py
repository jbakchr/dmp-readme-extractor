def build_json_output(data: dict) -> dict:
    return {
        "dataset": {
            "title": data.get("title"),
            "version": data.get("version"),
            "description": data.get("description"),
        },
        "people": {
            "creators": data.get("creators", []),
            "contributors": data.get("contributors", [])
        },
        "content": {
            "files": data.get("files", []),
            "keywords": data.get("keywords", [])
        },
        "methods": data.get("methods"),
        "funding": data.get("funding"),
        "citation": data.get("citation")
    }