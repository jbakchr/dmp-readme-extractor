import re


def extract_creators(text):
    creators = []

    lines = text.split("\n")
    for line in lines:
        name_match = re.match(r"^(.*?),", line)
        email_match = re.search(r"contact:\s*([\w\.-]+@[\w\.-]+)", line)
        orcid_match = re.search(r"ORCID:\s*([\d\-X]+)", line)

        if name_match:
            creator = {
                "name": name_match.group(1).strip()
            }

            if email_match:
                creator["email"] = email_match.group(1)

            if orcid_match:
                creator["orcid"] = orcid_match.group(1)

            creators.append(creator)

    return creators


def extract_keywords(text):
    return [k.strip() for k in text.split("\n") if k.strip()]


def extract_files(text):
    files = []
    for line in text.split("\n"):
        if "." in line:
            files.append(line.strip())
    return files


def extract_structured_data(sections: dict) -> dict:
    data = {}

    # Basic fields
    data["title"] = sections.get("title of the dataset")
    data["version"] = sections.get("version of dataset")
    data["description"] = sections.get("description")
    data["methods"] = sections.get("methods, materials and software")
    data["funding"] = sections.get("funding")
    data["citation"] = sections.get("how to cite this data")

    # Structured fields
    if "creators (include contact and orcid)" in sections:
        data["creators"] = extract_creators(
            sections["creators (include contact and orcid)"]
        )

    if "contributors" in sections:
        data["contributors"] = extract_creators(
            sections["contributors"]
        )

    if "keywords" in sections:
        data["keywords"] = extract_keywords(
            sections["keywords"]
        )

    if "this dataset contains the following files" in sections:
        data["files"] = extract_files(
            sections["this dataset contains the following files"]
        )

    return data