from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, Seq2SeqTrainer
from transformers import Seq2SeqTrainingArguments
from textSummarizer.entity import ModelTrainerConfig
from datasets import load_from_disk
import torch
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):

        self.config = config

    def train(self):
        device = torch.device("cpu")    
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        # Load the dataset
        dataset_samsum_pt = load_from_disk(str(self.config.data_path))

        trainer_args = TrainingArguments(

            output_dir=str(self.config.root_dir),
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
        )

        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["train"],
            eval_dataset=dataset_samsum_pt["validation"],
        )
        trainer.train()

        # Save the fine-tuned model
        model_save_path = model_pegasus.save_pretrained(os.path.join(self.config.root_dir,
                                                                      "pegasus-samsum-model"))

        # Save the tokenizer
        tokenizer_save_path = tokenizer.save_pretrained(os.path.join(self.config.root_dir, 
                                                                     "tokenizer"))