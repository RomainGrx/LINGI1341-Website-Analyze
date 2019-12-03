TEX=./main.tex
PDF=./main.pdf

.PHONY : pdf clean hardclean

default : pdf clean

open :
	cd ./Latex && open main.pdf

pdf :
	cd ./Latex && pdflatex $(TEX)

clean : 
	cd ./Latex && rm -f *.o *.aux *.out *.log *.aux

hardclean : 
	cd ./Latex && rm -f $(PDF) *.o *.aux *.out *.log *.aux