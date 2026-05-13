def parse_sections(text: str) -> dict:
    sections = {}
    current_key = None
    buffer = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        # Detect headers (ending with :)
        if line.endswith(":"):
            if current_key:
                sections[current_key] = "\n".join(buffer).strip()
                buffer = []

            current_key = line[:-1].strip().lower()
        else:
            buffer.append(line)

    # Save last section
    if current_key:
        sections[current_key] = "\n".join(buffer).strip()

    return sections
