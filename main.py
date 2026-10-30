import sys
import math

def read_measurements(filename: str) -> dict:
    city_stats = {}
    try:
        with open(filename, "rb") as f:
            for line in f:
                text = line.decode("utf-8").split(";")
                station = text[0]
                temperature = float(text[1])
                if station not in city_stats:
                    city_stats[station] = [temperature, temperature, temperature, 1] # max, min, sum, quant
                else:
                    if temperature > city_stats[station][0]:
                        city_stats[station][0] = temperature
                    if temperature < city_stats[station][1]:
                        city_stats[station][1] = temperature
                    city_stats[station][2] += temperature
                    city_stats[station][3] += 1
    except FileNotFoundError:
        print(f"Файл с таким именем не найден", file=sys.stderr)
        sys.exit(1)
    return city_stats



def normalize_dict(city_stats: dict) -> dict:
    normalized = {}
    for station in city_stats:
        avg = city_stats[station][2] / city_stats[station][3]
        rounded_avg = math.floor(avg * 10 + 0.5) / 10
        normalized[station] = (city_stats[station][1], rounded_avg, city_stats[station][0])
    return normalized



def print_sorted(normalized: dict) -> None:
    sorted_keys = sorted(normalized.keys())
    for key in sorted_keys:
        min_by_station, avg_by_station, max_by_station = normalized[key]
        print(f"{key};{min_by_station:.1f};{avg_by_station:.1f};{max_by_station:.1f}", end="\n")



def main():
    if len(sys.argv) != 2:
        print("ошибка: укажите путь к файлу.", file=sys.stderr)
        sys.exit(1)
    filename = sys.argv[1]
    stats = read_measurements(filename)
    normalized_stats = normalize_dict(stats)
    print_sorted(normalized_stats)


if __name__ == "__main__":
    main()