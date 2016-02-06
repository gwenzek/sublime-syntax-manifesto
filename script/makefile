.DELETE_ON_ERROR:

all: scopes

download: syntaxes

syntaxes:
	mkdir syntaxes
	python download.py
	rm Packages-master.zip

scopes: syntaxes
	mkdir scopes
	python extract_scopes.py

clean:
	# rm -r syntaxes
	rm -r scopes
