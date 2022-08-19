.PHONY: clean distclean

all: snellen.pdf

%.pdf: %.tex
	xelatex -file-line-error -interaction=nonstopmode --shell-escape $<
	command -v pdfsizeopt && pdfsizeopt --quiet $@ $@; true

clean:
	rm -f *.aux *.log *.out

distclean: clean
	rm snellen.pdf
