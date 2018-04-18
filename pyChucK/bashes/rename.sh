cd $1

a=0
for i in *.gif; do
    new=$(printf "%02d.gif" "$a") #04 pad to length of 4
    mv -i -- "$i" "$new"
    let a=a+1
done
