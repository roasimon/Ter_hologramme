import pickle
import matplotlib.pyplot as plt

def show_figure(fig):

    # create a dummy figure and use its
    # manager to display "fig"  
    dummy = plt.figure()
    new_manager = dummy.canvas.manager
    new_manager.canvas.figure = fig
    fig.set_canvas(new_manager.canvas)

if __name__ == '__main__':
    with open('S_H.fig.pickle', 'rb') as f:
        fig = pickle.load(f)
        show_figure(fig)
        plt.show()
