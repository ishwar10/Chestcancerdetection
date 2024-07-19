from cnnclassifier.config.configuration import configuration_manager
from cnnclassifier.components.data_ingestion import DataIngestion
from cnnclassifier import logger

STAGE_NAME= "Data ingestion Stage"

class data_ingestion_training_pipeline:
    def __init__(self):
        pass
    def main(self):
        config=configuration_manager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(data_ingestion_config)
        data_ingestion.downloadfile()
        data_ingestion.extract_zip_file()


if  __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=data_ingestion_training_pipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e


