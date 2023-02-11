from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    frature_store_file_path:str
    train_file_path:str
    test_file_path:str
