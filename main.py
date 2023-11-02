from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

from textSummarizer.logging import logger
from textSummarizer.pipeline.Pipeline import Pipeline


class PipelineRunner():
    def __init__(self, pipeline_object: Pipeline, stage_name: str):
        self.pipeline_object = pipeline_object
        self.stage_name = stage_name

    def run_pipeline(self):
        try:
            logger.info(f">>>>>> stage {self.stage_name} started <<<<<<")
            self.pipeline_object.main()
            logger.info(f">>>>>> stage {self.stage_name} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e


data_ingestion_pipeline_runner = PipelineRunner(DataIngestionTrainingPipeline(), "Data Ingestion Stage")
data_ingestion_pipeline_runner.run_pipeline()

data_validation_pipeline_runner = PipelineRunner(DataValidationTrainingPipeline(), "Data Validation Stage")
data_validation_pipeline_runner.run_pipeline()

data_transformation_pipeline_runner = PipelineRunner(DataTransformationTrainingPipeline(), "Data Transformation Stage")
data_transformation_pipeline_runner.run_pipeline()

model_trainer_pipeline_runner = PipelineRunner(ModelTrainerTrainingPipeline(), "Model Trainer Stage")
model_trainer_pipeline_runner.run_pipeline()

model_evaluation_pipeline_runner = PipelineRunner(ModelEvaluationTrainingPipeline(), "Model Evaluation Stage")
model_evaluation_pipeline_runner.run_pipeline()
