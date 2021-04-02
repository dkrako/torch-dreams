import torch
import numpy as np

def default_func_mean(layer_outputs):
    losses = []
    for output in layer_outputs:
        losses.append(output.mean())
    loss = torch.mean(torch.stack(losses))
    return -loss

class Hook():
    def __init__(self, module, backward=False):
        if backward==False:
            self.hook = module.register_forward_hook(self.hook_fn)
        else:
            self.hook = module.register_backward_hook(self.hook_fn)
    def hook_fn(self, module, input, output):
        self.input = input
        self.output = output
    def close(self):
        self.hook.remove()