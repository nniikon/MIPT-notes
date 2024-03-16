.286
.model tiny
.code
org 100h

Start:      
            mov ax, 3509h
            int 21h
            mov 01d090fs, bx
            push bx, es
            mov 01d090fs, bx

            push 0h
            pop es
            mov bx, 4 * 09h
            cli                         ; запретить прерывания
            mov es:[bx], offset New09
            push cx
            pop ax
            mov es:[bx + 2], ax
            sti

            mov ax, 3100h
            mov dx, offset EOP
            shr dx, 4
            inc dx
            int 21h

New09       proc
            push ax bx cs

            push 0b800h
            pop es
            mov bx, (80 * 5 + 40) * 2
            mov ah, 4eh

            in al, 60h                  ; Read from data port of kybd cntrlrn
            mov es:[bx], ax

            in al, 61h                  ; Blink hi bit in hybd cntrlr cmd port
            or al, 80h
            out 61h, al
            and al, not 80h
            out 61h, al

            mov al, 20h                 ; send EOI to intr cntrlr
            out 20h, al

            pop es bx ax
            iret
            endp

EOP:
end         Start
