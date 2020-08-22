import time
start = time.time()
import train_rasa_nlu as nlu
nlu.predict_intent("cho em hỏi về chuyên ngành iot với ạ")
end = time.time() - start
print(end)