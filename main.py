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
    visual.speed_endurance(tuple(uavs), threshold=300, approx=1)
    visual.weight_payload(tuple(uavs), threshold=20, approx=1)
    visual.weight_ceiling(tuple(uavs), threshold=5100)
    visual.weight_range(tuple(uavs), threshold=20)
    visual.volume_weight(tuple(uavs), threshold=10, approx=1)

    # Среднее
    mean_weight = np.array([uav.takeoff_weight for uav in uavs if uav.takeoff_weight is not None]).mean()
    mean_speed = np.array([uav.max_speed for uav in uavs if uav.max_speed is not None]).mean()
    mean_endurance = np.array([uav.endurance for uav in uavs if uav.endurance is not None]).mean()
    mean_payload = np.array([uav.payload for uav in uavs if uav.payload is not None]).mean()
    mean_ceiling = np.array([uav.ceiling for uav in uavs if uav.ceiling is not None]).mean()
    mean_range = np.array([uav.max_range for uav in uavs if uav.max_range is not None]).mean()
    mean_volume = np.array([uav.geometry.vol for uav in uavs if uav.geometry.vol is not None]).mean()
    print(f"\nMean weight: {mean_weight}\n"
          f"Mean max speed: {mean_speed}\n"
          f"Mean endurance: {mean_endurance}\n"
          f"Mean payload: {mean_payload}\n"
          f"Mean ceiling: {mean_ceiling}\n"
          f"Mean range: {mean_range}\n"
          f"Mean volume: {mean_volume}\n")

    n_electric, n_others = 0, 0
    for uav in uavs:
        if uav.engine == 'Electric':
            n_electric += 1
        else:
            n_others += 1
    print(f"Part of electric engines: {n_electric / (n_electric + n_others) * 100}\n"
          f"Part of other engine's types: {n_others / (n_electric + n_others) * 100}\n")

    plt.show()


if __name__ == '__main__':
    main()
else:
    print("Error: no entering point!")
    exit(-1)
