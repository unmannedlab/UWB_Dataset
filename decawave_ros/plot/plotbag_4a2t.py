import rosbag
import rospy
import matplotlib
#matplotlib.use("pgf")

from decawave_ros.msg import uwb_distance
import matplotlib.pyplot as plt

#plt.style.use('seaborn')
plt.rcParams.update({
    #"pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    #'pgf.rcfonts': False,
    # Use 10pt font in plots, to match 10pt font in document
    "axes.labelsize": 10,
    "font.size": 10,
    # Make the legend/label fonts a little smaller
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8
})

def set_size(width_in, fraction=1, subplots=(1, 1)):
    """Set figure dimensions to sit nicely in our document.

    Parameters
    ----------
    width_pt: float
            Document width in points
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure (in pts)
    #fig_width_pt = width_pt * fraction
    fig_width_in = width_in * fraction
    # Convert from pt to inches
    #inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    #fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)


bag = rosbag.Bag('/media/jh/easystore/uwb_bags/2023-02-10-15-23-44_0.bag')
# Initialize some empty lists for storing the data
dist_a0t0 = []
dist_a1t0 = []
dist_a2t0 = []
dist_a3t0 = []
time_a0t0 = []
time_a1t0 = []
time_a2t0 = []
time_a3t0 = []

dist_a0t1 = []
dist_a1t1 = []
dist_a2t1 = []
dist_a3t1 = []
time_a0t1 = []
time_a1t1 = []
time_a2t1 = []
time_a3t1 = []

dist_a0t2 = []
dist_a1t2 = []
dist_a2t2 = []
dist_a3t2 = []
time_a0t2 = []
time_a1t2 = []
time_a2t2 = []
time_a3t2 = []

dist_a0t3 = []
dist_a1t3 = []
dist_a2t3 = []
dist_a3t3 = []
time_a0t3 = []
time_a1t3 = []
time_a2t3 = []
time_a3t3 = []

dist_a0t4 = []
dist_a1t4 = []
dist_a2t4 = []
dist_a3t4 = []
time_a0t4 = []
time_a1t4 = []
time_a2t4 = []
time_a3t4 = []

dist_a0t5 = []
dist_a1t5 = []
dist_a2t5 = []
dist_a3t5 = []
time_a0t5 = []
time_a1t5 = []
time_a2t5 = []
time_a3t5 = []

def ax_plot(ax, x, y , ylabel,):
    ax.scatter(x,y, s=10, color='deepskyblue', marker='.')
    ax.set_xlabel('Time(s)')
    ax.set_ylabel(ylabel)
    ax.grid(which='major', color='#DDDDDD', linewidth=0.8)
    ax.tick_params(axis="x", direction="in")
    ax.tick_params(axis="y", direction="in")
    ax.set_xlim(0,20)
    #ax.set_ylim(0,65)


start_time_bag = bag.get_start_time()
#print(start_time_bag)  #float 
time_1 = float(28)
time_2 = float(48)
start_time=rospy.Time(start_time_bag+time_1)
end_time=rospy.Time(start_time_bag+time_2)

for topic,msg,t in bag.read_messages(topics=['/Decawave'], start_time=start_time, end_time=end_time):
    #print(msg)
    #print(type(t))  # class 'rospy.rostime.Time'
    t = t-start_time
    
    if msg.tag==0:
        #print(len(msg.dist_array))
        if len(msg.dist_array) == 4:
            time_a0t0.append(t.to_sec())
            dist_a0t0.append(msg.dist_array[0].dist)
            
            time_a1t0.append(t.to_sec())
            dist_a1t0.append(msg.dist_array[1].dist)
            
            time_a2t0.append(t.to_sec())
            dist_a2t0.append(msg.dist_array[2].dist)
           
            time_a3t0.append(t.to_sec())
            dist_a3t0.append(msg.dist_array[3].dist)

        if len(msg.dist_array) == 3:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t0.append(t.to_sec())
                dist_a0t0.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t0.append(t.to_sec())
                    dist_a1t0.append(msg.dist_array[1].dist)
                    if msg.dist_array[2].anc==2:
                        time_a2t0.append(t.to_sec())
                        dist_a2t0.append(msg.dist_array[2].dist)
                    if msg.dist_array[2].anc==3:
                        time_a3t0.append(t.to_sec())
                        dist_a3t0.append(msg.dist_array[2].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t0.append(t.to_sec())
                    dist_a2t0.append(msg.dist_array[1].dist)
                    time_a3t0.append(t.to_sec())
                    dist_a3t0.append(msg.dist_array[2].dist)  

            if msg.dist_array[0].anc==1:
                time_a1t0.append(t.to_sec())
                dist_a1t0.append(msg.dist_array[0].dist)
                time_a2t0.append(t.to_sec())
                dist_a2t0.append(msg.dist_array[1].dist)
                time_a3t0.append(t.to_sec())
                dist_a3t0.append(msg.dist_array[2].dist)  

        if len(msg.dist_array) == 2:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t0.append(t.to_sec())
                dist_a0t0.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t0.append(t.to_sec())
                    dist_a1t0.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t0.append(t.to_sec())
                    dist_a2t0.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t0.append(t.to_sec())
                    dist_a3t0.append(msg.dist_array[1].dist)
            
            if msg.dist_array[0].anc==1:
                time_a1t0.append(t.to_sec())
                dist_a1t0.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t0.append(t.to_sec())
                    dist_a2t0.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t0.append(t.to_sec())
                    dist_a3t0.append(msg.dist_array[1].dist)

        if len(msg.dist_array) == 1:
            if msg.dist_array[0].anc==0:
                time_a0t0.append(t.to_sec())
                dist_a0t0.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==1:
                time_a1t0.append(t.to_sec())
                dist_a1t0.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==2:
                time_a2t0.append(t.to_sec())
                dist_a2t0.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==3:
                time_a3t0.append(t.to_sec())
                dist_a3t0.append(msg.dist_array[0].dist)

        if len(msg.dist_array) == 0:
            continue 
    if msg.tag==1:
        #print(len(msg.dist_array))
        if len(msg.dist_array) == 4:
            time_a0t1.append(t.to_sec())
            dist_a0t1.append(msg.dist_array[0].dist)
            
            time_a1t1.append(t.to_sec())
            dist_a1t1.append(msg.dist_array[1].dist)
            
            time_a2t1.append(t.to_sec())
            dist_a2t1.append(msg.dist_array[2].dist)
           
            time_a3t1.append(t.to_sec())
            dist_a3t1.append(msg.dist_array[3].dist)

        if len(msg.dist_array) == 3:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t1.append(t.to_sec())
                dist_a0t1.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t1.append(t.to_sec())
                    dist_a1t1.append(msg.dist_array[1].dist)
                    if msg.dist_array[2].anc==2:
                        time_a2t1.append(t.to_sec())
                        dist_a2t1.append(msg.dist_array[2].dist)
                    if msg.dist_array[2].anc==3:
                        time_a3t1.append(t.to_sec())
                        dist_a3t1.append(msg.dist_array[2].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t1.append(t.to_sec())
                    dist_a2t1.append(msg.dist_array[1].dist)
                    time_a3t1.append(t.to_sec())
                    dist_a3t1.append(msg.dist_array[2].dist)  

            if msg.dist_array[0].anc==1:
                time_a1t1.append(t.to_sec())
                dist_a1t1.append(msg.dist_array[0].dist)
                time_a2t1.append(t.to_sec())
                dist_a2t1.append(msg.dist_array[1].dist)
                time_a3t1.append(t.to_sec())
                dist_a3t1.append(msg.dist_array[2].dist)  

        if len(msg.dist_array) == 2:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t1.append(t.to_sec())
                dist_a0t1.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t1.append(t.to_sec())
                    dist_a1t1.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t1.append(t.to_sec())
                    dist_a2t1.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t1.append(t.to_sec())
                    dist_a3t1.append(msg.dist_array[1].dist)
            
            if msg.dist_array[0].anc==1:
                time_a1t1.append(t.to_sec())
                dist_a1t1.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t1.append(t.to_sec())
                    dist_a2t1.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t1.append(t.to_sec())
                    dist_a3t1.append(msg.dist_array[1].dist)

        if len(msg.dist_array) == 1:
            if msg.dist_array[0].anc==0:
                time_a0t1.append(t.to_sec())
                dist_a0t1.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==1:
                time_a1t1.append(t.to_sec())
                dist_a1t1.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==2:
                time_a2t1.append(t.to_sec())
                dist_a2t1.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==3:
                time_a3t1.append(t.to_sec())
                dist_a3t1.append(msg.dist_array[0].dist)

        if len(msg.dist_array) == 0:
            continue 
    if msg.tag==2:
        #print(len(msg.dist_array))
        if len(msg.dist_array) == 4:
            time_a0t2.append(t.to_sec())
            dist_a0t2.append(msg.dist_array[0].dist)
            
            time_a1t2.append(t.to_sec())
            dist_a1t2.append(msg.dist_array[1].dist)
            
            time_a2t2.append(t.to_sec())
            dist_a2t2.append(msg.dist_array[2].dist)
           
            time_a3t2.append(t.to_sec())
            dist_a3t2.append(msg.dist_array[3].dist)

        if len(msg.dist_array) == 3:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t2.append(t.to_sec())
                dist_a0t2.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t2.append(t.to_sec())
                    dist_a1t2.append(msg.dist_array[1].dist)
                    if msg.dist_array[2].anc==2:
                        time_a2t2.append(t.to_sec())
                        dist_a2t2.append(msg.dist_array[2].dist)
                    if msg.dist_array[2].anc==3:
                        time_a3t2.append(t.to_sec())
                        dist_a3t2.append(msg.dist_array[2].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t2.append(t.to_sec())
                    dist_a2t2.append(msg.dist_array[1].dist)
                    time_a3t2.append(t.to_sec())
                    dist_a3t2.append(msg.dist_array[2].dist)  

            if msg.dist_array[0].anc==1:
                time_a1t2.append(t.to_sec())
                dist_a1t2.append(msg.dist_array[0].dist)
                time_a2t2.append(t.to_sec())
                dist_a2t2.append(msg.dist_array[1].dist)
                time_a3t2.append(t.to_sec())
                dist_a3t2.append(msg.dist_array[2].dist)  

        if len(msg.dist_array) == 2:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t2.append(t.to_sec())
                dist_a0t2.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t2.append(t.to_sec())
                    dist_a1t2.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t2.append(t.to_sec())
                    dist_a2t2.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t2.append(t.to_sec())
                    dist_a3t2.append(msg.dist_array[1].dist)
            
            if msg.dist_array[0].anc==1:
                time_a1t2.append(t.to_sec())
                dist_a1t2.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t2.append(t.to_sec())
                    dist_a2t2.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t2.append(t.to_sec())
                    dist_a3t2.append(msg.dist_array[1].dist)

        if len(msg.dist_array) == 1:
            if msg.dist_array[0].anc==0:
                time_a0t2.append(t.to_sec())
                dist_a0t2.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==1:
                time_a1t2.append(t.to_sec())
                dist_a1t2.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==2:
                time_a2t2.append(t.to_sec())
                dist_a2t2.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==3:
                time_a3t2.append(t.to_sec())
                dist_a3t2.append(msg.dist_array[0].dist)

        if len(msg.dist_array) == 0:
            continue
    if msg.tag==3:
        #print(len(msg.dist_array))
        if len(msg.dist_array) == 4:
            time_a0t3.append(t.to_sec())
            dist_a0t3.append(msg.dist_array[0].dist)
            
            time_a1t3.append(t.to_sec())
            dist_a1t3.append(msg.dist_array[1].dist)
            
            time_a2t3.append(t.to_sec())
            dist_a2t3.append(msg.dist_array[2].dist)
           
            time_a3t3.append(t.to_sec())
            dist_a3t3.append(msg.dist_array[3].dist)

        if len(msg.dist_array) == 3:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t3.append(t.to_sec())
                dist_a0t3.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t3.append(t.to_sec())
                    dist_a1t3.append(msg.dist_array[1].dist)
                    if msg.dist_array[2].anc==2:
                        time_a2t3.append(t.to_sec())
                        dist_a2t3.append(msg.dist_array[2].dist)
                    if msg.dist_array[2].anc==3:
                        time_a3t3.append(t.to_sec())
                        dist_a3t3.append(msg.dist_array[2].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t3.append(t.to_sec())
                    dist_a2t3.append(msg.dist_array[1].dist)
                    time_a3t3.append(t.to_sec())
                    dist_a3t3.append(msg.dist_array[2].dist)  

            if msg.dist_array[0].anc==1:
                time_a1t3.append(t.to_sec())
                dist_a1t3.append(msg.dist_array[0].dist)
                time_a2t3.append(t.to_sec())
                dist_a2t3.append(msg.dist_array[1].dist)
                time_a3t3.append(t.to_sec())
                dist_a3t3.append(msg.dist_array[2].dist)  

        if len(msg.dist_array) == 2:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t3.append(t.to_sec())
                dist_a0t3.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t3.append(t.to_sec())
                    dist_a1t3.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t3.append(t.to_sec())
                    dist_a2t3.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t3.append(t.to_sec())
                    dist_a3t3.append(msg.dist_array[1].dist)
            
            if msg.dist_array[0].anc==1:
                time_a1t3.append(t.to_sec())
                dist_a1t3.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t3.append(t.to_sec())
                    dist_a2t3.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t3.append(t.to_sec())
                    dist_a3t3.append(msg.dist_array[1].dist)

        if len(msg.dist_array) == 1:
            if msg.dist_array[0].anc==0:
                time_a0t3.append(t.to_sec())
                dist_a0t3.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==1:
                time_a1t3.append(t.to_sec())
                dist_a1t3.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==2:
                time_a2t3.append(t.to_sec())
                dist_a2t3.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==3:
                time_a3t3.append(t.to_sec())
                dist_a3t3.append(msg.dist_array[0].dist)

        if len(msg.dist_array) == 0:
            continue
    if msg.tag==4:
        #print(len(msg.dist_array))
        if len(msg.dist_array) == 4:
            time_a0t4.append(t.to_sec())
            dist_a0t4.append(msg.dist_array[0].dist)
            
            time_a1t4.append(t.to_sec())
            dist_a1t4.append(msg.dist_array[1].dist)
            
            time_a2t4.append(t.to_sec())
            dist_a2t4.append(msg.dist_array[2].dist)
           
            time_a3t4.append(t.to_sec())
            dist_a3t4.append(msg.dist_array[3].dist)

        if len(msg.dist_array) == 3:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t4.append(t.to_sec())
                dist_a0t4.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t4.append(t.to_sec())
                    dist_a1t4.append(msg.dist_array[1].dist)
                    if msg.dist_array[2].anc==2:
                        time_a2t4.append(t.to_sec())
                        dist_a2t4.append(msg.dist_array[2].dist)
                    if msg.dist_array[2].anc==3:
                        time_a3t4.append(t.to_sec())
                        dist_a3t4.append(msg.dist_array[2].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t4.append(t.to_sec())
                    dist_a2t4.append(msg.dist_array[1].dist)
                    time_a3t4.append(t.to_sec())
                    dist_a3t4.append(msg.dist_array[2].dist)  

            if msg.dist_array[0].anc==1:
                time_a1t4.append(t.to_sec())
                dist_a1t4.append(msg.dist_array[0].dist)
                time_a2t4.append(t.to_sec())
                dist_a2t4.append(msg.dist_array[1].dist)
                time_a3t4.append(t.to_sec())
                dist_a3t4.append(msg.dist_array[2].dist)  

        if len(msg.dist_array) == 2:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t4.append(t.to_sec())
                dist_a0t4.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t4.append(t.to_sec())
                    dist_a1t4.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t4.append(t.to_sec())
                    dist_a2t4.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t4.append(t.to_sec())
                    dist_a3t4.append(msg.dist_array[1].dist)
            
            if msg.dist_array[0].anc==1:
                time_a1t4.append(t.to_sec())
                dist_a1t4.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t4.append(t.to_sec())
                    dist_a2t4.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t4.append(t.to_sec())
                    dist_a3t4.append(msg.dist_array[1].dist)

        if len(msg.dist_array) == 1:
            if msg.dist_array[0].anc==0:
                time_a0t4.append(t.to_sec())
                dist_a0t4.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==1:
                time_a1t4.append(t.to_sec())
                dist_a1t4.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==2:
                time_a2t4.append(t.to_sec())
                dist_a2t4.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==3:
                time_a3t4.append(t.to_sec())
                dist_a3t4.append(msg.dist_array[0].dist)

        if len(msg.dist_array) == 0:
            continue
    if msg.tag==5:
        #print(len(msg.dist_array))
        if len(msg.dist_array) == 4:
            time_a0t5.append(t.to_sec())
            dist_a0t5.append(msg.dist_array[0].dist)
            
            time_a1t5.append(t.to_sec())
            dist_a1t5.append(msg.dist_array[1].dist)
            
            time_a2t5.append(t.to_sec())
            dist_a2t5.append(msg.dist_array[2].dist)
           
            time_a3t5.append(t.to_sec())
            dist_a3t5.append(msg.dist_array[3].dist)

        if len(msg.dist_array) == 3:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t5.append(t.to_sec())
                dist_a0t5.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t5.append(t.to_sec())
                    dist_a1t5.append(msg.dist_array[1].dist)
                    if msg.dist_array[2].anc==2:
                        time_a2t5.append(t.to_sec())
                        dist_a2t5.append(msg.dist_array[2].dist)
                    if msg.dist_array[2].anc==3:
                        time_a3t5.append(t.to_sec())
                        dist_a3t5.append(msg.dist_array[2].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t5.append(t.to_sec())
                    dist_a2t5.append(msg.dist_array[1].dist)
                    time_a3t5.append(t.to_sec())
                    dist_a3t5.append(msg.dist_array[2].dist)  

            if msg.dist_array[0].anc==1:
                time_a1t5.append(t.to_sec())
                dist_a1t5.append(msg.dist_array[0].dist)
                time_a2t5.append(t.to_sec())
                dist_a2t5.append(msg.dist_array[1].dist)
                time_a3t5.append(t.to_sec())
                dist_a3t5.append(msg.dist_array[2].dist)  

        if len(msg.dist_array) == 2:
            print(msg)
            if msg.dist_array[0].anc==0:
                time_a0t5.append(t.to_sec())
                dist_a0t5.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==1:
                    time_a1t5.append(t.to_sec())
                    dist_a1t5.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t5.append(t.to_sec())
                    dist_a2t5.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t5.append(t.to_sec())
                    dist_a3t5.append(msg.dist_array[1].dist)
            
            if msg.dist_array[0].anc==1:
                time_a1t5.append(t.to_sec())
                dist_a1t5.append(msg.dist_array[0].dist)
                if msg.dist_array[1].anc==2:
                    time_a2t5.append(t.to_sec())
                    dist_a2t5.append(msg.dist_array[1].dist)
                if msg.dist_array[1].anc==3:
                    time_a3t5.append(t.to_sec())
                    dist_a3t5.append(msg.dist_array[1].dist)

        if len(msg.dist_array) == 1:
            if msg.dist_array[0].anc==0:
                time_a0t5.append(t.to_sec())
                dist_a0t5.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==1:
                time_a1t5.append(t.to_sec())
                dist_a1t5.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==2:
                time_a2t5.append(t.to_sec())
                dist_a2t5.append(msg.dist_array[0].dist)
            if msg.dist_array[0].anc==3:
                time_a3t5.append(t.to_sec())
                dist_a3t5.append(msg.dist_array[0].dist)

        if len(msg.dist_array) == 0:
            continue

bag.close()
# Plot
# Define X and Y variable data
text_width_in = 6.13899

plt.figure(figsize=set_size(text_width_in, subplots=(1, 1)))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
ax1=plt.subplot(1,1,1)
ax_plot(ax1,time_a0t0,dist_a0t0,ylabel='A0-T0\nDistance(m)')
'''
plt.figure(figsize=set_size(text_width_in, subplots=(2, 2)))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
ax1=plt.subplot(2,2,1)
ax_plot(ax1,time_a0t0,dist_a0t0,ylabel='A0-T0\nDistance(m)')
ax2=plt.subplot(2,2,2)
ax_plot(ax2,time_a1t0,dist_a1t0,ylabel='A1-T0\nDistance(m)')
ax3=plt.subplot(2,2,3)
ax_plot(ax3,time_a2t0,dist_a2t0,ylabel='A2-T0\nDistance(m)')
ax4=plt.subplot(2,2,4)
ax_plot(ax4,time_a3t0,dist_a3t0,ylabel='A3-T0\nDistance(m)')
'''
'''
#good for customize the whole figure, better
fig, [(ax1,ax2),(ax3,ax4)] = plt.subplots(2, 2, figsize=set_size(text_width_in, subplots=(2, 2)))
ax1.set_xlim(0,65)
ax1.set_xlabel('Time(s)')
ax1.set_ylabel('A0-T0 Range(m)')
'''
#plt.suptitle('Distance_4a2t_4agolfcartmoving_tagsmoving_outdoor')
plt.savefig('s2.png')
plt.show()
