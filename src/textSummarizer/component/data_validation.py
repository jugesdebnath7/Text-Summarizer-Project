import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_files_exist(self)-> bool:
        try: 
            validation_status = True

            all_files =os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as file:
                        file.write(f"Validation status: {validation_status}\n")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE, 'w') as file:
                        file.write(f"Validation status: {validation_status}\n")

            return validation_status
        except Exception as e:
            logger.error(f"Error occurred during data validation: {e}")
            raise e               
