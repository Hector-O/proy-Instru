;
; contador_usart.asm
;
; Created: 08/06/2022 05:58:52 p. m.
; Author : hecth
;


; Replace with your application code
	.def temp=r16
	.def cont=r17
	.def cont1=r18
	.def cont2=r19
	.def cont3=r20
	.cseg
	.org 0
	jmp reset

	;.org $024
	;jmp recibe

reset:	ldi temp, $fe
	ldi cont, 0
	out ddrd, temp ; pone a salida excepto d1 (rx entrada, tx salida)
	;ucsr0a, registro ya confugurado por reset
	ldi temp, $98
	sts ucsr0b, temp ; habilita rx interrupcion, habilita receptor y transmisor
	;ucsr0c, registro ta configurado por reset (8 bits)
	ldi temp, 103
	sts ubrr0l, temp; confugura a 9600 Bits Por Segundo
	sei

main:inc cont
	sts udr0, cont
	call delay_500ms
	jmp main

;recibe:	lds temp, udr0; lee registro de datos
;	sts udr0, temp; escribe en el registro
;	reti

delay_500ms:	ldi cont1, 16
lazo_3:	ldi cont2, 250
lazo_2:	ldi cont3, 200
lazo_1:	nop
nop
nop
nop
nop
nop
nop
nop
nop
dec cont3
brne lazo_1
dec cont2
brne lazo_2
dec cont1
brne lazo_3
ret