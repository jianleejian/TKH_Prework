Last login: Tue May 18 22:17:03 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
jians-Air:~ jianlee$ python

WARNING: Python 2.7 is not recommended. 
This version is included in macOS for compatibility with legacy software. 
Future versions of macOS will not include Python 2.7. 
Instead, it is recommended that you transition to using 'python3' from within Terminal.

Python 2.7.16 (default, Feb 28 2021, 12:34:25) 
[GCC Apple LLVM 12.0.5 (clang-1205.0.19.59.6) [+internal-os, ptrauth-isa=deploy on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> names_list=["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]
>>> longest_name = ' '
>>> for name in names_list:
...     if len(name) > longest_name:
...             longest_name=name
...     else:
...             pass
... print longest_name
  File "<stdin>", line 6
    print longest_name
        ^
SyntaxError: invalid syntax
>>> 
