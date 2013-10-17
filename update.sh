#!/bin/sh

if test -e data.rt
then
	rm data.rt
	python addata.py
else
	python addata.py

echo 'updated data.rt file'
