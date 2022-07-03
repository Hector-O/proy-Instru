;
; Transmite.asm
;
; Created: 13/06/2022 04:44:21 p. m.
; Author : hecth
;


; Replace with your application code
	.def temp=r16
	.def send=r17
	.def cont1=r18
	.def cont2=r19
	.def cont3=r20
	.cseg
	.org 0
	jmp reset

	/*.org $024
	jmp recibe*/

reset:	ldi temp, $00
	out ddrb, temp//pone b como entrada
	out ddrc, temp//pone c como entrada

ldi temp, $fe
	out ddrd, temp ; pone a salida excepto d1 (rx entrada, tx salida)
	;ucsr0a, registro ya confugurado por reset
	ldi temp, $98
	sts ucsr0b, temp ; habilita rx interrupcion, habilita receptor y transmisor
	;ucsr0c, registro ta configurado por reset (8 bits)
	ldi temp, 103
	sts ubrr0l, temp; confugura a 9600 Bits Por Segundo
	sei

main:in send, pinc//lee del pin C
	andi send, $3f// se queda con los primeros 6 bits
	in temp, pinb//lee del pin B
	andi temp, $03// se queda con los primeros 2 bits

	lsl send//desplaza 2 bits para insertar los nuevos
	lsl send

	or send, temp

	com send

	sts udr0, send; escribe en el registro
	call delay_200ms
	call delay_200ms
	call delay_200ms
	jmp main

/*
recibe:	lds temp, udr0; lee registro de datos
	sts udr0, temp; escribe en el registro
	reti*/  
delay_200ms:ldi cont1, 8
lazo3:	ldi cont2, 200
lazo2:	ldi cont3, 200
lazo1:	nop
	nop
	nop
	nop
	nop
	nop
	nop
	dec cont3
	brne lazo1
	dec cont2
	brne lazo2
	dec cont1
	brne lazo3
	reti