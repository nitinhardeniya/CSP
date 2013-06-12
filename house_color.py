# rc = costs of painting red, bc of blue and gc of green.
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='HousePaint.log',
                    filemode='w')


class HousePaint(object):
    """docstring for HousePaint"""
    def __init__(self, no_of_house,costs_of_red,costs_of_blue,costs_of_green):
        """
        Assuming costs of 
        """
        self.n=no_of_house

        self.costs_of_red=[costs_of_red]*self.n
        self.costs_of_blue=[costs_of_blue]*self.n
        self.costs_of_green=[costs_of_green]*self.n
        self.min=[]
        
    def minimum_cost_paint(self):
        
        i=1
        
        r =[0]*self.n
        b=[0]*self.n
        g=[0]*self.n

        #Initalize 
        r[0]=self.costs_of_red[0]
        b[0]=self.costs_of_blue[0]
        g[0] = self.costs_of_green[0]
        while i < self.n:
            r[i] = self.costs_of_red[i] + min(b[i-1], g[i-1])
            b[i] = self.costs_of_blue[i] + min(r[i-1], g[i-1])
            g[i] = self.costs_of_green[i] + min(b[i-1], r[i-1])
            logging.info(r)
            logging.info(b)
            logging.info(g)
            i += 1
        self.min=min(r,b,g)
        return min(r,b,g)

    def display(self):
        res=[]
        if self.min[0]==4:
            res.append('R')
        elif self.min[0]==3:
            res.append('B') 
        elif self.min[0]==2:
            res.append('G')
        for i in range(0,len(self.min)-1):
            diff=self.min[i+1]-self.min[i]
            logging.info(diff)
            logging.info(self.costs_of_red[0])
            
            if diff==self.costs_of_red[0]:
                res.append('R')

            elif diff==self.costs_of_green[0]:
                #print res
                res.append('G')
            elif diff==self.costs_of_blue[0]:
                res.append('B')
            i=i+1
        print res

        return


if __name__ == "__main__":

    if len(sys.argv)<4:
        print "usage python house_color.py <no_of_house> <costs_of_red> <costs_of_blue> <costs_of_green>"
    no_of_house=int(sys.argv[1])
    costs_of_red=int(sys.argv[2])
    costs_of_blue=int(sys.argv[3])
    costs_of_green=int(sys.argv[4])
    #h=HousePaint(4,4,3,2)
    h=HousePaint(no_of_house,costs_of_red,costs_of_blue,costs_of_green)
    print h.minimum_cost_paint()
    h.display()