from typing import Annotated
import typer
import csv_handler
import json_handler

app = typer.Typer()


@app.command(name='json-to-csv')
def csv(path: str, json: Annotated[bool, typer.Option(help="Save the results to a json file")] = False):
    print(f"Excel {path}")
    csv_handler.handle(path, json)

@app.command(name='csv-to-json')
def to_json(path: str):
    print(f"CSV {path}")
    json_handler.handle(path)


if __name__ == "__main__":
    app()