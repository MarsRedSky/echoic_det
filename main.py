import pandas as pd, csv, os

def get_csv():
# open and read CSV file
    with open("echoic_data_test.csv") as csvfile:
       x = pd.read_csv(csvfile)
       # make_tuple(x = x[x.cue == "quoted"])
       make_tuple(x)

def make_tuple(x):
    data = [tuple(row) for row in x.values]
    response_cleaner(data)

def response_cleaner(data):
    quote = ""
    ls_results = []
    for cue,id,sarc,parent,response in data:
        if cue == "quoted":
            response = response.split()
            for word in response:
                if word.startswith('"') and word.endswith('"'):
                    quote = word
                    quote = quote.replace('"','')

                    ls_results.append(quote_comparer(parent, quote))
                    break
        else:
            ls_results.append("N/A")
    tuple_zip(data,ls_results)

def quote_comparer(parent, quote):
    store = ""
    for char in parent:
        if char.isalpha() or char.isspace(): # this should be replaced by code that allows for highphenated words
            store = store + char
    if quote not in store:
        return 0
    else:
        return 1

def tuple_zip(data,results):
    new_data = []
    for count, item in enumerate(data):
        c1,c2,c3,c4,c5 = item
        new_item = c1, c2, c3, c4, c5, results[count]
        new_data.append(new_item)
        print(new_item)
    # print(new_data)
    csv_writer(new_data)

def csv_writer(final):
    directory = "results"
    if not os.path.exists(directory):
        os.makedirs(directory)
    csv_file = "echoic_results.csv"
    with open(os.path.join(directory,csv_file), "wt") as csv_file:
        fieldnames = ["cue", "id","sarc","parent","response","mention"]
        writer = csv.writer(csv_file)
        writer.writerow(fieldnames)
        for data in final:
            writer.writerow(data)

get_csv()
