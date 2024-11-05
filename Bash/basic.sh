#!/bin/bash

# is inline annotation
:<<!
is multiple annotation
variable declaration: string initialized
	string:
		bare: \ special char
		single quote: pure string
		double quote: ---
	number:int only. $((a)) to use. -gt to use
	array

a=1				cannot a = 1
if [ $a == $ b]; then		cannot[$a == $b]		
!

read -p 'who are you? ' person
echo 'Hello '$person' !'

v1=hello\ world\!
v2='hello world!'
echo hello, $v1, $v2, 1$v1'7'$v2
echo ${v1:2:3}, ${#v1}

a=10
b=3
echo $((a+b)), $((a-b)), $((a*b)), $((a/b)), $((a%b))

A=(apple banana guava)
echo $A, ${A[0]}, ${A[1]}, ${A[2]}
echo ${#A}, ${#A[0]}, ${#A[1]}, ${#A[2]}
echo ${A[*]}, ${#A[*]}

if [ $a -gt $b ]; then
	echo 'a is bigger'
elif [ $a == $b ]; then
	echo 'a is equal to b'
else
	echo 'b is bigger'
fi

if [ $a == $((10)) ] && [ $b == $((3)) ]; then
	echo 'a is ten and b is three'
fi

for num in 1 2 3; do
	echo hello $num
done

for fruit in ${A[*]}; do
	echo $fruit
done

s=0
for ((i=0;i<10;i++)); do
	s=$((s+i))
done
echo $s

s=1
while [ $s -lt $((100)) ]; do
	s=$((s*2))
done
echo $s

function sayHi(){
	echo hello, ${0}, ${1}, ${2}
	echo $0, $1, $2   # out parameter
}
sayHi tree bird

# ln src dest    # hard link # cannot be folder # same color # write one affect the other # delete one, the other remains   # check ls -i
# ln -s src dest # soft link # can be folder    # cyan color # write one affect the other # delete source, the other failed # check ls -l
