# Taken from an old script. The old one is more horrible if you are wondering.
if __name__ == "__main__":
    print("Do NOT execute this script directly. Execute the acrpy.py at the parent directory.")
import collections,numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl
from matplotlib.animation import FuncAnimation
import random
arrayLen = 1000

circpos = 0
contractSymbol = ""
updated = False

coolGraph = True

g_PriceHistory = collections.deque(np.zeros(arrayLen))

def graphAnim(i=0):
    global updated
    global normalGraph
    global pieChart
    global coolGraph
    global g_PriceHistory
    global circpos
    global contractSymbol
    if not updated:
        return
    normalGraph.cla()

    if coolGraph:
        # Use this combined with updated = true for a more cooler effect if you don't value your resources.
        #if circpos < 0:
        #    circpos = 360
        #circpos -= 0.2
        
        circpos =  random.randint(0, 360)
        pieChart.cla()
        pieChart.pie([g_PriceHistory[-1],2],startangle=circpos,counterclock=False,radius=1,colors=['#787878', 'black']) 
        pieChart.pie([1,1],radius=0.95,colors=['black','black'])
        pieChart.pie([g_PriceHistory[-1],2],startangle=60-circpos*2.2,counterclock=True,radius=0.85,colors=['#787878', 'black'])
        pieChart.pie([1,1],radius=0.80,colors=['black','black'])
        pieChart.pie([g_PriceHistory[-1],2],startangle=60-circpos*1.8,counterclock=True,radius=0.75,colors=['#787878', 'black'])
        pieChart.pie([1,1],radius=0.70,colors=['black','black'])
        pieChart.pie([g_PriceHistory[-1],2],startangle=70+circpos*-5.7,counterclock=True,radius=0.65,colors=['#787878', 'black'])
        pieChart.pie([1,1],radius=0.60,colors=['black','black'])
        pieChart.pie([g_PriceHistory[-1],2],startangle=70+circpos*3,counterclock=True,radius=0.55,colors=['#787878', 'black'])
        pieChart.pie([1,1],radius=0.50,colors=['black','black'])
        pieChart.pie([g_PriceHistory[-1],2],startangle=circpos*10.6,counterclock=False,radius=0.45,colors=['#787878', 'black'])
        pieChart.pie([1,1],radius=0.40,colors=['black','black'])
        pieChart.pie([g_PriceHistory[-1],2],startangle=circpos*-5.5,counterclock=False,radius=0.35,colors=['#787878', 'black'])
        pieChart.pie([1,1],radius=0.30,colors=['black','black'])
        pieChart.pie([g_PriceHistory[-1],2],startangle=circpos*8.2,counterclock=True,radius=0.25,colors=['#787878', 'black'])
        pieChart.pie([1,1],radius=0.20,colors=['black','black'])
    plt.title('${} price {}'.format(contractSymbol,g_PriceHistory[-1]))
    
    
    normalGraph.plot(g_PriceHistory)
    normalGraph.scatter(len(g_PriceHistory)-1, g_PriceHistory[-1])
    normalGraph.text(len(g_PriceHistory)-1, g_PriceHistory[-1]+2, "{}%".format(g_PriceHistory[-1]))
    normalGraph.set_ylim(g_PriceHistory[-1]*0.9,g_PriceHistory[-1]+g_PriceHistory[-1]*0.1)
    normalGraph.set_xlim(len(g_PriceHistory)-50,len(g_PriceHistory))
    updated = False



fig = any
normalGraph = any
pieChart = any
ani = any


def initanim():
    global fig,normalGraph,pieChart, ani
    mpl.style.use("dark_background")
    fig = plt.figure(figsize=(12,6), facecolor='black')
    normalGraph = plt.subplot(121)
    pieChart = plt.subplot(122)
    normalGraph.set_facecolor('black')
    ani = FuncAnimation(fig, graphAnim, interval=150, save_count=10)

def addPrice(price: float):
    global g_PriceHistory, arrayLen, updated
    if g_PriceHistory[arrayLen -1] == price:
        return
    g_PriceHistory.popleft()
    g_PriceHistory.append(price)
    updated = True

def setGraphSymbol(symbol: str):
    global contractSymbol
    contractSymbol = symbol

def startGraphThread():
    global plt
    plt.show()
