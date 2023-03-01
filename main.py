from sqliteoperation import SqliteOperation
from task_solution import TaskSolution

ts = TaskSolution()

one_data = ts.read_one_file('vocab.enron.txt')
print(len(one_data))
all_data = ts.read_all_file()
print(len(all_data))

# print(ts.task_q1(one_data))
# print(ts.task_q1(all_data))
# print(ts.task_q2(one_data))

# print(ts.task_q2(all_data))

# print(ts.task_q3(one_data))
# print(ts.task_q3(all_data))

conn = SqliteOperation('task_4.db')
table = 'beg_of_words'

table_structure = {"file1_enron": "text", "file2_kos": "text", "file3_nips": "text",
                   "file4_nytimes": "text", "file5_pubmed": "text"}
print(conn.Create_table(table, table_structure))

print(conn.select_data_table(table))

print(conn.select_count_table(table))

ts.task_q4(conn, table)
