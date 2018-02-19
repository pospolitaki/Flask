from contextlib import contextmanager
import time
# class Lock(object):
#       def __init__(self):
#         self.lock = False

# lock = Lock()

# class My_context_manager_attr():
#   def __init__(self, obj):
#     self.obj_to_edit = obj

#   def __enter__(self):
#     return self.obj_to_edit

#   def __exit__(self, *args):
#     print('obj attr has been edited')

 
# with My_context_manager_attr(lock) as obj:
#   obj.lock = True

# print(lock.lock)

# lock2 = Lock()

# @contextmanager
# def my_manager(lock_obj):
#   print("generator manager", lock_obj.lock)
#   lock_obj.lock = True
#   yield lock_obj
#   print(lock_obj.lock)

# with my_manager(lock2) as l:
#   print(l.lock)


"""
  Сделать менеджер контекста, который бы проглатывал все исключения вызванные 
   в теле и писал их в консоль, пример использования:
    
    with no_exceptions():
      1 / 0 # => logs: ZeroDivisionError

    print('Done!') # => continues execution
"""

# @contextmanager
# def no_exceptions():
#   try:
#     yield
#   except Exception as error:
#     print(error,'has been occured')

# with no_exceptions():
#   1 + 'df'

"""
Сделать менеджер контекста, который бы мог измерять время выполнения блока кода, 
   пример использования:
    
    with TimeIt() as t:
      some_long_function()

    print('Execution time was:', t.time)


"""

@contextmanager
def timeIt():
  start = time.time()
  yield 
  done = time.time()
  print('Execution time was:', str(done - start))


with timeIt():
  [x**10 for x in range(1,1000)]

class TimeIt():
  def __init__(self):
    self.start = time.time()
  def __enter__(self):
    return self
  def __exit__(self, *args):
    self.done = time.time()
    self.time = self.start = self.done
    print(self.time)

with TimeIt() as t:
  [x**10 for x in range(1,1000)]

print('Execution time was:', t.time)
      
  