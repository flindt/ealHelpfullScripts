for file in /home/pfl/git/*.txt
do
	N=$(cat log1.txt | grep ^commit | wc -l)
	echo $file $N
done
