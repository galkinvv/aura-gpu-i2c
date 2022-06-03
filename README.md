# aura-gpu-dkms

i2c driver for AURA capable GPUs 

## Installing

You can get releases for Fedora, OpenSUSE, and OpenMandriva from my [COPR](https://copr.fedorainfracloud.org/coprs/kylegospo/aura-gpu-dkms/).

If you wish to use this with Secure Boot, follow [this guide](https://gist.github.com/KyleGospo/9adbe078d1d7f160ae43c091df98f773).

## After Install

The `i2c-dev` module is required:

List all i2c devices with:
```
sudo i2cdetect -l
```
It will output something like
```
i2c-3   smbus           SMBus PIIX4 adapter port 4 at 0b00      SMBus adapter
i2c-10  i2c             AMDGPU DM i2c hw bus 4                  I2C adapter
i2c-1   smbus           SMBus PIIX4 adapter port 2 at 0b00      SMBus adapter
i2c-8   i2c             AMDGPU DM i2c hw bus 2                  I2C adapter
i2c-6   i2c             AMDGPU DM i2c hw bus 1                  I2C adapter
i2c-4   i2c             AMDGPU DM i2c hw bus 0                  I2C adapter
i2c-11  i2c             AURA GPU adapter                        I2C adapter
i2c-2   smbus           SMBus PIIX4 adapter port 3 at 0b00      SMBus adapter
i2c-0   smbus           SMBus PIIX4 adapter port 0 at 0b00      SMBus adapter
i2c-9   i2c             AMDGPU DM i2c hw bus 3                  I2C adapter
i2c-7   i2c             dmdc                                    I2C adapter
i2c-5   i2c             dmdc                                    I2C adapter
```
Here we can see this module "AURA GPU adapter" is detected as device number 11. We can now scan that device with:
```
sudo i2cdetect -y 11
```
It should output all clients available on that bus:
```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- 08 -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- 29 -- -- -- -- -- --
30: 30 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- --
70: 70 -- -- -- -- -- -- --   
```
