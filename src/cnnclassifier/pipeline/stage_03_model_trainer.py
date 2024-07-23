from cnnclassifier.config.configuration import configuration_manager
from cnnclassifier.components.model_trainer import training
from cnnclassifier import logger



STAGE_NAME = "Training"



class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configuration_manager()
        training_config = config.training_config()
        training_1 = training(config=training_config)
        training_1.get_base_model()
        training_1.train_valid_generator()
        training_1.train()



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e