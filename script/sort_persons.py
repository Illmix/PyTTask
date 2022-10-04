import argparse
from csv import DictReader

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
parser.add_argument('--column', '--list', dest='column_name', nargs='+', type=str,
                    help=f'Enter one of the column names: {", ".join(column_names)}.'
                         f' Do the same, but add stdout at the end to output the list', required=True)
args = parser.parse_args()
if args.column_name[0] not in column_names:
    print(f'Enter one of the column names: {", ".join(column_names)}')
try:
    if args.column_name[1] == 'stdout':
        persons[args.column_name[0]].sort()
        for x in persons[args.column_name[0]]:
            print(x)
    else:
        print(f'Unknown command {args.column_name[1]}. To see a list of commands, run: python sort_persons.py -h')
except IndexError:
    with open(f'{args.column_name[0]}.txt', 'w') as f:
        persons[args.column_name[0]].sort()
        for x in persons[args.column_name[0]]:
            f.write(x)
            f.write('\n')
    print(f'The result is saved in {args.column_name[0]}.txt')
