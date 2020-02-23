#!/usr/bin/python
import hashlib
userpt = raw_input("Enter your plaintext: ")
userhash = raw_input("Enter the hash: ")
print ("Starting to compare...")

#Generates a Hash from the PT and sets an object
genhash_md5=(hashlib.md5(userpt).hexdigest())
genhash_sha256 =(hashlib.sha256(userpt).hexdigest())
genhash_sha224 =(hashlib.sha224(userpt).hexdigest())
genhash_sha512 =(hashlib.sha512(userpt).hexdigest())
genhash_sha1 = (hashlib.sha1(userpt).hexdigest())
genhash_sha384 = (hashlib.sha384(userpt).hexdigest())
if (genhash_md5) == (userhash):
    print "========== MD5 Match Below! =========="
    print "Your hash: ",userhash
    print "Generated hash: ",genhash_md5
elif (genhash_sha256) == (userhash):
    print "========== SHA256 Match Below! =========="
    print "Your hash: ", userhash
    print "Generated hash: ", genhash_sha256
elif (genhash_sha224) == (userhash):
    print "========== SHA224 Match Below! =========="
    print "Your hash: ", userhash
    print "Generated hash: ",genhash_sha224
elif (genhash_sha512) == (userhash):
    print "========== SHA512 Match Below! =========="
    print "Your hash: ", userhash
    print "Generated hash", genhash_sha512
elif (genhash_sha1) == (userhash):
    print "========== SHA1 Match Below! =========="
    print "Your hash: ", userhash
    print "Generated hash: ", genhash_sha1
elif (genhash_sha384) == (userhash):
    print "========== SHA1 Match Below! =========="
    print "Your hash: ", userhash
    print "Generated hash: ", genhash_sha384
else:
    print("No match found...better try Tinder!")




