"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    result = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        for elem in reader:
            neo = NearEarthObject(designation=elem['pdes'],
                                  name=elem['name'],
                                  diameter=elem['diameter'],
                                  hazardous=elem['pha'])
            result.append(neo)
    return result


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    result = []
    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)
        # ['des', 'orbit_id', 'jd', 'cd', 'dist', 'dist_min', 'dist_max', 'v_rel', 'v_inf', 't_sigma_f', 'h']
        # print(contents['fields'])
        for data in contents['data']:
            # des, cd, dist, v_rel
            ca = CloseApproach(designation=data[0],
                               time=data[3],
                               distance=data[4],
                               velocity=data[7])
            result.append(ca)
    return result
