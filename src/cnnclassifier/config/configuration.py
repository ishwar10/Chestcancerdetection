import os
from cnnclassifier.constants import *
from cnnclassifier.utils.commons import read_yaml,create_directories
from cnnclassifier.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig

class configuration_manager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,param_filepath=PARAMS_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(param_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir)
        return data_ingestion_config

    def prepare_base_model(self)->PrepareBaseModelConfig:
        config_prep=self.config.prepare_base_model
        create_directories([config_prep.root_dir])
        prepare_base_model=PrepareBaseModelConfig (
            root_dir=Path(config_prep.root_dir),
            base_model_path=Path(config_prep.base_model_path),
            updated_base_model_path=Path(config_prep.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES)
        return prepare_base_model
    
