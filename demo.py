from utils import dprint

def demo():
    import numpy as np
    import torch
    nepochs = 5

    for epoch_id in range(nepochs):
        print(f'[{epoch_id}/{nepochs}] training loss: {np.random.rand()}')

        # two dprint usages
        tensorA = torch.rand(20, 5)
        varB = np.random.rand()
        dprint({"tensorA.size()": tensorA.size(), "varB":varB})
if __name__ == '__main__':
    demo()
