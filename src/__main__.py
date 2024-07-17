import typer

app = typer.Typer()


@app.command(name='json-to-csv')
def to_csv(path: str):
    print(f"Excel {path}")

@app.command(name='csv-to-json')
def to_json(path: str):
    print(f"CSV {path}")    


if __name__ == "__main__":
    app()