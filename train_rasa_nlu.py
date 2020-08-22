import os
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer 
from rasa_nlu import config
from rasa_nlu.model import Interpreter

def train_rasa(data_json, Config, model_directory):
    train_data = load_data(data_json)
    trainer = Trainer(config.load(Config))
    trainer.train(train_data)
    model_dir = trainer.persist(model_directory, fixed_model_name = "tuyen_sinh")

def predict_intent(text):
    interpreter = Interpreter.load("./models/nlu/default/tuyen_sinh")
    print(interpreter.parse(text))

train_rasa("./data/data_ts.json", "./config/config.yml", "./models/nlu")
