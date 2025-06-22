# Pydantic with LangChain

This repository demonstrates how to work with **Pydantic** in the context of LangChain — especially when building structured tools, validators, and data handling pipelines. Pydantic is used to enforce input/output structure, validate data integrity, and serialize/deserialize model inputs.

These examples help clarify how Pydantic works at the field level, model level, and within nested structures.


## 📄 File Descriptions

- `field_validator.py`  For custom constraints on individual fields.

- `model_validator.py`  To check consistency or cross-field conditions after model creation.

- `nested_models.py`  To represent and validate hierarchical or structured input data.

- `computed_field.py`  To dynamically calculate a field value based on others, without explicitly storing it.

- `serialization.py`  Demonstrates `.model_dump()`, `.model_json()`, and parsing from raw inputs.


## 🚀 Getting Started

Install Pydantic v2+ to run these examples:

```bash
pip install pydantic
```
