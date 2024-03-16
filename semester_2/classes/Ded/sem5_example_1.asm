.286
.model tiny
.code
org 100h

Start:      push 0b800h
            pop es
            mov bx, (80 * 5 + 40) * 2
            mov ah, 4eh

Next:       in al, 60h                  ; Read from data port of kybd cntrlrn
            mov es:[bx], ax

            cmp al, 11d
            jne Next

            ret
end         Start
