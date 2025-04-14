from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.component.data_validation import DataValidation
from textSummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        """
        Main function to execute the data validation stage of the text summarization pipeline.
        It initializes the configuration manager, retrieves the data validation configuration, and performs data validation.
        """
        # Initialize the configuration manager and retrieve the data validation configuration
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()