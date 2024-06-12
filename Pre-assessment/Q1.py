
def removeGroups(object):

    def __init__(self, fruitDict):
        self.fruit = fruitDict

    def removeBerries(self, fruitDict):
        berrystack = []
        for i in self.fruit:
            berrystack.append(i)
            if 'berry' in i:
                berrystack.pop()
        print(f'Fruits that are not berries: {berrystack}')
    

def main():
    fruitDict = ['apple', 'banana', 'cherry', 'strawberry', 'kiwi',
                  'mango', 'blueberry', 'raspberry', 'plum', 'orange',
                    'blackberry', 'pear', 'peach', 'avocado', 'cranberry']
    removeGroups.removeBerries(fruitDict)

if __name__ == "__main__":
    main()
                