import matplotlib.pyplot as plt
import numpy as np

import helpers


def weight_speed(uavs: tuple, threshold: float = None, approx: int = None):
    if threshold is None:
        x = np.array([uav.takeoff_weight for uav in uavs
                      if uav.takeoff_weight is not None and uav.max_speed is not None])
        y = np.array([uav.max_speed for uav in uavs
                      if uav.takeoff_weight is not None and uav.max_speed is not None])
    else:
        x = np.array([uav.takeoff_weight for uav in uavs
                      if uav.takeoff_weight is not None and uav.max_speed is not None
                      and uav.takeoff_weight < threshold])
        y = np.array([uav.max_speed for uav in uavs
                      if uav.takeoff_weight is not None and uav.max_speed is not None
                      and uav.takeoff_weight < threshold])

    inscriptions = ('',
                    f"Max takeoff weight, [{uavs[0].units['max takeoff weight']}]",
                    f"Max speed, [{uavs[0].units['max speed']}]")
    # Plotting
    fig = plt.figure("Data Analysis (weight and speed)")

    x_approx, y_approx = None, None
    if approx is not None:
        x_approx = np.linspace(x.min(), x.max(), 200)
        y_approx = helpers.get_poly(x, y, approx, x_approx)
    plotting(fig, x, y, *inscriptions,
             x_approx=x_approx, y_approx=y_approx, polydeg=approx)


def speed_endurance(uavs: tuple, threshold: float = None, approx: int = None):
    if threshold is None:
        x = np.array([uav.max_speed for uav in uavs
                      if uav.max_speed is not None and uav.endurance is not None])
        y = np.array([uav.endurance for uav in uavs
                      if uav.max_speed is not None and uav.endurance is not None])
    else:
        x = np.array([uav.max_speed for uav in uavs
                      if uav.max_speed is not None and uav.endurance is not None
                      and uav.endurance < threshold])
        y = np.array([uav.endurance for uav in uavs
                      if uav.max_speed is not None and uav.endurance is not None
                      and uav.endurance < threshold])

    inscriptions = ('',
                    f"Max speed, [{uavs[0].units['max speed']}]",
                    f"Endurance, [{uavs[0].units['endurance']}]")
    # Plotting
    fig = plt.figure("Data Analysis (speed and endurance)")

    x_approx, y_approx = None, None
    if approx is not None:
        x_approx = np.linspace(x.min(), x.max(), 200)
        y_approx = helpers.get_poly(x, y, approx, x_approx)
    plotting(fig, x, y, *inscriptions,
             x_approx=x_approx, y_approx=y_approx, polydeg=approx)


def weight_payload(uavs: tuple, threshold: float = None, approx: int = None):
    if threshold is None:
        x = np.array([uav.takeoff_weight for uav in uavs
                      if uav.takeoff_weight is not None and uav.payload is not None])
        y = np.array([uav.payload for uav in uavs
                      if uav.takeoff_weight is not None and uav.payload is not None])
    else:
        x = np.array([uav.takeoff_weight for uav in uavs
                      if uav.takeoff_weight is not None and uav.payload is not None
                      and uav.payload < threshold])
        y = np.array([uav.payload for uav in uavs
                      if uav.takeoff_weight is not None and uav.payload is not None
                      and uav.payload < threshold])

    inscriptions = ('',
                    f"Max takeoff weight, [{uavs[0].units['max takeoff weight']}]",
                    f"Payload, [{uavs[0].units['payload']}]")
    # Plotting
    fig = plt.figure("Data Analysis (weight and payload)")

    x_approx, y_approx = None, None
    if approx is not None:
        x_approx = np.linspace(x.min(), x.max(), 200)
        y_approx = helpers.get_poly(x, y, approx, x_approx)
    plotting(fig, x, y, *inscriptions,
             x_approx=x_approx, y_approx=y_approx, polydeg=approx)


