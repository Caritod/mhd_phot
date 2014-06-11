from huachoUtils import *
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import ImageGrid
from matplotlib.colors import LogNorm


mpl.rc('xtick',labelsize=8)
mpl.rc('ytick',labelsize=8)
mpl.rc('text',usetex=True)
#mpl.rc('font',**{'family':'serif','serif':['Computer Modern']})

def add_inner_title(ax, title, loc, size=None, **kwargs):
    from matplotlib.offsetbox import AnchoredText
    from matplotlib.patheffects import withStroke
    if size is None:
        size = dict(size=plt.rcParams['ytick.labelsize'])
    at = AnchoredText(title, loc=loc, prop=size,
                      pad=0., borderpad=0.5,
                      frameon=False, **kwargs)
    ax.add_artist(at)
    at.txt._text.set_path_effects([withStroke(foreground="w", linewidth=2)])
    return at


nxtot=400
nytot=8
nztot=8
mpiX=8
mpiY=1
mpiZ=1
neqs=10


cv=100.
gam=(cv+1.)/cv
vsc=1.
psc=1.

firstrun=True
plt.ion()


path='/Users/esquivel/Desktop/Storage-Diable/MHD-EXO/BIN/'


for nout in range(4,5):
    #  this is the ionization rate
    if (firstrun):
        denT= coplot3d(2,nytot/2,0,neqs,nxtot,nytot,nztot,mpiX,mpiY,mpiZ,nout,path=path)
        vx=   coplot3d(2,nytot/2,1,neqs,nxtot,nytot,nztot,mpiX,mpiY,mpiZ,nout,path=path)/denT
        vy=   coplot3d(2,nytot/2,2,neqs,nxtot,nytot,nztot,mpiX,mpiY,mpiZ,nout,path=path)/denT
        Etot= coplot3d(2,nytot/2,4,neqs,nxtot,nytot,nztot,mpiX,mpiY,mpiZ,nout,path=path)
        bx=   coplot3d(2,nytot/2,5,neqs,nxtot,nytot,nztot,mpiX,mpiY,mpiZ,nout,path=path)
        by=   coplot3d(2,nytot/2,6,neqs,nxtot,nytot,nztot,mpiX,mpiY,mpiZ,nout,path=path)
        #bz=   coplot3d(2,nytot/2,7,neqs,nxtot,nytot,nztot,mpiX,mpiY,mpiZ,nout,path=path)
        #denN= coplot3d(2,nytot/2,8,neqs,nxtot,nytot,nztot,mpiX,mpiY,mpiZ,nout,path=path)
        Pgas=  Etot-0.5*(denT*(vx*vx+vy*vy)+bx*bx+by*by)


    plt.clf()

    plt.subplot(3, 2, 1)
    plt.plot(denT[4,::],'-ro')
    plt.title(r'$\rho$')

    plt.subplot(3, 2, 2)
    plt.plot(Pgas[4,::],'-ro')
    plt.title(r'$P_{gas}$')

    plt.subplot(3, 2, 3)
    plt.plot(vx[4,::],'-ro')
    plt.title(r'$v_{x}$')

    plt.subplot(3, 2, 4)
    plt.plot(vy[4,::],'-ro')
    plt.title(r'$v_{y}$')

    plt.subplot(3, 2, 5)
    plt.plot(by[4,::],'-ro')
    plt.title(r'$B_{x}$')

    plt.subplot(3, 2, 6)
    plt.plot(Etot[4,::]/denT[4,::],'-ro')
    plt.title(r'$E_{tot}/\rho$')

#plt.ioff()
