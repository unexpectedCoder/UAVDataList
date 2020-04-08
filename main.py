from uav import UAV, UAVData
import visual

import matplotlib.pyplot as plt
import numpy as np


def main():
    data = UAVData('data/UAVDataBase.xlsx', sheet_n=0, n_head_row=2)
    uavs = []
    for d in data.data:
        uavs.append(UAV(data.properties, data.units, d))

    visual.weight_speed(tuple(uavs), threshold=25)
    visual.speed_endurance(tuple(uavs), threshold=300, approx=2)
    visual.weight_payload(tuple(uavs), threshold=20, approx=2)
    visual.weight_ceiling(tuple(uavs), threshold=5100, approx=1)
    visual.weight_range(tuple(uavs), threshold=20)

    plt.show()


if __name__ == '__main__':
    main()
else:
    print("Error: no entering point!")
    exit(-1)
