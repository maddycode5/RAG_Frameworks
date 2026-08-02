# embedding utilities

import numpy as np

def batch_generator(items, batch_size):
    for i in range(0, len(items), batch_size):
        yield items[i: i + batch_size]


def validate_embeddings(embeddings):
    if embeddings is None:
        raise ValueError("Embeddings are None")

    if len(embeddings) == 0:
        raise ValueError("Embeddings are empty")

    return True
def numpy_to_list(array:np.ndarray):
    return array.tolist()

    