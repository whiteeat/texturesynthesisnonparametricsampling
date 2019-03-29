import textureSynthesis as ts
import time

if __name__ == '__main__':
    #PUT YOUR PARAMETERS HERE
    exampleMapPath = "imgs/1.jpg"
    outputSize = [75,75]
    outputPath = "out/test/"
    searchKernelSize = 15

    start_time = time.time()
    ts.textureSynthesis(exampleMapPath, outputSize, searchKernelSize, outputPath, attenuation=80, truncation=0.8, snapshots=False)
    print("It takes: {:4f}s.".format(time.time() - start_time))