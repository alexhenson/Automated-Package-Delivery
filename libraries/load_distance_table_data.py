import csv

distance_table = {}


# This method takes a CSV file and converts it into a nested dictionary
# The first for loop will add the distances in miles to each row
# The second for loop ensures that each row has the same number of distances to and from each address
# First for loop is O(n)
# Second for loop is O(n^2) with the nested loop
def load_distance_table_data(distance_file):
    with open(distance_file) as distances:
        rows = list(csv.reader(distances))
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
