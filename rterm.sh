#!/bin/sh

if test -e data.rt
then
	echo ''
else
	python addata.py
fi

# something about package
echo 'enter the package-name'
read package

python try.py "$package"



