src=spahn
intro=intro_only
style=ob

dirs:
	mkdir -p outputs

propositions:
	pdflatex propositions
	mv propositions.pdf outputs

svg:
	pdflatex --shell-escape $(src)_$(style).tex

dirty:
	pdflatex -draftmode $(src)_$(style).tex

final:
	pdflatex $(src)_$(style).tex

bib:
	make dirty style=$(style)
	biber $(src)_$(style)
	make dirty style=$(style)
	make final style=$(style)
	mv $(src)_$(style).pdf outputs

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
	find -name '*.aux' | xargs rm -f

allclean:
	make clean
	rm -f outputs/*.pdf
	rm -f *.pdf
	rm -f svg-inkscape/*

intro:
	make dirs
	pdflatex $(intro).tex
	biber $(intro)
	pdflatex $(intro).tex
	mv $(intro).pdf outputs
	make clean



