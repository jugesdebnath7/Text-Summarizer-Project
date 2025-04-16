import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataTransformationConfig
from transformers import AutoTokenizer  # type: ignore
from datasets import load_from_disk


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config=config
        self.tokenizer=AutoTokenizer.from_pretrained(config.tokenizer_name)


    def convert_examples_to_features(self, example_batch):
        # Tokenize the input and target texts
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)

        target_encodings = self.tokenizer(
                    example_batch['summary'], max_length=128, truncation=True)
            
            
        # Return a dictionary with the input and target encodings
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids'],

        }
         
    def convert(self):
        dataset_samsum=load_from_disk(self.config.data_path)
        print(dataset_samsum.column_names)
        dataset_samsum_pt =dataset_samsum.map(self.convert_examples_to_features, batched=True)
        dataset_samsum_pt.save_to_disk(self.config.root_dir)
        logger.info(f"Dataset saved to {self.config.root_dir}")

        