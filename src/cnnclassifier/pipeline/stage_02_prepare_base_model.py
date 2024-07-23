from cnnclassifier.config.configuration import configuration_manager
from cnnclassifier.components.Prepare_base_model import Preparebasemodel
from cnnclassifier import logger

STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configuration_manager()
        prepare_base_model_config = config.prepare_base_model()
        prepare_base_model = Preparebasemodel(config=prepare_base_model_config)
        prepare_base_model.getbasemodel()
        prepare_base_model.update_base_model()



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e