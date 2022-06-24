import tabula

table = tabula.read_pdf('weather.pdf', pages = 1)

print(type(table[0]))

type(table[0]).to_csv('output.csv', index = None)