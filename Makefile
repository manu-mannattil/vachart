.PHONY: clean distclean

all: snellen.pdf

%.pdf: %.tex
	xelatex $<
	command -v pdfsizeopt && pdfsizeopt $@ $@; true

clean:
	rm -f *.aux *.log *.out

distclean: clean
	rm snellen.pdf
