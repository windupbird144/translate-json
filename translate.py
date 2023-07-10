import argparse
import json
from collections import OrderedDict
from apply import apply_func_to_values
from deepl import translate_token

def main(filename, target_language, api_key):
    # Read JSON file
    with open(filename) as file:
        json_data = json.load(file, object_pairs_hook=OrderedDict)

    # Apply function to values
    def translate_to_target_language(token):
        return translate_token(token, target_language, api_key)

    modified_dict = apply_func_to_values(json_data, translate_to_target_language) 

    # Print prettified JSON
    print(json.dumps(modified_dict, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    # Set up CLI argument parser
    parser = argparse.ArgumentParser(description="Apply function to values in a JSON file.")
    parser.add_argument("filename", help="Path to the JSON file")
    parser.add_argument("target_language", help="Target language")
    parser.add_argument("-k", "--key", help="Deepl API key", required=True)

    # Parse CLI arguments
    args = parser.parse_args()

    # Call the main function with the provided arguments
    main(args.filename, args.target_language, args.key)