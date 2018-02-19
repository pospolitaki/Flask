from contextlib import contextmanager

@contextmanager
def my_context_manager(fname):
    f = open(fname) #all code before yield will be executed as __enter__()
    yield f.read()
    #all code after yield will be executed as __exit__()
    f.close()

with my_context_manager('test.txt') as f:
    print(f)