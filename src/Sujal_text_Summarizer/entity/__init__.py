from dataclasses import dataclass
from pathlib import Path 

@dataclass(frozen=True)
class DataingestionConfig:
    root_dir: Path 
    source_URL: str 
    local_data_file: Path  # Corrected the typo here
    unzip_dir: Path
