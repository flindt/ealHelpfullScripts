for file in /home/pfl/git/*.txt
do
	echo $file 
	cat log1.txt | grep ^commit | wc -l
done
