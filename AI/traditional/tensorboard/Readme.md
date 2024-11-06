# tensorboard
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter()
writer.add_scalar("Loss/train", loss, epoch)

```bash
tensorboard --logdir=runs
```

+ more: https://pytorch.org/docs/stable/tensorboard.html 


# 