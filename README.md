## Translate

Translate the values in a JSON file, preserving the structure and keys. You need a deepl API key to use this program.

## Example

Create a file test.json
```json
{
    "foo" : {
        "bar" : "Hello, world!"
    }
}
```

Translate the file to French:
```bash
export KEY=YOUR-DEEPL-KEY
python -m venv .venv # Create a virtual env
(.venv) pip install -r requirements.txt # Install dependencies
(.venv) python translate.py test.json fr -k $KEY
```

The translation is printed to stdout. Use a redirection operator to print it to a file.
```bash
python translate.py test.json fr -k $KEY > test-fr.json
```