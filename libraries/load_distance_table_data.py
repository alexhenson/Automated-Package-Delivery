import csv

distance_table = {}


def load_distance_table_data(distance_file):
    """Takes a CSV file and converts it into a nested dictionary

    The first for loop will add the distances in miles to each row. The second for loop ensures that each row has
    the same number of distances to and from each address

    Args:
        distance_file: This argument is a CSV file to be converted to a nested dictionary

    Returns:
        distance_table: This function returns a nested dictionary

    Raises:
        N/A: This function raises no errors/has no error checking

    Time complexity: Because of the nested for loop, it's time complexity is O(n^2)
    Space complexity: Because of the nested for loop the space complexity is O(n^2)
    """
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
