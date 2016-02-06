.DELETE_ON_ERROR:

all: scopes

download: master.zip

master.zip:
	wget "https://github.com/sublimehq/Packages/archive/master.zip"

syntaxes: master.zip
	mkdir $@
	python extract_syntaxes.py $< $@

scopes: syntaxes
	mkdir $@
	python extract_scopes.py

clean:
	# rm master.zip
	rm -r syntaxes
	rm -r scopes
