            CLD         ; DF = 0 (DI++)             ; флаг направления
            STOSB       ; ES:[DI++] = AL
            STOSW       ; ES:[DI]   = AL; DI += 2;
            STOSD
            STOSQ

            mov cx, 40d
NEXT:       STOSW
            loop NEXT

            mov cx, 40d
            rep stosw   ; while (cx--) {es:[di] = AX; DI += 2}

            LODSB       ; AL = ds:[SI++]                            ; ds писать необязательно, т.к. и так юзается по дефолту
            LODSW, ...

            MOVSB, ...  ; ES:[DI++] = ds:[SI++]

            CMPSB       ; CMP ds:[SI++], ES:[DI++]

            REP CMPSB   ; while (CX--) CMP ds:[SI++], ES:[DI++]     ; кринжж

            REPE CMPSB   ; while (CX-- && ES:[DI++] == ds:[SI++])   ;
            REPNE CMPSB  ; while (CX-- && ES:[DI++] != ds:[SI++])   ;

            SCASB        ; CMP AL, ES:[DI++]

            ; начало strlen
            xor al, al
            repne scasb

HOMEWORK:   strlen, memchr, memset, memcpy (dnc about direction), movmem (smart), memcmp
