from pydprint import dprint

def demo():
    import numpy as np
    import torch
    nepochs = 5

    for epoch_id in range(nepochs):
        loss1 = np.random.rand()
        loss2 = np.random.rand()

        # dprint usage1: check tensor size
        tensorA = torch.rand(20, 5)
        dprint(tensorA.size())

        # dprint usage2: check variable-value
        varB = np.random.rand()
        dprint(varB)

        # dprint usage3: monitor multiple things with inline (by passing them as a dict)
        test_dict = {"tensorA.size()": tensorA.size(), "varB":varB}
        dprint(test_dict)

        # dpring usage4: monitor within execution (print-and-return)
        #loss_total = loss1 + loss2
        loss_total = loss1 + dprint(loss2)

        # normal print during execution
        print(f'[{epoch_id}/{nepochs}] training loss: {loss_total}')
if __name__ == '__main__':
    demo()
