from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.component.data_transformation import DataTransformation
from textSummarizer.logging import logger

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        """
        Main function to execute the data validation stage of the text summarization pipeline.
        It initializes the configuration manager, retrieves the data validation configuration, and performs data validation.
        """
        # Initialize the configuration manager and retrieve the data validation configuration
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()