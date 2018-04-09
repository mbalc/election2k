#!/usr/bin/env bash
mkdir -p data

cd data

#mkdir -p gminy
mkdir -p obwody
#mkdir -p powiaty

(
#    curl http://prezydent2000.pkw.gov.pl/gminy/gm-okr\[01-68\].xls -o "gminy/gm-okr#1.xls"
    curl http://prezydent2000.pkw.gov.pl/gminy/obwody/obw\[01-68\].xls -o "obwody/obw#1.xls"
    curl http://prezydent2000.pkw.gov.pl/gminy/zal1.xls -o "zal1.xls"
#    curl http://prezydent2000.pkw.gov.pl/gminy/zal2.xls -o "zal2.xls"
#    curl http://prezydent2000.pkw.gov.pl/gminy/kraj.zip -o "kraj.zip"
#    unzip kraj.zip -d powiaty
#    rm kraj.zip
    echo "Press Q to exit log viewer!"
) | less


