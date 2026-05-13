import json
import sys
from src.parser import parse_sections
from src.extractor import extract_structured_data
from src.transformer import build_json_output


def main(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    sections = parse_sections(text)
    structured = extract_structured_data(sections)
    output = build_json_output(structured)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"✅ JSON written to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py input.txt output.json")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    main(input_path, output_path)
