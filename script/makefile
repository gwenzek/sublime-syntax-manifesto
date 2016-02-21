.DELETE_ON_ERROR:

all: syntaxes themes

download: Packages.zip Themes.zip

syntaxes: summary.syntaxes.txt

themes: summary.themes.txt

Packages.zip:
	wget "https://github.com/sublimehq/Packages/archive/master.zip" -O $@

Themes.zip:
	wget "https://github.com/Colorsublime/Colorsublime-Themes/archive/master.zip" -O $@

extracted_syntaxes: Packages.zip
	mkdir -p $@
	python extract_from_zip.py $< $@ '.sublime-syntax'

extracted_themes: Themes.zip extract_from_zip.py
	mkdir -p $@
	python extract_from_zip.py $< $@ '.tmTheme'

summary.themes.txt: extracted_themes extract_scopes.py
	mkdir -p themes
	python extract_scopes.py $< themes $@

summary.syntaxes.txt: extracted_syntaxes extract_scopes.py
	mkdir -p syntaxes
	python extract_scopes.py $< syntaxes $@

clean:
	rm -r ./*/
	rm summary.*.txt
