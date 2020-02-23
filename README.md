# HashCompare
HashCompare compares generated hashes to an unknown hash. During multiple web app pentests I've come across a need for a fast way to compare a unkown hash to possible known variables I've set.
_Example:_ On a pentest you have a cookie set upon login that looks like a hash, but you want to know if it might be your hashed password or username. This tool may come in handy to check that.

**Currently Supported Hash Types**
* MD5
* SHA256
* SHA224
* SHA512
* SHA1
* SHA384

# Example

```
codeviper@HYDRA:/mnt/c/Development/Crypto/HashCompare$ python hashcompare.py
Enter your plaintext: Sup3rS3cr3tP@ss!*;1234
Enter the hash: 77c8534d8c05707bc194d7f5a63353f53d9a656421ec9084f6f46bef205a883a
Starting to compare...
========== SHA256 Match Below! ==========
Your hash:  77c8534d8c05707bc194d7f5a63353f53d9a656421ec9084f6f46bef205a883a     
Generated hash:  77c8534d8c05707bc194d7f5a63353f53d9a656421ec9084f6f46bef205a883a
```
