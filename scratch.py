class generator(nn.Module):
    # initializers
    def __init__(self):
        super(generator, self).__init__()
		    #++++++++++++++++++++++++++++++++++++++++++++++#
        #++++++++++++++++++++++++++++++++++++++++++++++#
        # ============== YOUR CODE HERE ============== #
        enc_cfg = [64, 128, 256, 512, 512, 512, 512, 512]
        dec_cfg = [512, 1024, 1024, 1024, 1024, 512, 256, 128]
        # U-Net encoder:
        # C64-C128-C256-C512-C512-C512-C512-C512
        # U-Net decoder:
        # CD512-CD1024-CD1024-C1024-C1024-C512-C256-C128
        # As a reminder: let Ck denote a Convolution-BatchNorm-ReLU layer with k filters. CDk
        # denotes a Convolution-BatchNormDropout-ReLU layer with a dropout rate of 50%.
        kernel_size = (4,4)

        self.encoder = nn.Sequential(
            F.Conv2d(3, 64, kernel_size),
            F.LeakyReLU(.2),
            F.Conv2d(64, 128, kernel_size),
            F.BatchNorm2d(128),
            F.LeakyReLU(.2),
            F.Conv2d(128, 256, kernel_size),
            F.BatchNorm2d(256),
            F.LeakyReLU(.2),
            F.Conv2d(256, 512, kernel_size),
            F.BatchNorm2d(512),
            F.LeakyReLU(.2),
            F.Conv2d(512, 512, kernel_size),
            F.BatchNorm2d(512),
            F.LeakyReLU(.2),
            F.Conv2d(512, 512, kernel_size),
            F.BatchNorm2d(512),
            F.LeakyReLU(.2),
            F.Conv2d(512, 512, kernel_size),
            F.BatchNorm2d(512),
            F.LeakyReLU(.2),
            F.Conv2d(512, 512, kernel_size),
            F.BatchNorm2d(512),
            F.LeakyReLU(.2),
            F.Conv2d(512, 512, kernel_size),
            F.BatchNorm2d(512),
            F.LeakyReLU(.2))
        
        # CD512-CD1024-CD1024-C1024-C1024-C512-C256-C128
        self.decoder = F.Sequential(
            F.Conv2d(512, 1024, kernel_size),
            F.BatchNorm2d(1024),
            F.Dropout(.5),
            F.ReLU(),
            F.Conv2d(1024, 1024, kernel_size),
            F.BatchNorm2d(1024),
            F.Dropout(.5),
            F.ReLU(),
            F.Conv2d(1024, 1024, kernel_size),
            F.BatchNorm2d(1024),
            F.Dropout(.5),
            F.ReLU(),
            F.Conv2d(1024, 1024, kernel_size),
            F.BatchNorm2d(1024),
            F.ReLU(),
            F.Conv2d(1024, 1024, kernel_size),
            F.BatchNorm2d(1024),
            F.ReLU(),
            F.Conv2d(1024, 512, kernel_size),
            F.BatchNorm2d(512),
            F.ReLU(),
            F.Conv2d(512, 256, kernel_size),
            F.BatchNorm2d(256),
            F.ReLU(),
            F.Conv2d(256, 128, kernel_size),
            F.BatchNorm2d(128),
            F.ReLU(),
            F.Conv2d(128, 3, kernel_size)
        )
        self.discriminator = F.
		    # ============== END OF CODE ================= # 
        #++++++++++++++++++++++++++++++++++++++++++++++#
        #++++++++++++++++++++++++++++++++++++++++++++++#

    # weight_init
    def weight_init(self, mean, std):
        for m in self._modules:
            normal_init(self._modules[m], mean, std)

    # forward method
    def forward(self, input):
		    #++++++++++++++++++++++++++++++++++++++++++++++#
        #++++++++++++++++++++++++++++++++++++++++++++++#
        # ============== YOUR CODE HERE ============== # 







		    # ============== END OF CODE ================= # 
        #++++++++++++++++++++++++++++++++++++++++++++++#
        #++++++++++++++++++++++++++++++++++++++++++++++#

        return o

class discriminator(nn.Module):
    # initializers
    def __init__(self):
        super(discriminator, self).__init__()
		    #++++++++++++++++++++++++++++++++++++++++++++++#
        #++++++++++++++++++++++++++++++++++++++++++++++#
        # ============== YOUR CODE HERE ============== # 






		    # ============== END OF CODE ================= # 
        #++++++++++++++++++++++++++++++++++++++++++++++#
        #++++++++++++++++++++++++++++++++++++++++++++++#

    # weight_init
    def weight_init(self, mean, std):
        for m in self._modules:
            normal_init(self._modules[m], mean, std)

    # forward method
    def forward(self, input, label):
		    #++++++++++++++++++++++++++++++++++++++++++++++#
        #++++++++++++++++++++++++++++++++++++++++++++++#
        # ============== YOUR CODE HERE ============== # 






		    # ============== END OF CODE ================= # 
        #++++++++++++++++++++++++++++++++++++++++++++++#
        #++++++++++++++++++++++++++++++++++++++++++++++#
        return x
