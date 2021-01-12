from datetime import datetime

import matplotlib.pyplot as plt

import algorithm
import graphs


# starting time
start = datetime.now()

# Using openpyxl to writing to excel file
# Give the location of the file
data_file = ".local/Worksheet.xlsx"
k_count = 3

data = algorithm.load_data(data_file)
result = algorithm.calculate(*data, k_count)

fig, ax = plt.subplots()
graphs.plot_group_scatter(result, ax)
fig.savefig('clusters.png')

graphs_list = []
for group_num, list_of_address_in_short_path in enumerate(result.list_of_address_in_short_path):
    fig, ax = plt.subplots()
    G = graphs.plot_group_route(group_num, list_of_address_in_short_path, ax)
    fig.savefig(f"G{group_num}.png")
    graphs_list.append(G)

fig, ax = plt.subplots()
graphs.plot_combined_route(result, graphs_list, ax)
fig.savefig('GT.png')

# end time
end = datetime.now()

# total time taken
print(f"Runtime of the program is {end - start}")
