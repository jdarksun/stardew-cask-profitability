import csv

print('{| class="wikitable sortable" style="text-align: right;"')
print('!colspan="7" class="unsortable" style="position: sticky; top: 0; z-index: 100;"|No Profession')
print('|-')
print('!style="position: sticky; top: 0;"|Input Item')
print('!style="position: sticky; top: 0;"|Type')
print('!style="position: sticky; top: 0;"|Input Item Sell Price')
print('!style="position: sticky; top: 0;"|Processed Sell Price')
print('!style="position: sticky; top: 0;"|Increase in Value (g)')
print('!style="position: sticky; top: 0;"|Productivity (g/minute)')
print('!style="position: sticky; top: 0;"|Approximate g/day <sup>[[#Notes|[1]]]</sup>')

minutes_per_day = 1600

def print_row(item, item_type, input_item_sell_price, processed_sell_price, increase_in_value, productivity, gold_per_day):
    print('|-')
    print(f'|style="text-align: left;"|{{{{name|{item}}}}}')
    print(f'|style="text-align: left;"|{item_type}')
    print(f'|{input_item_sell_price}||{processed_sell_price}||{increase_in_value}||{productivity}||{gold_per_day}')

with open('Stardew CSVs - Fruit Cost.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader, None)
    for row in csv_reader:
        fruit = row[0]
        raw_item_sell_price = int(row[1])
        days = int(row[2])
        input_item_sell_price = raw_item_sell_price * 3
        processed_sell_price = input_item_sell_price * 2
        increase_in_value = processed_sell_price - input_item_sell_price
        productivity = round(increase_in_value/(days * minutes_per_day), 3)
        gold_per_day = round(increase_in_value/days, 1)
        print_row(fruit, "Wine", input_item_sell_price, processed_sell_price, increase_in_value, productivity, gold_per_day)

with open('Stardew CSVs - Other Inputs.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader, None)
    for row in csv_reader:
        item = row[0]
        input_item_sell_price = int(row[1])
        days = int(row[2])
        processed_sell_price = input_item_sell_price * 2
        increase_in_value = processed_sell_price - input_item_sell_price
        productivity = round(increase_in_value/(days * minutes_per_day), 3)
        gold_per_day = round(increase_in_value/days, 1)
        print_row(item, item, input_item_sell_price, processed_sell_price, increase_in_value, productivity, gold_per_day)

print('|-')
print('|}')

print('{| class="wikitable sortable" style="text-align: right;"')
print('!colspan="7" class="unsortable" style="position: sticky; top: 0; z-index: 100;"|Artisan')
print('|-')
print('!style="position: sticky; top: 0;"|Input Item')
print('!style="position: sticky; top: 0;"|Type')
print('!style="position: sticky; top: 0;"|Input Item Sell Price')
print('!style="position: sticky; top: 0;"|Processed Sell Price')
print('!style="position: sticky; top: 0;"|Increase in Value (g)')
print('!style="position: sticky; top: 0;"|Productivity (g/minute)')
print('!style="position: sticky; top: 0;"|Approximate g/day <sup>[[#Notes|[1]]]</sup>')

minutes_per_day = 1600

def print_row(item, item_type, input_item_sell_price, processed_sell_price, increase_in_value, productivity, gold_per_day):
    print('|-')
    print(f'|style="text-align: left;"|{{{{name|{item}}}}}')
    print(f'|style="text-align: left;"|{item_type}')
    print(f'|{input_item_sell_price}||{processed_sell_price}||{increase_in_value}||{productivity}||{gold_per_day}')

with open('Stardew CSVs - Fruit Cost.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader, None)
    for row in csv_reader:
        fruit = row[0]
        raw_item_sell_price = int(row[1])
        days = int(row[2])
        input_item_sell_price = round(raw_item_sell_price * 3 * 1.4)
        processed_sell_price = input_item_sell_price * 2
        increase_in_value = processed_sell_price - input_item_sell_price
        productivity = round(increase_in_value/(days * minutes_per_day), 3)
        gold_per_day = round(increase_in_value/days, 1)
        print_row(fruit, "Wine", input_item_sell_price, processed_sell_price, increase_in_value, productivity, gold_per_day)

with open('Stardew CSVs - Other Inputs.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader, None)
    for row in csv_reader:
        item = row[0]
        input_item_sell_price = int(row[1]) * 1.4
        days = int(row[2])
        processed_sell_price = input_item_sell_price * 2
        increase_in_value = processed_sell_price - input_item_sell_price
        productivity = round(increase_in_value/(days * minutes_per_day), 3)
        gold_per_day = round(increase_in_value/days, 1)
        print_row(item, item, input_item_sell_price, processed_sell_price, increase_in_value, productivity, gold_per_day)

print('|-')
print('|}')
