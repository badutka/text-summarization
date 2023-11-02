import os
from textSummarizer.logging import logger
from textSummarizer.config.configuration import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            statuses = []
            messages = []

            for file in all_files:
                validation_status = file in self.config.ALL_REQUIRED_FILES
                statuses.append(validation_status)

                msg = f"Validation status: {validation_status} for file: {file}"
                messages.append(msg)

                logger.info(msg)

            status = all(statuses)

            with open(self.config.STATUS_FILE, 'w') as f:
                for msg in messages:
                    f.write(msg + "\n")
                f.write(f"Overall status: {status}")

            return status

        except Exception as e:
            raise e
