import matplotlib.pyplot as plt
from astropy.io import fits
import pandas
starSystem1= fits.open('C:\\Users\\acer\\Desktop\\my folder\\PyCharm Community Edition 2022.2.2\\Rishi_1.fits')   #storing star system data in this variable
starSystem2= fits.open('C:\\Users\\acer\\Desktop\\my folder\\PyCharm Community Edition 2022.2.2\\Rishi_2.fits')   #storing star system data in this variable
starSystem3= fits.open('C:\\Users\\acer\\Desktop\\my folder\\PyCharm Community Edition 2022.2.2\\Rachna.fits')    #storing star system data in this variable
starSystem4= fits.open('C:\\Users\\acer\\Desktop\\my folder\\PyCharm Community Edition 2022.2.2\\Ankur.fits')     #storing star system data in this variable
starSystem5= fits.open('C:\\Users\\acer\\Desktop\\my folder\\PyCharm Community Edition 2022.2.2\\Arush.fits')     #storing star system data in this variable
starSystem6= fits.open('C:\\Users\\acer\\Desktop\\my folder\\PyCharm Community Edition 2022.2.2\\kushagra.fits')  #storing star system data in this variable
starSystems = [starSystem1,starSystem2,starSystem3,starSystem4,starSystem5,starSystem6]
def drawing_graph(k) :                                                                                            #this is the function used to Lighcurves of all the star systems
    df=pandas.DataFrame(starSystems[k][1].data)                                                                   #converting Lightcurve data into DataFrame
    plt.plot(df.loc[:,df.columns[1]],df.loc[:,df.columns[7]])                                                     #plotting points on curve
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[3])
    plt.title("star system " + str(k+1))
    plt.show()

a=0
while a<6:                                                                                                        #drawing graph for all 6 star systems
    drawing_graph(a)
    a+=1

print("Q1) 1. From the graph we can onclude that Rachna,Ankur,Arush,Kushagra supports exoplanets")

