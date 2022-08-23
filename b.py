from random import randint
class duycoin:
    def __init__(self,release,name,release_probably) -> None:
        # price in usd
        self.price=0
        self.name=name
        self.release=release
        self.release_probably=release_probably
        print('Created',name+'\nCost: 0\nRelease:',release)
    def buy(self,coins):
        if coins<=self.release:
            print('Buying', coins)
            self.price+=0.001*coins
            self.release-=coins
            print(self.name,'cost',self.price,'; remain',self.release)
            self.release_new()
            return 1
        else:
            return 0
    def cell(self,coins):
        print('Celling', coins)
        self.price-=0.001*coins
        self.release+=coins
        print(self.name,'cost',self.price,'; remain',self.release)
        self.release_new()
    def release_new(self):
        if not randint(0,self.release_probably):
            self.release+=1
            print('Released 1 coin!')

dugduy=duycoin(100,'DugDuy coin',3)
for i in range(5):
    dugduy.buy(randint(0,4))
# print(dugduy.price)