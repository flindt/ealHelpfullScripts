for file in /home/pfl/git/*.txt
do
	N=$(cat $file | grep ^commit | wc -l)
	echo $file $N
done
