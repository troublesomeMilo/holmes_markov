from markov_python.cc_markov import MarkovChain
import fetch_data

hounds = MarkovChain()

hounds.add_file('D:\Projects\holmes_markov\Hounds.txt')

output = hounds.generate_text()

output = ' '.join(output)

output = output.capitalize() + "."

print output