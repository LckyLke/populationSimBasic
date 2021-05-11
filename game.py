from blop import Blop
import numpy as np
import random as rd

class Game:
    def __init__(self, number_of_blops, blocksize):
        self.number_of_blop = number_of_blops
        self.blopsGreen = np.array([Blop("Green", {'x': blocksize * 10, 'y':blocksize*10}, blocksize) for _ in range(number_of_blops//2)])
        self.blopsRed = np.array([Blop("Red", {'x': blocksize*90, 'y':blocksize*90}, blocksize) for _ in range(number_of_blops//2)])
        self.blocksize = blocksize

    def collsion(self):



        for i, blop in enumerate(self.blopsGreen):

            for ir, blopR in enumerate(self.blopsRed):
                if blop.position == blopR.position:
                    if rd.random() > .5:

                        self.blopsRed = np.delete(self.blopsRed, ir)
                        self.blopsGreen = np.append(self.blopsGreen, [Blop('Green', blop.position, self.blocksize)])
                        print(self.blopsRed.size, " Red blobs")
                        print(self.blopsGreen.size, " Green blobs")
                        return
                    if rd.random() < .5:
                        print(self.blopsRed.size, " Red blobs")
                        print(self.blopsGreen.size, " Green blobs")
                        self.blopsGreen = np.delete(self.blopsGreen, i)
                        self.blopsRed = np.append(self.blopsRed, [Blop('Red', blopR.position, self.blocksize)])
                        return