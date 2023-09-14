import io
import json

from PIL import Image
from rich import print

from focus_converter.common.cli_options import *
from focus_converter.converter import FocusConverter
from focus_converter.data_loaders.data_loader import DataFormats

app = typer.Typer(name="FOCUS converters", add_completion=False)


@app.command("convert")
def main(
    provider: PROVIDER_OPTION,
    export_path: EXPORT_PATH_OPTION,
    data_format: DATA_FORMAT_OPTION,
    data_path: DATA_PATH,
    parquet_data_format: PARQUET_DATA_FORMAT_OPTION = None,
    export_include_source_columns: EXPORT_INCLUDE_SOURCE_COLUMNS = True,
):
    # compute function for conversion

    if data_format == DataFormats.PARQUET and parquet_data_format is None:
        raise typer.BadParameter("parquet_data_format required")

    converter = FocusConverter()
    converter.load_provider_conversion_configs()
    converter.load_data(
        data_path=data_path,
        data_format=data_format,
        parquet_data_format=parquet_data_format,
    )
    converter.configure_data_export(
        export_path=export_path,
        export_include_source_columns=export_include_source_columns,
    )
    converter.prepare_horizontal_conversion_plan(provider=provider)
    converter.convert()


@app.command("explain")
def explain(
    provider: PROVIDER_OPTION,
):
    # function to show conversion plan
    converter = FocusConverter()
    converter.load_provider_conversion_configs()
    converter.prepare_horizontal_conversion_plan(provider=provider)

    image = Image.open(io.BytesIO(converter.explain()))
    image.show()


@app.command("list-providers")
def list_providers():
    converter = FocusConverter()
    converter.load_provider_conversion_configs()
    print(json.dumps({"providers": list(converter.plans.keys())}, indent=4))


if __name__ == "__main__":
    app()