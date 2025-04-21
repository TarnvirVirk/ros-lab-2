import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/virkt/CS497F/ros-lab-2/install/py_pubsub'
