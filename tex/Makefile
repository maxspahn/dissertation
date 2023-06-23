src=24_spahn_dissertation

dirs:
	mkdir -p outputs

dirty:
	make dirs
	pdflatex $(src)_$(style).tex

bib:
	make dirs
	make dirty style=$(style)
	biber $(src)_$(style)
	make dirty style=$(style)
	make dirty style=$(style)
	mv *.pdf outputs
	make clean style=$(style)

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


