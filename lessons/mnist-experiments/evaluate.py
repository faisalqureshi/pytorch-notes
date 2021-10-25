import torch
from torch.utils import tensorboard

class Evaluate:
    def __init__(self, device=-1):
        self.device = device # -1 suggests cuda isn't available
        self.loss = None
        self.model = None

        print(f'Evaluating on {self.get_device_name()}')

    def get_device_name(self):
        if self.device == -1 or not torch.cuda.is_available():
            return 'CPU (No cuda-enabled device found)'
        else:
            return f'[{self.device}]: {torch.cuda.get_device_name(self.device)}'

    def gpu(self, o):
        """
        Ensure that the item isn't on gpu already.  Otherwise, I am not sure
        what is the effect of this call.
        """
        if self.device >= 0:
            return o.to(device=self.device)
        return o.to(device='cpu')

    def cpu(self, o):
        """
        Ensure that the item isn't on cpu already.  Otherwise, I am not sure
        what is the effect of this call.
        """
        if self.device >= 0:
            return o.to(device='cpu')
        return o

    def set_loss(self):
        self.loss = torch.nn.MSELoss()

    def set_model(self, model):
        self.model = self.gpu(model)

    def load_model(self):
        return load_checkpoint(filepath)

    def load_checkpoint(self, filepath):
        assert(self.model)

        checkpoint = torch.load(filepath)
        self.model.load_state_dict(checkpoint['model_state_dict'])

    def reconstruct_one_image(self, img):
        assert(self.model)
        assert(self.loss)

        start = torch.cuda.Event(enable_timing=True)    
        end = torch.cuda.Event(enable_timing=True)

        start.record()

        self.model.eval()
        img = self.gpu(img.unsqueeze(0))
        with torch.no_grad():
            output = self.model(img)
        
        sample_loss = self.loss(img, output)

        end.record()
        torch.cuda.synchronize()
        time_per_sample = start.elapsed_time(end)

        print(f'Took {time_per_sample} ms')

        return self.cpu(output.squeeze(0)), sample_loss.item(), time_per_sample