def weight_ceiling(uavs: tuple, threshold: float = None, approx: int = None):
    if threshold is None:
        x = np.array([uav.takeoff_weight for uav in uavs
                      if uav.takeoff_weight is not None and uav.ceiling is not None])
        y = np.array([uav.ceiling for uav in uavs
                      if uav.takeoff_weight is not None and uav.ceiling is not None])
    else:
        x = np.array([uav.takeoff_weight for uav in uavs
                      if uav.takeoff_weight is not None and uav.ceiling is not None
                      and uav.ceiling < threshold])
        y = np.array([uav.ceiling for uav in uavs
                      if uav.takeoff_weight is not None and uav.ceiling is not None
                      and uav.ceiling < threshold])

    inscriptions = ('',
                    f"Max takeoff weight, [{uavs[0].units['max takeoff weight']}]",
                    f"Ceiling, [{uavs[0].units['ceiling']}]")
    # Plotting
    fig = plt.figure("Data Analysis (weight and ceiling)")

    x_approx, y_approx = None, None
    if approx is not None:
        x_approx = np.linspace(x.min(), x.max(), 200)
        y_approx = helpers.get_poly(x, y, approx, x_approx)
    plotting(fig, x, y, *inscriptions,
             x_approx=x_approx, y_approx=y_approx, polydeg=approx)


def weight_range(uavs: tuple,
                 threshold: float = None, approx: int = None):
    if threshold is None:
        x = np.array([uav.takeoff_weight for uav in uavs
                      if uav.takeoff_weight is not None and uav.max_range is not None])
        y = np.array([uav.max_range for uav in uavs
                      if uav.takeoff_weight is not None and uav.max_range is not None])
    else:
        x = np.array([uav.takeoff_weight for uav in uavs
                      if uav.takeoff_weight is not None and uav.max_range is not None
                      and uav.max_range < threshold])
        y = np.array([uav.max_range for uav in uavs
                      if uav.takeoff_weight is not None and uav.max_range is not None
                      and uav.max_range < threshold])

    inscriptions = ('',
                    f"Max takeoff weight, [{uavs[0].units['max takeoff weight']}]",
                    f"Max range, [{uavs[0].units['range']}]")
    # Plotting
    fig = plt.figure("Data Analysis (weight and range)")

    x_approx, y_approx = None, None
    if approx is not None:
        x_approx = np.linspace(x.min(), x.max(), 200)
        y_approx = helpers.get_poly(x, y, approx, x_approx)
    plotting(fig, x, y, *inscriptions,
             x_approx=x_approx, y_approx=y_approx, polydeg=approx)


def volume_weight(uavs: tuple,
                  threshold: float = None, approx: int = None):
    if threshold is None:
        x = np.array([uav.geometry.vol for uav in uavs
                      if uav.geometry.vol is not None and uav.takeoff_weight is not None])
        y = np.array([uav.takeoff_weight for uav in uavs
                      if uav.geometry.vol is not None and uav.takeoff_weight is not None])
    else:
        x = np.array([uav.geometry.vol for uav in uavs
                      if uav.geometry.vol is not None and uav.takeoff_weight is not None
                      and uav.takeoff_weight < threshold])
        y = np.array([uav.takeoff_weight for uav in uavs
                      if uav.geometry.vol is not None and uav.takeoff_weight is not None
                      and uav.takeoff_weight < threshold])

    inscriptions = ('',
                    f"Volume, [{uavs[0].units['width']}$^3$]",
                    f"Max takeoff weight, [{uavs[0].units['max takeoff weight']}]")
    # Plotting
    fig = plt.figure("Data Analysis (volume and weight)")

    x_approx, y_approx = None, None
    if approx is not None:
        x_approx = np.linspace(x.min(), x.max(), 200)
        y_approx = helpers.get_poly(x, y, approx, x_approx)
    plotting(fig, x, y, *inscriptions,
             x_approx=x_approx, y_approx=y_approx, polydeg=approx)


def plotting(fig, x: np.ndarray, y: np.ndarray, title: str, x_label: str, y_label: str,
             with_grid: bool = True,
             x_approx: np.ndarray = None, y_approx: np.ndarray = None, polydeg: int = 1):
    ax = fig.add_axes((.15, .15, .75, .75))
    ax.plot(x, y, marker='.', ls='', color='blue', label='Data')
    if x_approx is not None and y_approx is not None:
        if polydeg < 1:
            polydeg = 1
        elif polydeg > 5:
            polydeg = 5
        ax.plot(x_approx, y_approx, color='green', lw=2, label=f'Approximation {polydeg} degree')
        ax.legend()

    if title != '':
        ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if with_grid:
        ax.grid()
