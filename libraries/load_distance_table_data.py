import csv

distance_table = {}

def load_distance_table_data(distance_file):
    with open(distance_file) as distances:
        rows = list(csv.reader(distances))
        for row in rows:
            row[0] = row[0].strip().splitlines()[0]
        cols = [row[0] for row in rows]
        for row in rows:
            distance_table[row[0]] = {}
            for i, v in enumerate(row[1:]):
                distance_table[row[0]][cols[i]] = float(v if v else 0)
        for a in cols:
            for b in cols:
                if distance_table[a][b]:
                    distance_table[b][a] = distance_table[a][b]
                else:
                    distance_table[a][b] = distance_table[b][a]

    return distance_table

    # with open(package_file) as packages:
    #     for row in csv.DictReader(packages):
    #         print(row['Address'], distance_table[row["Address"]]["HUB"])
