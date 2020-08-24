import time
start = time.time()
import train_rasa_nlu as nlu
nlu.predict_intent("lịch thi")
#nlu.predict_intent("khá ổn đó")
end = time.time() - start
print(end)