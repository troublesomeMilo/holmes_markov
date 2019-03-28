# holmes_markov
Sherlock Holmes Markov chain generator

Created this as a simple project while learning Python

fetch_data
Uses the Requests library to get text from the Hound of the Baskervilles from gutenberg.org.
Uses the BeautifulSoup library to parse the text.
Uses the io module to write the text to a txt file.

cc_markov
A Markov chain generator developed to support folks learning Python.
Takes text as input.
Can be called to generate a Markov chain based on the seed word and input text.

run
Initiates fetch_data.
Feeds the generated text into cc_markov.
Prints generated chain.
