src=24_spahn_dissertation
intro=24_spahn_introduction_only
style=onebib

dirs:
	mkdir -p outputs

propositions:
	pdflatex propositions
	mv propositions.pdf outputs
	make clean

dirty:
	pdflatex $(src)_$(style).tex
	mv *.pdf outputs

bib:
	make dirty style=$(style)
	biber $(src)_$(style)
	make dirty style=$(style)
	make dirty style=$(style)
	mv *.pdf outputs

clean:
	rm -f *.bcf
	rm -f *.toc
	rm -f *.run.xml
	rm -f *.abo
	rm -f *.glo
	rm -f *.log
	rm -f *.out
	rm -f *.syg
	rm -f *.ist
	rm -f *.aux
	rm -f *.bbl
	rm -f *.blg
	rm -f *.tex.bbl
	rm -f *.tex.blg
	rm -rf aux/*
	find -name '*.aux' | xargs rm -f

allclean:
	make clean
	rm -f outputs/*.pdf
	rm -f *.pdf

intro:
	make dirs
	pdflatex $(intro).tex
	biber $(intro)
	pdflatex $(intro).tex
	mv $(intro).pdf outputs
	make clean



