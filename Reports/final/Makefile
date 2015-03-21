main = report

all: once.a

once.%:
	pdflatex $(main)

bib:
	bibtex $(main)

clean:
	rm -f $(main).{aux,log,toc,bbl,blg,out}

remove: clean
	rm -f $(main).pdf

release: remove once.a bib once.b once.c

