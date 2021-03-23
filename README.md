ACS ACR122U NFC Reader / Writer - Experimental fork
=========

Python based reader/writer that is used to read tag data from the NFC ISO 14443 Type A and B cards, Mifare, FeliCa, and all 4 types of NFC (ISO/IEC 18092) tags.

Code provides a basic framework used to grab tag data.

NFC2keyboard.py acts as a virtual keyboard and types the (4 byte) UID when a card is detected and presses enter, presses enter again when card is removed. 

Observer.py is a test of the Observer pattern from [the pyscard user guide]

scTest.py is sort of an iteration from before virtual keyboard funtionality was added.

#Tech
[pyscard]- python for smart cards

[pynput] - for virtual keyboard stuff

License (inherited by fork)
----
MIT

[pyscard]:http://pyscard.sourceforge.net/
[the pyscard user guide]:https://pyscard.sourceforge.io/user-guide.html
[pynput]:https://pypi.org/project/pynput/
