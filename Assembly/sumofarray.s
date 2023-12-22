# CIS 216 - Computer Organization and Design
# Amari Grimes 
# SumofArray.s

.data
#define the array
array: .word 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
#define the length of the array
length: .word 12
#define sum
sum: .word 0
#define strings
hdr: .asciiz "Sum: "

.text
.globl main
.ent main
main:
        #load and print the string
        la $a0, hdr
        li $v0, 4
        syscall

        #store the length from earlier in t0
        lw $t0, length 
        #store loop index in t1
        li $t1, 0        
        #store the full sum in t2
        li $t2, 0
        la $t3, array #store first value in t3

sumLoop:
        lw $t4, ($t3) 
        add $t2, $t2, $t4 
        add $t1, $t1, 1 
        add $t3, $t3, 4      
        blt $t1, $t0, sumLoop
        sw $t2, sum 

        li $v0, 1
        move $a0, $t2
        syscall
 
        li $v0, 10
        syscall
.end main
