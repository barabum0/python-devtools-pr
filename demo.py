import numpy as np

data = {
    'foo': np.array(range(20)),
    'bar': {'apple', 'banana', 'carrot', 'grapefruit'},
    'spam': [{'a': i, 'b': (i for i in range(3))} for i in range(3)],
    'sentence': 'this is just a boring sentence.\n' * 4
}

debug(data)
