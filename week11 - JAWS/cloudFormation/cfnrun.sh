#!/bin/bash

function createStack(){
    echo -n "Use cfn-template: "
    read stack
    echo -n "Creat stack: "
    read name
    aws cloudformation create-stack --stack-name $name --template-body file://D:\\vscodeprojects\\aws-cloudformation-stacks\\$stack --on-failure DO_NOTHING
    if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAIL
	fi
}

function readStack(){
    echo -n "Read stack: "
    read name
    aws cloudformation describe-stacks --stack-name $name
    if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAIL
	fi
}

function updateStack(){
    if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAIL
	fi
}

function deleteStack(){
    echo -n "Delete stack: "
    read name
    aws cloudformation delete-stack --stack-name $name
    if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAIL
	fi
}

function listStacks(){
    aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE
    if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAIL
	fi
}

function helpmenu(){
	echo "\nWelcome to RDS Management System: "
	echo "C - Create Stack."
	echo "R - Read Stack"
	echo "U - Update Stack"
	echo "D - Delete Stack"
    echo "L - Lis Stacks"
	echo "X - Exit"
}

echo -n "CFN command (C/R/U/D/L/X): "
read op

while [ "$op" != "X" ]
do
	case $op in
		"C")createStack
		;;
		"R")readStack
        ;;
		"U")updateStack
		;;
		"D")deleteStack
        ;;
		"L")listStacks
		;;
		*)helpmenu
		;;
	esac
	echo -n "CFN command (C/R/U/D/L/X): "
	read op
done
echo
echo "Thank you! "