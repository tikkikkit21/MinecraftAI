from javascript import require, On
import math
import numpy as np
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
viewer = require('prismarine-viewer')
Vec3 = require('Vec3')
item = require('prismarine-item')('1.20')

RANGE_GOAL = 1
BOT_USERNAME = 'TikkiIsDifferent' # Email here if using account
BOT_PASSWORD = '' # Password here if using account

bot = mineflayer.createBot({
  'host': '127.0.0.1',
  'port': 25565,
  'username': BOT_USERNAME
#   'password': BOT_PASSWORD # If using an actual account, uncomment this.
})

bot.loadPlugin(pathfinder.pathfinder)
print("Started mineflayer")

class Movement():
    def __init__(self):
        self.bot = bot

    def moveForward(self):
        self.bot.setControlState('forward', True)

    def moveBackward(self):
        self.bot.setControlState('back', True)

    def moveLeft(self):
        self.bot.setControlState('left', True)

    def moveRight(self):
        self.bot.setControlState('right', True)

    def jump(self):
        self.bot.setControlState('jump', True)
        self.bot.setControlState('jump', False)

    def sneak(self):
        self.bot.setControlState('sneak', True)

    def stop(self):
        self.bot.clearControlStates()

class Hands():
    def __init__(self):
        self.bot = bot
        
    def attack(self):
        entity = self.bot.nearestEntity()
        if entity:
            self.bot.attack(entity, True)
        else:
            print("no entities nearby")
    
    def destroyBlock(self):
        self.bot.stopDigging()
        block = self.bot.blockAtCursor(4)
        if block and not self.bot.targetDigBlock:
            if self.bot.canDigBlock(block):
                self.bot.dig(block, False)
            else:
                print("Bot cannot mine this block.")
        else:
            print("No block within range of sight (must be within 4 blocks inclusively)")
    
    
    def placeBlock(self): # Doesn't work properly for now...
        block = self.bot.blockAtCursor(4)
        heldItem = self.bot.heldItem
        # canPlaceOnBlocks = []
        # if heldItem:
        #     canPlaceOnBlocks = heldItem.blocksCanPlaceOn
        #     print(heldItem)
        #     print("hola como esta")
        #     print(canPlaceOnBlocks)
        if block and not self.bot.targetDigBlock:
            self.bot.placeBlock(block, Vec3(0,1,0))
        else:
            print("No block within range of sight to place block on.")

class Head():
    def __init__(self):
        self.bot = bot
        self.yaw = 0
        self.pitch = 0

    def rotateLeft(self):
        self.yaw = (self.yaw + (math.pi / 12)) % (2*math.pi)
        self.bot.look(self.yaw, self.pitch, True)

    def rotateRight(self):
        self.yaw = (self.yaw - (math.pi / 12)) % (2*math.pi)
        self.bot.look(self.yaw, self.pitch, True)

    def rotateUp(self):
        self.pitch = (self.pitch + (math.pi / 12))
        if self.pitch > math.pi / 2:
            self.pitch = math.pi / 2
        self.bot.look(self.yaw, self.pitch, True)
        
    def rotateDown(self):
        self.pitch = (self.pitch - (math.pi / 12))
        if self.pitch < -( math.pi / 2):
            self.pitch = -(math.pi / 2)
        self.bot.look(self.yaw, self.pitch, True)


@On(bot, 'spawn')
def handle(*args):
    bot.look(0, 0, True)
    bot.chat("Hello")


@On(bot, 'blockPlaced')
def handle(*args):
    print("LEN ARGS")
    print(len(args))
    # for i, arg in enumerate(args):
    #     print(i)
    #     print(arg)
    print(args[1])
    print(args[2])
    
