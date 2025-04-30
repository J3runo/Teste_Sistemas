import time 
from my_code import long_running_function

def test_long_running_funtion_performance():
  start_time = time.time()
  long_running_function()
  end_time = time.time()
  duration = end_time - start_time
  assert duration < 6, f"A funcao demorou {duration}, mais do que o esperado"
