"""
This script serves as the entry point for the data ingestion stage of a text summarization pipeline.
It imports the necessary modules and classes, sets up the logging, and executes the main function of the DataIngestionTrainingPipeline class.

The script ensures that the necessary modules and classes are imported and the logging setup is done correctly before executing the main function.

If the script is run directly, it will execute the main function of the DataIngestionTrainingPipeline class. If the script is imported as a module, the necessary modules and classes will be available for other scripts to use.

Usage:
    python main.py
    
"""

import sys
import os
sys.path.append(os.path.abspath("src"))
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"  

if __name__ == "__main__":
    # Call the main function of the DataIngestionTrainingPipeline class to execute the stage
    try:
        logger.info(f"\n\n===================== Stage {STAGE_NAME} started =====================")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.main()
        logger.info(f"\n\n ===================== Stage {STAGE_NAME} completed =====================\n\n")
    except Exception as e:
        logger.exception(f"An error occurred in the {STAGE_NAME}: {e}")
        raise e    
    