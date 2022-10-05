import argparse
from csv import DictReader
import sys

parser = argparse.ArgumentParser()
with open("persons.csv", 'r', encoding='utf-8') as f:
    csv_reader = DictReader(f)
    line_count = 0
    persons = {}
    for row in csv_reader:
        if not line_count:
            column_names = list(row.keys())
            line_count += 1
            for name in column_names:
                persons[name] = []
        for name in column_names:
            persons[name].append(row[name])
parser.add_argument('--column', dest='column_name', type=str,
                    help=f'Enter one of the column names: {", ".join(column_names)}.', required=True)
args = parser.parse_args()
if args.column_name not in column_names:
    print(f'Enter one of the column names: {", ".join(column_names)}',  file=sys.stdout)
else:
    with open(f'{args.column_name}.txt', 'w', encoding='utf-8') as f:
        persons[args.column_name].sort()
        for x in persons[args.column_name]:
            f.write(x)
            f.write('\n')
            print(x, file=sys.stdout)
    print(f'The result is saved in {args.column_name}.txt', file=sys.stdout)
