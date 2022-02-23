"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
import numpy as np


def visualize(data_dict):
    """Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    fig.tight_layout()

    plt.show()


def textualize(statistics_dict):
    """Generate a textual representation of statistics

    :param data_dict: Dictionary of statistics -> data to present as text
    """

    Statistics_text = ""

    for key in statistics_dict:
        Statistics_text += ("{} value for the data is {}. ".format(key,statistics_dict[key]))

    print(Statistics_text)

    return(Statistics_text)