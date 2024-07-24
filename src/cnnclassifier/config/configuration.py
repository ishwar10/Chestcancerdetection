import os
from cnnclassifier.constants import *
from cnnclassifier.utils.commons import read_yaml,create_directories
from cnnclassifier.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig,TrainingConfig,EvaluationConfig

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
    
    def training_config(self)->TrainingConfig:
        train_config=self.config.training
        prepare_base_model=self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Chest-CT-Scan-data")
        create_directories([
            Path(train_config.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(train_config.root_dir),
            trained_model_path=Path(train_config.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
        path_of_model="artifacts/training/model.h5",
        training_data="artifacts/data_ingestion/Chest-CT-Scan-data",
        mlflow_uri="https://dagshub.com/ishwarky15/Chestcancerdetection.mlflow",
        all_params=self.params,
        params_image_size=self.params.IMAGE_SIZE,
        params_batch_size=self.params.BATCH_SIZE
            )
        return eval_config
    

    
