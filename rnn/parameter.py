from torch import cuda

HIDDEN_SIZE = 128
NUM_LAYERS = 1
BATCH_SIZE = 64
FEATURE_SIZE = 37
SEQ_SIZE = 48
OUT_SIZE = 2
USE_GPU = cuda.is_available()
