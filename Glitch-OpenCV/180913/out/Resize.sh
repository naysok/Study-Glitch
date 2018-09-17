#!/bin/bash
for file in *.jpg; do sips --resampleWidth 720 $file --out ${file%.jpg}-Resize.jpg; done


