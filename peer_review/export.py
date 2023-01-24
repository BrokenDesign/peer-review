# import numpy as np
# import pandas as pd
# import logging
# from enum import Enum, auto
# from dataclasses import dataclass
# from typing import Protocol, Dict, Tuple

# logger = logging.getLogger(__name__)

# class ExportType(Enum):
#     XLSX = auto()
#     CSV = auto()

# class FileExporter(Protocol):
#     def write_file(self, pdist, url: str):
#         pass


# class ExcelExporter(FileExporter):
#     def __init__(self, uri: str) -> None:
#         # TODO: ExcelExporter
#         pass


# class CSVExporter(FileExporter):

#     # TODO: CSVExporter
#     def __init__(self, uri: str) -> None:
#         pass

# def file_exporter():
#     exporter: FileExporter
#     if uri.endswith(".csv"):
#         exporter = CSVExporter(uri)
#     elif uri.endswith(".xlsx"):
#         exporter = ExcelExporter(uri)
#     else:
#         logger.error(f"Invalid file extention: {uri}")
#         raise Exception("Expected CSV or XLSX filetype")
#     return exporter
