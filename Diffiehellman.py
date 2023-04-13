print("Both parties agree to a single prime")
prime= int(input("Enter a prime number:"))

print("Both parties agree to a single prime")
root=int(input("Enter a primitive root number:"))

K1secret = int(input("Enter K1 secret key:"))
K2secret = int(input("Enter K2 secret key:"))

print("\n")

print("Enter K1 public key -> A = root^K1sec*mod(prime))")
K1public = (root**K1secret)%prime
print("\n")
print("K1 Public Key is",K1public,"\n")


print("Enter K2 public key -> B = root^K2sec*mod(prime))")
K2public = (root**K2secret)%prime
print("\n")
print("K2 Public Key is",K2public,"\n")


print ("K1 calculates the shared key ")
K1key=(K1public**K2secret)%prime
print ("Party1 calculates the shared key and results: ",K1key, "\n")

print ("K2 calculates the shared key )")
K2key =(K2public**K2secret)%prime
print ("Party2 calculates the shared key and gets", K2key, "\n")
print("Attacker does not know about the secret key of either K1 or K2")