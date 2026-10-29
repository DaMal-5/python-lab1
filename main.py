import sys

def read_meas(filename : str) -> dict:
    city_stats = {}
    try:
        with open(filename, "rb") as f:
            for line in f:
                text = line.decode("utf-8").split(";")
                station = text[0]
                temp = float(text[1])
                if station not in city_stats:
                    city_stats[station] = [temp, temp, temp, 1] # max, min, sum, quant
                else:
                    if temp > city_stats[station][0]:
                        city_stats[station][0] = temp
                    if temp < city_stats[station][1]:
                        city_stats[station][1] = temp
                    city_stats[station][2] += temp
                    city_stats[station][3] += 1
    except FileNotFoundError:
        print(f"Файл с таким именем не найден", file=sys.stderr)
        sys.exit(1)
    return city_stats