camel = r"""
The camel habitat...
@
':;
!; !'',,,',',,,,'!
;
;:
:;
!!
!!;
;
:;
;;
!!
!!
;;
!!
!!
;;
!!
!!
!,!
!,!
!!!
/_I
L_I
L_I /_I
Look at that!"""
lion = r"""
The lion habitat...
,mM^"
,MM:.
WMMm
"^MP
Y,
(--,)
w.
M
,YWMMW
'MMMMMW, WMWMW,
YP"WMMMммммммь,
MMMMWWMMMM;
:MMM[==MWMW^;
MMMMb WMW" @
MMMMMMMW "=./
dMMMMMMMM[
MMMMMMMMMMW^
) {\"^W^
Ww.
MMMP
/
\/"")
All
-;"\:
The lion is roaring!"""
deer = r"""
The deer habitat...
/1
//
11
11
1.1
//_
---
\:
:/
..@ 
,.-./\
;;-'
;;;
\\
1
;
/
IN
......"""
goose = r"""
The goose habitat...
(.
(-.
<
<-
(<<
<<
(_<_<
Beautiful!"""
bat = r"""
The bat habitat...
It's doing fine."""
rabbit = r"""
The rabbit habitat...
/1
Y:
///
jj/(^
>-"~"-
"
/
Y
jo
1
(~T~
j
>_-__/
/
1
Y
1
/1;-"~
1
/1/,-"~
WWW
--
Y
/
Y
1
I
!
1\
/"\
("
(
Y.
)
It looks fine!"""
animals=[camel, lion, deer, goose, bat, rabbit]
while True:
    print("Please enter the number of the habitat you would like to view: ")
    user_input=input("> ")
    if user_input== "exit":
        print("See you later!")
        break
    index = int(user_input)
    print(animals[index])
