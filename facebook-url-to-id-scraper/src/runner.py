thonimport json
from extractors.facebook_parser import parse_facebook_url
from outputs.exporters import export_to_json

def main():
    with open('data/inputs.sample.txt', 'r') as file:
        urls = file.readlines()

    results = []
    for url in urls:
        facebook_data = parse_facebook_url(url.strip())
        results.append(facebook_data)

    export_to_json(results, 'data/sample.json')

if __name__ == "__main__":
    main()