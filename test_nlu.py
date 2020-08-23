import time
start = time.time()
import train_rasa_nlu as nlu
nlu.predict_intent("cơ sở học của FPT")
end = time.time() - start
print(end)