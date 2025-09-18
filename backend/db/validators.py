quotes_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["quote", "author", "tags", "additionDate"],
        "properties": {
            "quote": {
                "bsonType": "string",
                "description": "The quote itself.",
                "minLength": 1,
            },
            "author": {
                "bsonType": "string",
                "description": "The author of this quote.",
                "minLength": 1,
            },
            "tags": {
                "bsonType": "array",
                "description": "The tags related to this quote.",
                "items": {
                    "bsonType": "string",
                    "description": "A tag itself.",
                    "minLength": 1,
                },
                "minItems": 1,
            },
            "additionDate": {
                "bsonType": "date",
                "description": "Date of parsing for this quote.",
            },
        },
    },
}
