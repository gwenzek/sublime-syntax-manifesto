.DELETE_ON_ERROR:

all: syntaxes themes

download: Packages.zip Themes.zip

Packages.zip:
	wget "https://github.com/sublimehq/Packages/archive/master.zip" -O $@

Themes.zip:
	wget "https://github.com/Colorsublime/Colorsublime-Themes/archive/master.zip" -O $@

extracted_syntaxes: Packages.zip
	mkdir $@
	python extract_from_zip.py $< $@ '.sublime-syntax'

syntaxes: extracted_syntaxes
	mkdir $@
	python extract_syntaxes_scopes.py $< $@

extracted_themes: Themes.zip
	mkdir $@
	python extract_from_zip.py $< $@ '.tmTheme'

themes: extracted_themes
	mkdir -p $@
	python extract_themes_scopes.py $< $@

clean:
	rm -r ./*/
	rm summary.*.txt
