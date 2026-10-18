import json
import os
from jsonschema import Draft7Validator, RefResolver

def ads_schema_validator():
    schema_dir = os.path.dirname(__file__)
    top_schema_file = os.path.join(schema_dir, "Document.json")
    with open(top_schema_file, "r") as f:
        schema = json.load(f)

    # preload so the validator isn't constantly connecting to github.com
    base = schema["$id"].rsplit("/", 1)[0]
    store = {}
    for p in glob.glob(os.path.join(schema_dir, "*.json")):
        with open(p, "r") as f:
            store[f"{base}/{os.path.basename(p)}"] = json.load(f)
    resolver = RefResolver.from_schema(schema, store=store)

    validator = Draft7Validator(schema=schema, resolver=resolver)

    return validator
